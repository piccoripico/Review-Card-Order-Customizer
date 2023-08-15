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

### Usage Examples

<table>
<thead>
  <tr>
    <th></th>
    <th>Sort by</th>
    <th>Sort item</th>
    <th>Remarks</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>card creation date</td>
    <td>Card ID</td>
    <td>IDs are the older the smaller.</td>
  </tr>
  <tr>
    <td>2</td>
    <td>interval days (descending)</td>
    <td>Card interval days desc</td>
    <td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>deck name firstly, and note content secondly</td>
    <td>(1st) Deck name<br>(2nd) Note sort field</td>
    <td>This allows management by manually entered serial numbers.</td>
  </tr>
</tbody>
</table>

### Note

When the V2 scheduler is phased out of Anki, this addon will become obsolete. The V3 scheduler has its back-end system written in Rust, making it difficult to perform the same operations as with the V2 scheduler.

### Changelog

2023-07-28
- Added config window (after this addon is updated, please restart Anki.)

2023-07-29
- Changed supported Anki versions to 2.1.50+

2023-08-10
- Changed config window's layout for usability improvement

2023-08-15
- Added 3 sort items: H)Note type name, I)Note sort field, J)Deck name
- Added error handling

### Sort items (For the optional direct input to be used as ORDER BY clause, please use the items in the middle column. For example, 'cards.did, random()')

<table>
<thead>
  <tr>
    <th>Sort Items</th>
    <th>(SQL)</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1)Card ID</td>
    <td>cards.id</td>
    <td>The unique identifier (ID) of the card. (time.localtime(cards.id/1000) =   created timestamp)</td>
  </tr>
  <tr>
    <td>2)Note ID</td>
    <td>cards.nid</td>
    <td>The note ID of the card.</td>
  </tr>
  <tr>
    <td>3)Deck ID</td>
    <td>cards.did</td>
    <td>The ID of the deck the card belongs to.</td>
  </tr>
  <tr>
    <td>4)Card template order</td>
    <td>cards.ord</td>
    <td>The order number of the card's template.</td>
  </tr>
  <tr>
    <td>5)Card modified timestamp</td>
    <td>cards.mod</td>
    <td>The last modification timestamp of the card.</td>
  </tr>
  <tr>
    <td>6)Card update sequence</td>
    <td>cards.usn</td>
    <td>The update sequence number of the card (used for syncing).</td>
  </tr>
  <tr>
    <td>7)Card type</td>
    <td>cards.type</td>
    <td>The type of the card (0 = new, 1 = learning, 2 = review).</td>
  </tr>
  <tr>
    <td>8)Card queue type</td>
    <td>cards.queue</td>
    <td>The type of the card's queue (0 = new, 1 = learning, 2 = review, 3 = day learning, 4 = preview, -1 = suspended, -2 = sibling buried, -3 = manually buried).</td>
  </tr>
  <tr>
    <td>9)Card due date</td>
    <td>cards.due</td>
    <td>The due date of the card. For new cards, it represents the due order. For review cards, it represents the due date.</td>
  </tr>
  <tr>
    <td>A)Card interval days</td>
    <td>cards.ivl</td>
    <td>The current interval (in days) of the card.</td>
  </tr>
  <tr>
    <td>B)Card ease factor</td>
    <td>cards.factor</td>
    <td>The current ease factor of the card.</td>
  </tr>
  <tr>
    <td>C)Card review times</td>
    <td>cards.reps</td>
    <td>The number of reviews of the card.</td>
  </tr>
  <tr>
    <td>D)Card lapse times</td>
    <td>cards.lapses</td>
    <td>The total number of lapses of the card.</td>
  </tr>
  <tr>
    <td>E)Card remaining steps</td>
    <td>cards.left</td>
    <td>The remaining number of learning steps of the card.</td>
  </tr>
  <tr>
    <td>F)Card original due date</td>
    <td>cards.odue</td>
    <td>The original due date (used only in filtered decks).</td>
  </tr>
  <tr>
    <td>G)Deck original ID</td>
    <td>cards.odid</td>
    <td>The original deck ID (used only in filtered decks).</td>
  </tr>
  <tr>
    <td>H)Note type name</td>
    <td>notetypes.name</td>
    <td>The name of the note type the card belongs to.</td>
  </tr>
  <tr>
    <td>I)Note sort field</td>
    <td>notes.sfld</td>
    <td>The content of the note's field that you set to "Sort by this field in the browser".</td>
  </tr>
  <tr>
    <td>J)Deck name</td>
    <td>decks.name</td>
    <td>The name of the deck the card belongs to.</td>
  </tr>
  <tr>
    <td>Randomize cards</td>
    <td>random()</td>
    <td>Randomize the card order.</td>
  </tr>
</tbody>
</table>
