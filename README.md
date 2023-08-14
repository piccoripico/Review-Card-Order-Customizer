## Review Card Order Customizer (V2 Scheduler only)
### Available on AnkiWeb: https://ankiweb.net/shared/info/81245454

This addon is designed to sort the order of cards displayed during review sessions.

- Possibly useful for those who want to learn in a specific sequence.
- Please note that this feature is only available with the V2 Scheduler <b>(it will not work with the V3 Scheduler)</b>. Make sure the V3 Scheduler is disabled in Anki's Preferences.
- GitHub: https://github.com/piccoripico/Review-Card-Order-Customizer

### Config

To sort cards by their Deck ID and Card ID for example, set the configuration as the following image:

<img src="https://github.com/piccoripico/Review-Card-Order-Customizer/raw/main/ConfigWindow.JPG">

- Descending order if "desc" selected.
- Higher priority item(s) first.
- FIY: The Anki's default is "cards.due, random()".

### Note

When the V2 scheduler is phased out of Anki, this addon will become obsolete. The V3 scheduler has its back-end system written in Rust, making it difficult to perform the same operations as with the V2 scheduler.

### Changelog

2023-07-28
- Added config window (after this addon is updated, please restart Anki.)

2023-07-29
- Changed supported Anki versions to 2.1.50+

2023-08-10
- Changed config window's layout for usability improvement

2023-08-14
- Added 3 sort items: H)Note type name, I)Note sort field, J)Deck name

### Sort items (For the optional direct input to be used as ORDER BY clause, please use the items in the middle column. For example, 'cards.did, random()')

| Sort Items | (SQL) | Description |
|---|---|---|
| 1)Card ID | cards.id | The unique identifier (ID) of the card. (time.localtime(cards.id/1000) =   created timestamp) |
| 2)Note ID | cards.nid | The note ID of the card. |
| 3)Deck ID | cards.did | The ID of the deck the card belongs to. |
| 4)Card template order | cards.ord | The order number of the card's template. |
| 5)Card modified timestamp | cards.mod | The last modification timestamp of the card. |
| 6)Card update sequence | cards.usn | The update sequence number of the card (used for syncing). |
| 7)Card type | cards.type | The type of the card (0 = new, 1 = learning, 2 = review). |
| 8)Card queue type | cards.queue | The type of the card's queue (0 = new, 1 = learning, 2 = review, 3 = day   learning, 4 = preview, -1 = suspended, -2 = sibling buried, -3 = manually   buried). |
| 9)Card due date | cards.due | The due date of the card. For new cards, it represents the due order. For   review cards, it represents the due date. |
| A)Card interval days | cards.ivl | The current interval (in days) of the card. |
| B)Card ease factor | cards.factor | The current ease factor of the card. |
| C)Card review times | cards.reps | The number of reviews of the card. |
| D)Card lapse times | cards.lapses | The total number of lapses of the card. |
| E)Card remaining steps | cards.left | The remaining number of learning steps of the card. |
| F)Card original due date | cards.odue | The original due date (used only in filtered decks). |
| G)Deck original ID | cards.odid | The original deck ID (used only in filtered decks). |
| H)Note type name | notetypes.name | The name of the note type the card belongs to. |
| I)Note sort field | notes.sfld | The content of the note's field that you set to "Sort by this field   in the browser". |
| J)Deck name | decks.name | The name of the deck the card belongs to. |
| Randomize cards | random() | Randomize the card order. |
