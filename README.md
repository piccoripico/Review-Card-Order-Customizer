## Review Card Order Customizer (V2 Scheduler only)
> Available on AnkiWeb: <a href="https://ankiweb.net/shared/info/81245454" rel="nofollow">https://ankiweb.net/shared/info/81245454</a>

> GitHub: <a href="https://github.com/piccoripico/Review-Card-Order-Customizer" rel="nofollow">https://github.com/piccoripico/Review-Card-Order-Customizer</a>

This addon is designed to sort the order of cards displayed during review sessions.

- Possibly useful for those who want to learn in a specific sequence.
- Please note that this feature is only available with the V2 Scheduler <b>(it will not work with the V3 Scheduler)</b>. Make sure the V3 Scheduler is disabled in Anki's Preferences.

### Config

- To sort cards by their Deck ID and Card ID for example, set the configuration as the following image: <img src="https://github.com/piccoripico/Review-Card-Order-Customizer/raw/main/ConfigWindow.JPG">
- Descending order if "desc" selected.
- Higher priority item(s) first.
- FYI: The Anki's default is "cards.due, random()".

### Usage Examples

- Example 1: Order by card creation date  
  - Select: Card ID (The older creation the smaller number.)
- Example 2: Completely random order  
  - Select: Randomize cards  
- Example 3: Order by deck name firstly, and note content secondly  
  - Select: (1st) Deck name (2nd) Note sort field (This setting allows management by manually entered serial numbers.)  

### Note

- When the V2 scheduler is phased out of Anki, this addon will become obsolete. The V3 scheduler has its back-end system written in Rust, making it difficult to perform the same operations as with the V2 scheduler.

### Changelog

- 2023-07-28
  - Added config window (after this addon is updated, please restart Anki.)
- 2023-07-29
  - Changed supported Anki versions to 2.1.50+
- 2023-08-10
  - Changed config window's layout for usability improvement
- 2023-08-15
  - Added 3 sort items: Note type name, Note sort field, Deck name
  - Added error handling
- 2023-08-20
  - Added 14 sort items: Card flags, Note GUID, Note model ID, Note modified timestamp, Note update sequence, Note tags, Note fields, Note sort field, Notetype modified timestamp, Notetype update sequence, Deck modified timestamp, Deck update sequence, Template name, Template modified timestamp, Template update sequence
  - (Reference: https://github.com/ankidroid/Anki-Android/wiki/Database-Structure)

### Sort items (For the optional direct input to be used as ORDER BY clause, please use the items in the middle column. For example, 'cards.did, random()')

|         Sort Items                     |      (SQL)                 | Description                                                                                          |
|---------------------------------------|----------------------------|------------------------------------------------------------------------------------------------------|
| 1)Card ID                             | cards.id                   | The unique identifier (ID) of the card. (time.localtime(cards.id/1000) = created timestamp)         |
| 2)Note ID                             | cards.nid                  | The note ID of the card.                                                                             |
| 3)Deck ID                             | cards.did                  | The ID of the deck the card belongs to.                                                              |
| 4)Card template order                 | cards.ord                  | The order of the card template.                                                                      |
| 5)Card modified timestamp             | cards.mod                  | The timestamp of when the card was last modified.                                                    |
| 6)Card update sequence                | cards.usn                  | The update sequence number of the card (used for syncing).                                           |
| 7)Card type                           | cards.type                 | The type of the card (0 = new, 1 = learning, 2 = review, 3 = relearning).                            |
| 8)Card queue type                     | cards.queue                | The queue type of the card (0 = new, 1 = learning, 2 = review, 3 = day learning, 4 = preview,  -1 = suspended, -2 = sibling buried, -3 = manually buried).|
| 9)Card due date                       | cards.due                  | The due date of the card.                                                                            |
| A)Card interval days                  | cards.ivl                  | The interval between card reviews in days (or seconds).                                              |
| B)Card ease factor                    | cards.factor               | The ease factor of the card.                                                                         |
| C)Card review times                   | cards.reps                 | The number of times the card has been reviewed.                                                      |
| D)Card lapse times                    | cards.lapses               | The number of times the card has lapsed (answered correctly to incorrectly).                         |
| E)Card remaining steps                | cards.left                 | The remaining steps for the card in the learning phase.                                              |
| F)Card original due date              | cards.odue                 | The original due date of the card (used only in filtered decks).                                     |
| G)Card original deck ID               | cards.odid                 | The original deck ID of the card (used only in filtered decks).                                      |
| H)Card flags                          | cards.flags                | The flags (red, etc.) associated with the card.                                                      |
| K)Note GUID                           | notes.guid                 | The globally unique ID of the note.                                                                  |
| L)Note model ID                       | notes.mid                  | The model ID of the note.                                                                            |
| M)Note modified timestamp             | notes.mod                  | The timestamp of when the note was last modified.                                                    |
| N)Note update sequence                | notes.usn                  | The update sequence number of the note (used for syncing).                                           |
| O)Note tags                           | notes.tags                 | The tags associated with the note.                                                                   |
| P)Note fields                         | notes.flds                 | The fields of the note.                                                                              |
| I)Note sort field                     | notes.sfld                 | The sort field of the note (you set to "Sort by this field in the browser").                         |
| Q)Notetype name                       | notetypes.name             | The name of the note type.                                                                           |
| R)Notetype modified timestamp         | notetypes.mtime_secs       | The timestamp of when the note type was last modified.                                               |
| S)Notetype update sequence            | notetypes.usn              | The update sequence number of the note type (used for syncing).                                      |
| J)Deck name                           | decks.name                 | The name of the deck.                                                                                |
| T)Deck modified timestamp             | decks.mtime_secs           | The timestamp of when the deck was last modified.                                                    |
| U)Deck update sequence                | decks.usn                  | The update sequence number of the deck.                                                              |
| V)Template name                       | templates.name             | The name of the card template.                                                                       |
| W)Template modified timestamp         | templates.mtime_secs       | The timestamp of when the card template was last modified.                                           |
| X)Template update sequence            | templates.usn              | The update sequence number of the card template (used for syncing).                                  |
| Randomize cards                       | random()                   | Randomize the order of cards.                                                                        |
