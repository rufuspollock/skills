---
name: marketing-strategy
description: Use when asked for a marketing strategy, "lightweight marketing strategy", campaign or launch plan, promotion or go-to-market plan, or a marketing or press pack, for a product, report, course, event, site or initiative; also when a launch keeps slipping or the drafts exist but nothing has been posted.
license: Proprietary
metadata:
  author: rgrp
  status: draft
  origin: tao.rufuspollock.com "Marketing Strategy Structure"; life-itself/courses explorer/marketing (Apr 2026); comparison with Haines marketingskills and Anthropic campaign-plan (life-itself/marketing docs/research/2026-11-19-marketing-skills.md)
---

# Marketing strategy

A campaign strategy is short and time-boxed. It follows Rufus's [Marketing Strategy Structure](https://tao.rufuspollock.com/Marketing+Strategy+Structure.md). Worked examples: [Explorer](https://github.com/life-itself/courses/tree/main/explorer/marketing) (strategy and pack); Reports that Matter launch, `reportsthatmatter/marketing` `projects/2611-launch/` (full build).

## What to make

Build in layers. Each layer is optional beyond the first; say which ones you are making and why.

1. **`strategy.md` (always).** From [strategy-template.md](strategy-template.md).
2. **`pack.md` (optional).** Reusable copy others can lift: one-liner, blurbs at set lengths, per-audience versions, hooks, press block. Make it when other people (editors, partners, collaborators) will write about the thing, or when many posts draw on the same copy. From [pack-template.md](pack-template.md).
3. **`runbook.md` and other materials (optional, full build).** The runbook is "do this, now": for each action, in date order, the exact text to paste, which image (with a download link), where the link goes (post, first comment, first reply), when, and who, as numbered steps anyone (or an agent) could follow without asking. From [runbook-template.md](runbook-template.md). Other materials: composed images, a public press-kit page, email drafts. Make these when the launch is big enough that the person posting shouldn't have to assemble anything.

The pack is for others to reuse; the runbook is for us to execute. Keep them separate.

## Process

1. **Bring rough context first.** Collect what exists before asking anything:
   - the offer
   - the dates
   - what has been done, what is in flight and what is stuck
   - the owned lists and accounts, with sizes
   - past campaigns and how they did
   - the initiative's standing brief, if it has one (e.g. `docs/marketing-foundation.md`); read it rather than restating it

   Then refine through a few questions. Don't arrive with a finished answer.
2. **Write `strategy.md`** from [strategy-template.md](strategy-template.md). Goals go near the top and must have a number and a date.
3. **Find the channels.** **REQUIRED SUB-SKILL:** use `finding-channels`. Its tables go in the appendix and its shortlist goes in the channels section.
4. **Write the optional layers** you chose (see "What to make"): the pack, then the runbook and materials.
5. **Critique.** Run two subagents in parallel:
   - a skeptical strategist: is the audience narrow enough, are the channels real and doable in the stated budget?
   - a member of the primary audience, reacting to the pack: would I click, share, sign up? Finish the sentence "I'd ignore this because…".

   Revise.
6. **Readiness gate before setting a date.** Is the offer simple (one job), lovable (someone would choose it) and complete (no visible stubs)? Then cut to what can ship without the open decisions, and set the date. A launch that has slipped twice is too big, so cut it further.
7. **Plan and log.**
   - Add a dated calendar of which piece goes to which channel on which day, with an owner for each.
   - Put tasks in the repo's tracker (Beads), not in Markdown.
   - Log each post where the repo logs activity.
8. **Results when it ends.** Fill in the Results section: the outcome against the goal, what each channel produced, and what we learned. Record these, not impressions.

Put the files in the initiative's marketing folder: as a project (`projects/<slug>.md` plus a same-named directory) where the repo uses projects, else `marketing/<campaign>/` with a short README of key links and the status of each asset.

## Common mistakes

- **Goals without a number or a date**, or placed at the bottom. Goals are one objective (a sentence or two) plus 3–5 key results that are **outcomes** (readers, pick-up, newsletters that run it), not outputs (posts made, notes sent). Counting notes go below the list.
- **Audiences picked from the channels you have.** Find who gets real use from the thing first, as named groups (never "the curious public"); then the channels that reach them.
- **Channels listed as platforms.** Use `finding-channels`.
- **One message for every audience.** Each audience gets its own hook, value proposition and channels.
- **The budget left unstated.** Time is the real budget. Plans that need more hours than exist don't run.
- **The plan grows instead of the posting.** More research and drafts aren't progress if nothing is posted.
- **No Results section.** If it's missing, the next campaign starts from zero.
- **AI-ish copy.** Long leads, needless counts and lists ("24 of the big ones, UK and US, 1986 to 2026"), hedging. Lead short; let one piece of evidence do the work; quotes keep their context (who, when, where).
- **A runbook that says "post the LinkedIn thing".** Name the exact text, the exact image and where the link goes.
