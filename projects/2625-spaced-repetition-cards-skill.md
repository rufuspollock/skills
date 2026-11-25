---
title: Spaced-Repetition Cards Skill
description: A reusable agent skill that turns a text or book into a good Anki / spaced-repetition deck, grounded in research and in the library repo's decks.
created: '2026-11-22'
owner: rufus
status: in-progress
tracker: beads
workspace: ~/src/life-itself/skills
status_notes:
- "2026-11-22 — Created from Rufus's brief to the library-anki session. Raw brief below; SCQ in progress."
- "2026-11-22 — Skill drafted and tested over two rounds: skills/making-spaced-repetition-cards. Blind judge pass 72–100% against 0–29% for old and no-skill decks. Waiting on Rufus's grading of a 12-card sample (library evals/spaced-repetition-cards/rufus-sample.tsv)."
---

# Spaced-Repetition Cards Skill

## Raw brief (2026-11-22, as given)

A good, reusable skill for making Anki / spaced-repetition cards from texts and books, based on real research and on what the [library repo](https://github.com/life-itself/library) (private) has already done.

- Library already has a book-to-Anki plan ([PLAN.md](https://github.com/life-itself/library/blob/main/PLAN.md), [MOTIVATION.md](https://github.com/life-itself/library/blob/main/MOTIVATION.md) with an SCQH and open questions) and three decks: Wilber *Sex, Ecology, Spirituality* (102 Q&A cards from a chapter digest), Wilber *Integral Psychology* (43 core + 48 extended), Thich Nhat Hanh *Heart of the Buddha's Teaching* (250 cards, verbatim quotes and exact lists, typed tags). None reviewed in real Anki use yet.
- Second user: [Sutras](https://sutras.lifeitself.org), wisdom texts with stable passage ids and notes as data. Its deferred idea `sutras-m2v.11` wants a deck per text beside the EPUB. The skill should serve that case (cards citing passage ids, verbatim quotes) without building the Sutras feature.
- Deliverables: a sourced research note in library `docs/`; the skill `making-spaced-repetition-cards` in this repo (when to use, card types by material, rules for a good card, workflow read → pick → draft → critique → cut, Anki TSV output with tags and a source/passage-id field, .apkg optional, core vs extended size guide, worked example); a test run on one short text with a critique pass; follow-ups in Beads.
- Limits: library is private and copyrighted; only a few short quoted lines may appear in this public repo. No paid services.

## SCQ

Status: draft (from Rufus's message of 2026-11-22; not yet signed off). Rufus asked that planning and evaluation run without needing him at each step.
Source: Rufus's brief to the `library-anki` session, 2026-11-22, plus his card critiques ([library `docs/2026-11-22-wilber-card-critiques.md`](https://github.com/life-itself/library/blob/main/docs/2026-11-22-wilber-card-critiques.md), private). Earlier SCQH for the parent idea: library `MOTIVATION.md` (2026-07-21).

### Situation
**Rufus wants to learn more from what he reads through spaced repetition, and has a first round of AI-made decks.**

- Library has three AI-made decks: Wilber *Sex, Ecology, Spirituality* (102 cards), Wilber *Integral Psychology* (43 core + 48 extended), Thich Nhat Hanh *Heart of the Buddha's Teaching* (250).
- Rufus has now reviewed Wilber cards on his phone in AnkiMobile.
- He wants to produce many more cards, from books and from texts like those on Sutras.
- Research on card writing and on AI-made cards is done: library `docs/2026-11-22-spaced-repetition-cards-research.md`.

### Complication
**The cards are "okay, but not great", and he found them off-putting, so the habit won't stick at scale.**

- Many cards are "mini essay questions": two questions in one, long subtle answers, undefined terms, doubtful claims carded as fact, the same point repeated (four worked examples in the critiques doc).
- No written standard exists for what a good card is, so each AI run fills the gaps its own way.
- Judging quality currently needs Rufus to review cards by hand, which doesn't scale to many more decks.

### Question
How do we make AI-drafted cards from books and texts that Rufus finds good to review, reliably, without him checking each deck?

Criteria:
- General: works for argument books (Wilber), teaching books with lists (Thich Nhat Hanh) and short wisdom texts with passage ids (Sutras).
- Focus on how each card is built; deck size is secondary.
- Quality is judged automatically, against a rubric calibrated on Rufus's critiques, before he sees a deck.
- Packaged as a skill in this repo; no paid services; no book text in this public repo beyond a few short quoted lines.
- Off the table: fixing the existing Wilber decks (examples only); building the Sutras deck feature.

Issue tree:
- What makes a single card good, for each kind of material? — proposed: rules in the research note plus Rufus's fault list
- How does an agent get from a book to the few things worth a card? — proposed: digest first, then a centrality cut
- How do we tell, without Rufus, that a deck is good? — open
  - Does an AI judge, given Rufus's four critiques, agree with him on new cards? — open
- How much of each book should become cards? — open
- What output format lets decks be regenerated without duplicates and traced to the source? — proposed: TSV with GUID and source columns

## Ideas offered (parked)

- More card variety: yes/no, multiple choice, cloze; 15 words is sometimes too aggressive (Rufus, 2026-11-22). Adopted: 15-word target, 25 hard limit; true/false, multiple choice and fill-the-blank allowed up to about a third of a deck.
- Test of a good card: an AI could score the reply against the back clearly, right or wrong or out of 10 (Rufus, 2026-11-22). Adopted as the core rule and the grader test.

- Use Fable subagents to identify the problem, the approach, the build, the test, and the evaluation (Rufus, 2026-11-22).

## Next

Done in the 2026-11-22 session: research, plan (library `docs/plans/2026-11-22-spaced-repetition-skill-plan.md`), skill, calibrated judge, two test rounds (see the skill's `test-log.md`). Open follow-ups are in Beads (search "spaced-repetition").
