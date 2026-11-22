# making-spaced-repetition-cards

Turns a book, chapter, article or wisdom text into an Anki deck of short cards with clear answers. Cards are built answer-first. A script and an AI judge check them, and the judge is calibrated against Rufus's critiques of earlier decks. Every card carries a stable id and a source line, so decks can be regenerated without duplicates and traced back to the passage (for example a Sutras passage id).

Example prompt: "Use making-spaced-repetition-cards on chapter 3 of this book; I want the key ideas."

Origin: the [life-itself/library](https://github.com/life-itself/library) book-to-Anki pilot (private repo), Rufus's verdict that its Wilber cards were "mini essay questions rather than good cards", and a research note on card writing (Matuschak, Nielsen, Wozniak, Gwern, Quantum Country, and studies of retrieval practice and AI-made questions). Test status: [test-log.md](test-log.md).
