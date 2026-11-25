---
name: making-spaced-repetition-cards
description: Use when making Anki or other spaced-repetition flashcards from a book, chapter, article, essay, poem or wisdom text, or when asked to "make cards", "Anki this", "turn this book into flashcards", build a deck per text (e.g. for Sutras), or improve a deck whose cards feel long, vague or off-putting. Not for quizzes or exams meant to grade other people.
license: MIT
metadata:
  author: rgrp
  status: draft
  origin: life-itself/library research note and Rufus's critiques of the Wilber decks (2026-11-22)
---

# Making spaced-repetition cards

A good card is a short question with one clear answer. **The test: an AI grader, given the card's back and someone's reply, could score the reply right or wrong (or out of 10) without doubt.** The rules stop the failure Rufus found in the first AI decks: "mini essay questions rather than good cards".

## Rules

1. **Answer first, and clear.** Write the answer before the question, as short as the answer allows: one word is often best. There is no fixed limit. A long answer is a warning sign: if it holds more than one idea, it's several cards, or none. Ungraded context can go on a small second line.
2. **One thing, one right answer.** One short question. No "X, and why?" If another fair answer exists, narrow the front by naming the test, example or contrast you mean. "Why does Wilber rank life above matter?" has many fair answers. "What test does Wilber use to rank life above matter?" has one.
3. **Every term is known.** A term on the front is everyday, defined on the card, or taught by an earlier card in this deck or in an earlier chapter's deck. Definitions come first; extended cards may rely on core.
4. **Only what matters.** Card a claim only if it is in the digest and worth knowing in a year. Ask the main point simply; skip subtle side points.
5. **Fair to the author.** The deck name already says whose book it is, so most fronts don't name the author. Name the author only where a claim is contestable. Drop claims you think are weak.
6. **Angles, not repeats.** Give each key claim two or three cards from different angles (what, why, contrast, example, and how it connects to the next claim). Never two cards with the same answer in this deck or another in the repo, except line cards beside idea cards and one-missing-item drills.
7. **Names first, then parts.** For up to four items, ask for the names first ("What are the four quadrants?"), then give one card per part. For five or more, skip the whole-list card. Write one-missing-item cards, each missing a different item and using the text's own short name for it, plus a card per item that matters.
8. **Don't leak.** The front must not contain the answer, or an analogy that gives it away. Line and quote cards are exempt, since they show the lead-in on purpose. Cue on content, never on stanza or chapter numbers.
9. **Quotes are exact.** Quoted text and line answers are checked word for word against the source. Paraphrase never goes in quotation marks. These cards are graded on wording, so a paraphrase is wrong; a slip of one small word is fine.
10. **Mostly open questions, with some variety.** Open recall is the default; it is strongest for learning. In argument books, at least a third of the deck's idea cards (core and extended together) ask why, how or what the difference is. Up to about a third of a deck can be true/false (the reader also gives the reason), multiple choice between real look-alikes, or fill the blank. Use these where they make the answer clearest.

Card shapes, verse, quotes, reflection prompts, and four rejected cards rewritten: [card-patterns.md](card-patterns.md). Read it before drafting.

## Workflow

1. **Scope.** Settle the reader's goal: the ideas, the wording, or both. Name the deck `Author – Title`, or the text's title for Sutras. Look for existing decks on the same author in the repo (for example `books/*/anki/`) so you don't repeat them.
2. **Digest.** For each chapter, write about a page listing the claims that carry the argument, in your own words. Mark the contestable ones. Cards come only from the digest.
3. **Draft.** Draft answer-first, two or three cards per claim, in dependency order. Give each card a GUID from [output-format.md](output-format.md).
4. **Check by script.** Fix every ERROR and look at each WARN:

   ```bash
   python3 check_deck.py deck-core.tsv --source chapter.md
   ```

5. **Judge.** Give a fresh subagent [judge.md](judge.md), [card-patterns.md](card-patterns.md), the deck and the digest. Use a different model from the drafter if you can. It runs the rubric and the grader test. Rewrite failed cards on central claims and cut the rest. Send the rewrites to the judge once more, and cut any that fail again. Don't argue cards back in.
6. **Split and note.** The core file holds the best card per key claim, usually 5 to 20 per chapter. Other angles go in the extended file. A short poem or text gets 10 to 20 core cards, plus line cards if it's being memorised. Write `NOTES.md` covering the goal, the counts, what was left out, and the checker and judge results.

## Common mistakes

- Compressing a digest paragraph into one card. That's where mini essays come from.
- Carding everything in the digest. Choosing what to card is half the work.
