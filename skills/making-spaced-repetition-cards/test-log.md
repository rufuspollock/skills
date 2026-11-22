# Test log

Test decks, texts and scores are in the private library repo, under `evals/spaced-repetition-cards/`.

## 2026-11-22: baseline, two rounds, blind evaluation

**Method.** Fresh Opus subagents got only the skill and a text. Each deck was then:

- checked by the script;
- judged blind, pooled and shuffled with the old library decks and no-skill decks for the same text;
- put through the grader test: a Sonnet "learner" answered every front from memory, and two graders (Opus and Sonnet) scored each reply against the back.

The judge was calibrated first on 34 labelled cards, including Rufus's four critiqued cards. It agreed on 31 of 34 overall and on 11 of 12 held-out cards.

**Round 1** (Wilber *Sex, Ecology, Spirituality* ch. 3; Thich Nhat Hanh *Heart of the Buddha's Teaching* ch. 11; *Faith in Mind*):

| Deck | Cards | Blind judge pass | Median answer words | Both graders sure |
|---|---|---|---|---|
| Wilber ch. 3, old deck | 6 | 0% | 45 | 16% |
| Wilber ch. 3, no skill | 64 | 29% | 24 | 23% |
| Wilber ch. 3, with skill | 36 | 97% | 10 | 52% |
| Thich Nhat Hanh ch. 11, old deck | 19 | 0% | 26 | 68% |
| Thich Nhat Hanh ch. 11, with skill | 72 | 72% | 7 | 62% |
| Faith in Mind, no skill | 47 | 72% | 8 | 55% |
| Faith in Mind, with skill | 28 | 100% | 5 | 75% |

**Changes after round 1:**

- "One right answer" rule: narrow the front until only one fair answer exists.
- Lists of five or more items become one-missing-item cards only.
- Fewer "In Wilber's view" fronts.
- Re-judge rewritten cards once.
- Line cards need a full-line cue.
- Verse examples moved off the Faith in Mind test text.

**Round 2** (new texts: Wilber ch. 4, and Marcus Aurelius *Meditations* Book 2 from Sutras, with passage-id links):

| Deck | Cards | Median answer words | Both graders sure | Graders within 2 points |
|---|---|---|---|---|
| Wilber ch. 4 | 45 | 8 | 75% | 100% |
| Meditations Book 2 | 35 | 8 | 54% (64% on idea cards) | 88% |

Wilber met the 70% bar; Meditations did not. Most of its unsure cards were quote cards, where the learner paraphrased and nothing said whether a paraphrase counts. The rest were one-missing-item cards whose items have no fixed names.

**Changes after round 2:**

- Quote and line cards are graded on wording.
- One-missing-item cards use the text's own short names.
- The judge accepts names-first cards for up to four items.
- True/false cards are balanced and not guessable.
- New rules for the grader threshold, file names and context lines.

A third round, to confirm these fixes on a new text, has not run yet.

**Caveats.**

- The skill's judge rubric also filtered the decks, so the blind-judge pass rate flatters the skill. The grader test is independent of the rubric.
- All drafting was on Opus; Sonnet and Haiku drafters are untested.
- Rufus has not yet graded a sample.
