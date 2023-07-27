## Review Card Order Customizer (V2 Scheduler only)
### Available on AnkiWeb: https://ankiweb.net/shared/info/81245454

This addon is designed to sort the order of cards displayed during review sessions.

- Possibly useful to study in a specific sequence.
- Please note that this feature is only available with the V2 Scheduler <b>(it will not work with the V3 Scheduler)</b>. Make sure the V3 Scheduler is disabled in Anki's Preferences.
- GitHub: https://github.com/piccoripico/Review-Card-Order-Customizer

### Config

To sort cards by their Deck ID and Note ID, set the configuration as the following image:

<img src="https://github.com/piccoripico/Review-Card-Order-Customizer/raw/main/ConfigWindow.JPG">

- Descending order if the "desc" selected.
- Higher priority items come first.
- The Anki's default is "due, random()" for your information.

### Note

When the V2 scheduler is phased out of Anki, this addon will become obsolete. The V3 scheduler has its back-end system written in Rust, making it difficult to perform the same operations as with the V2 scheduler.

### Changelog

2023/7/28

- Added config window

### Items

- 1)Card ID: id - The unique identifier (ID) of the card.
- 2)Note ID: nid - The note ID of the card.
- 3)Deck ID: did - The ID of the deck the card belongs to.
- 4)Card template order: ord - The order number of the card's template.
- 5)Card modified timestamp: mod - The last modification timestamp of the card.
- 6)Card update sequence: usn - The update sequence number of the card (used for syncing).
- 7)Card type: type - The type of the card (0 = new, 1 = learning, 2 = review).
- 8)Card queue type: queue - The type of the card's queue (0 = new, 1 = learning, 2 = review, 3 = day learning, 4 = preview, -1 = suspended, -2 = sibling buried, -3 = manually buried).
- 9)Card due date: due - The due date of the card. For new cards, it represents the due order. For review cards, it represents the due date.
- A)Card interval days: ivl - The current interval (in days) of the card.
- B)Card ease factor: factor - The current ease factor of the card.
- C)Card review times: reps - The number of reviews of the card.
- D)Card lapse times: lapses - The total number of lapses of the card.
- E)Card remaining steps: left - The remaining number of learning steps of the card.
- F)Card original due date: odue - The original due date (used only in filtered decks).
- G)Deck original ID: odid - The original deck ID (used only in filtered decks).
- Randomize cards: random() - Randomize the card order.
