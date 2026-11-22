# Judge prompt

Give this file, the deck TSV and the digest (or source text) to a fresh subagent. Use a different model from the drafter if you can. It returns a verdict per card. Fix or cut every FAIL.

---

You are judging Anki cards for a reader who wants **short, simple cards with clear questions and answers**: an AI should be able to score his reply against the back as right or wrong, or out of 10, without doubt. He rejected earlier decks as "mini essay questions rather than good cards". Be strict: when in doubt, FAIL. A deck of 30 sharp cards beats 60 passable ones.

First read the four rejected cards and their rewrites in `card-patterns.md` (section "Four rejected cards"). They are the standard: anything like the originals fails, and anything like the rewrites passes.

Read the cards in order; a card may rely on terms taught by earlier cards. For each card, check:

- **J1 One thing.** It asks exactly one question with one answer.
- **J2 Gradable.** Run the grader test. Write three replies a reader might give: a right one in different words, a near miss, and a wrong one. Score each 0 to 10 against the back. The card passes if you are sure of each score: the right reply gets 8 or more, the wrong one 2 or less, and the back settles how much the near miss is worth. FAIL with "answer unclear" if the back leaves the near miss open to argument, or if another reply would be just as fair as the back.
- **J3 Known terms.** Every term on the front is everyday, defined on the card, or taught by an earlier card.
- **J4 Worth it.** The point is central to the text (it's in the digest) and worth remembering in a year. Side points and trivia fail.
- **J5 Fair.** A contestable claim is framed as the author's. A claim you think is wrong or unsupported fails. Don't fail a card just because it lacks the author's name when the claim is plain exposition of the text.
- **J6 Not a repeat.** No earlier card tests the same point. One-missing-item cards on the same list, and a line card beside an idea card on the same passage, are not repeats.
- **J6b Connected (deck-level).** The deck has some cards that ask how claims connect: what problem a claim answers, or what follows from it. If there are none, say so in the deck verdict.
- **J7 Not leaky.** The front doesn't contain or give away the answer.
- **J8 Glad to see it.** Would the reader be glad, not weary, to see this card in review? It should be short, clear and interesting.

Output a table with one row per card: GUID, PASS or FAIL, the three grader-test scores, the failed checks (e.g. J2, J4), and a fix of 12 words or fewer ("split: …", "drop", "define X on front", "frame as Wilber's"). Then a deck verdict: how many cards pass, which key ideas in the digest have no card, and whether any one idea is over-carded.

Reflection cards (`type::reflect`) are judged only on J1, J3 and J8.

The skill's own rules apply. A names-first card for a structure of up to four items, whose answer is just the names, is not "a list asked whole". A true/false card fails J7 if its wording makes the verdict obvious.

## Testing a deck end to end (optional)

Use this for a new kind of text, or before publishing a deck to others. It needs no human.

1. **Learner.** A fresh subagent that hasn't read the text answers every front from memory, in 25 words or fewer, saying "don't know" where true.
2. **Two graders.** Two fresh subagents on different models each score every reply 0 to 10 against the back (quote and line cards on wording: a paraphrase is wrong), and mark each score "sure" or "unsure" ("unsure" means careful graders could differ by 3 points or more).
3. **Read the result.** Clear decks have both graders sure on at least 70% of non-reflection cards. Look at the cards where either grader was unsure: they usually have several fair answers or a thin cue. Rewrite or cut them.
