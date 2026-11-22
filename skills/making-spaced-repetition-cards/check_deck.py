#!/usr/bin/env python3
"""Check an Anki TSV deck written to this skill's format.

Usage: python3 check_deck.py DECK.tsv [--source TEXT.md ...] [--core]

Prints one line per problem (ERROR fails the deck, WARN is a judgement call
to look at) and a summary. Exit code 1 if any ERROR.
"""
import html, re, sys, unicodedata
from collections import Counter

REQUIRED = ["separator", "html", "guid column", "tags column", "columns"]
TYPES = {"concept", "why", "contrast", "list", "tf", "mc", "cloze", "quote", "line", "reflect"}
MAX_ANSWER = {"reflect": None}  # default 25 (hard); warn above TARGET
TARGET = 15
MAX_FRONT = 30
STOP = set("""a an the of to in on for and or but is are was were be been it its this that
these those as by with from at what which who whom why how does do did according
he she they his her their you your we our not no""".split())

def strip(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(s)

def norm(s):
    s = unicodedata.normalize("NFKC", strip(s))
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\[\^[^\]]*\]", "", s)
    s = re.sub(r"[*_`#>\[\]]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()

def words(s):
    return re.findall(r"[\w'’-]+", strip(s))

def answer_line(back):
    return re.split(r"<br\s*/?>", back, maxsplit=1)[0]

def trigrams(s):
    w = [x.lower() for x in words(s)]
    return {tuple(w[i:i+3]) for i in range(len(w) - 2)} or {tuple(w)}

def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    path, sources, core = argv[1], [], "--core" in argv
    if "--source" in argv:
        i = argv.index("--source") + 1
        while i < len(argv) and not argv[i].startswith("--"):
            sources.append(norm(open(argv[i], encoding="utf-8").read())); i += 1
    lines = open(path, encoding="utf-8").read().splitlines()
    errors, warns = [], []
    E = lambda n, m: errors.append(f"ERROR line {n}: {m}")
    W = lambda n, m: warns.append(f"WARN  line {n}: {m}")

    heads, rows = {}, []
    for n, l in enumerate(lines, 1):
        if l.startswith("#"):
            k, _, v = l[1:].partition(":")
            if k in heads: E(n, f"header #{k} repeated")
            heads[k] = v
        elif l.strip():
            rows.append((n, l.split("\t")))
    for k in REQUIRED:
        if k not in heads: E(0, f"missing header #{k}")
    if heads.get("separator", "").lower() != "tab": E(0, "#separator must be tab")
    cols = heads.get("columns", "").split("\t")
    if cols != ["GUID", "Front", "Back", "Tags"]:
        E(0, "#columns must be GUID<TAB>Front<TAB>Back<TAB>Tags")
    if heads.get("guid column") != "1" or heads.get("tags column") != "4":
        E(0, "#guid column must be 1 and #tags column 4")

    guids, fronts, answers, types = Counter(), [], {}, Counter()
    for n, r in rows:
        if len(r) != 4:
            E(n, f"{len(r)} columns, expected 4"); continue
        guid, front, back, tags = r
        tagl = tags.split()
        t = [x.split("::", 1)[1] for x in tagl if x.startswith("type::")]
        typ = t[0] if t else None
        if typ not in TYPES: E(n, f"needs one type:: tag from {sorted(TYPES)}")
        types[typ] += 1
        if not guid: E(n, "empty GUID")
        guids[guid] += 1
        if "<small>Source:" not in back: E(n, "back has no <small>Source: …</small> line")
        if '"' in front + back and not re.search(r"&quot;|“|”", front + back) and re.search(r'(^|\t)"', "\t".join(r)):
            W(n, "field starts with a straight double quote; Anki may treat it as CSV quoting")
        ans = answer_line(back)
        nf, na = len(words(front)), len(words(ans))
        qmarks = re.sub(r"[“\"][^”\"]*[”\"]", "", front).count("?")
        if qmarks > 1 or (front.count("?") == 0 and typ not in ("line", "reflect", "quote", "cloze", "tf")):
            E(n, f"front has {qmarks} question marks; ask exactly one thing")
        if re.search(r",\s*(and|or) (what|why|how|which|who|where|when)\b|\b(and|or) (what|why|how|which|who) (is|are|was|were|does|do|did|can|should|would)\b", strip(front), re.I):
            E(n, "front asks two things ('… and what/why/how …')")
        if nf > MAX_FRONT: E(n, f"front is {nf} words (max {MAX_FRONT})")
        lim = MAX_ANSWER.get(typ, 25)
        if lim and na > lim: E(n, f"answer line is {na} words (max {lim}); split the card or cut")
        elif lim and na > TARGET and typ not in ("line", "quote"): W(n, f"answer line is {na} words (target {TARGET})")
        if typ == "tf" and not re.match(r"\s*(true|false)\b", strip(front), re.I) and "true or false" not in strip(front).lower():
            E(n, "tf card front should start 'True or false:'")
        if typ == "tf" and not re.match(r"\s*(true|false)\b", strip(ans), re.I):
            E(n, "tf card answer must start with True or False")
        if typ == "mc" and len(re.findall(r"\([a-e]\)", front)) < 3:
            E(n, "mc card needs three or more options like (a) (b) (c)")
        if typ == "cloze" and "____" not in front:
            E(n, "cloze card front needs a ____ blank")
        if re.search(r"\b(stanza|verse|chapter|ch\.|passage|section|line|§)\s*(\d|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\b", strip(front), re.I):
            E(n, "front cues on a stanza/chapter number; cue on content instead")
        if typ not in ("line", "quote", "reflect", "tf", "mc", "cloze"):
            aw = {w.lower() for w in words(ans)} - STOP
            fw = {w.lower() for w in words(front)} - STOP
            if len(aw) >= 2 and len(aw & fw) / len(aw) > 0.5:
                W(n, "most of the answer's words are on the front (leaky front?)")
        if sources and typ in ("line", "quote"):
            a = norm(ans).strip(" .,;:!?")
            if len(a.split()) >= 3 and not any(a in src for src in sources):
                E(n, f"{typ} answer not found verbatim in source: “{strip(ans)[:60]}”")
        if sources:
            for q in re.findall(r"[“\"]([^”\"]{12,})[”\"]", strip(front) + " " + strip(ans)):
                for frag in re.split(r"\s*(?:…|\.\.\.|_{2,}|\s/\s)\s*", q):
                    f = norm(frag).strip(" .,;:!?")
                    if len(f.split()) >= 3 and not any(f in s for s in sources):
                        E(n, f"quote not found verbatim in source: “{frag[:60]}”")
        fronts.append((n, front, trigrams(front)))
        key = norm(ans)
        if key in answers and typ not in ("reflect",):
            W(n, f"same answer as line {answers[key]} (duplicate idea?)")
        answers.setdefault(key, n)
    for g, c in guids.items():
        if c > 1: E(0, f"GUID {g!r} used {c} times")
    for i in range(len(fronts)):
        for j in range(i + 1, len(fronts)):
            a, b = fronts[i][2], fronts[j][2]
            if len(a & b) / max(1, len(a | b)) > 0.5:
                W(fronts[j][0], f"front is near-duplicate of line {fronts[i][0]}")

    total = sum(types.values())
    graded = total - types["reflect"] - types["line"] - types["quote"]
    deep = types["why"] + types["contrast"]
    if graded >= 6 and deep * 3 < graded:
        warns.append(f"WARN  deck: only {deep} of {graded} idea cards are why/contrast; argument books should aim for a third or more")
    if core and total > 150:
        warns.append(f"WARN  deck: core deck has {total} cards; is every one the best card for its claim?")
    for m in errors + warns: print(m)
    print(f"\n{total} cards · types: " + ", ".join(f"{k} {v}" for k, v in sorted(types.items(), key=lambda x: str(x[0]))) +
          f" · {len(errors)} errors · {len(warns)} warnings")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
