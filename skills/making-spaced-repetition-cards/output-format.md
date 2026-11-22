# Output format

## File

One TSV per tier: `<slug>-core.tsv` and, if needed, `<slug>-extended.tsv`; for a book done part by part, `<slug>-<part>-core.tsv`. UTF-8. Header lines first:

```text
#separator:tab
#html:true
#guid column:1
#tags column:4
#notetype:Basic
#deck:<Deck name, e.g. Faith in Mind>
#columns:GUID	Front	Back	Tags
```

Anki 2.1.54 or later reads these directives. Front and Back map onto the Basic note type, so no setup is needed on desktop or AnkiMobile.

## Columns

- **GUID**: `<slug>:<location>:<claim-key>`, all lowercase, for example `faith-in-mind:3:extinguish-views` or `wilber-ses:ch03:holarchy-vs-dominator`. The location is the passage id when the text has one (Sutras stanza or section ids), otherwise `chNN`. The claim key is two to four words naming the point. Never renumber: keep a card's GUID when you reword it, so re-importing updates the card in place and keeps its review history.
- **Front**: one question, 30 words or fewer.
- **Back**: the answer line first, aiming for 15 words or fewer, with 25 as the hard limit. Then, optionally, `<br><small>` plus one line of context, using only terms the deck has already taught. Then always `<br><small>Source: …</small>`. The source is the title plus chapter, or a link to the passage: `<a href="https://sutras.lifeitself.org/meditations#4.3">Meditations 4.3</a>`.
- **Tags**: space-separated. Use `<slug>::<part>`, where the part is the book's own division (`ch03`, `book2`), or just `<slug>` for a short text, plus exactly one `type::` tag: `concept`, `why`, `contrast`, `list`, `tf` (true/false), `mc` (multiple choice), `cloze` (fill the blank), `quote`, `line` or `reflect`. Readers can suspend a type, such as `reflect` or `line`, in Anki's browser.

## Escaping

No tabs or newlines inside a field; use `<br>` for a line break. Write `&lt;`, `&gt;` and `&amp;` for literal characters. Don't start a field with a straight double quote, or Anki may treat the field as CSV quoting. Use curly quotes “…” for quotations.

## Importing

- **Desktop:** File → Import, choose the file, and check the field mapping and deck. Then Sync to push the deck to AnkiWeb and phones.
- **iPhone, without desktop:** save the file to Files, tap Share, choose Anki, and import.
- **Updating:** re-import the regenerated file. Rows whose GUID already exists update in place, and new GUIDs are added. To delete a card, remove it in Anki; deleting a row doesn't remove it.

## Other routes (only if asked)

- **.apkg:** build it with [genanki](https://github.com/kerrickstaley/genanki), setting `guid=` to the same GUID string. It's useful when publishing a deck for download beside an EPUB.
- **AnkiConnect:** adds cards straight into a running Anki desktop. It suits adding cards one by one while reading.
