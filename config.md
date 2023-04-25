## Review Card Order Customizer (V2 Scheduler only)

This addon is designed to sort the order of cards displayed during review sessions.
- Possibly useful when you want to study in a specific sequence.
- Available with V2 Scheduler only <b>(Nothing will happen with V3 Scheduler!)</b>. Please check in advance whether the V3 Scheduler is enabled in Anki's Preferences.
- GitHub: https://github.com/piccoripico/Review-Card-Order-Customizer

### Configuration

To sort cards by their deck ID (ascending), due date (descending) and review times (ascending), you can set it as the following:

    "order_by": "did, due desc, reps"
    
- The "desc" is optional (ascending if skipped).
- Higher priority items come first.
- The Anki's default is "due, random()" for your information.

### List of items

- id: The unique identifier (ID) of the card.
- nid: The note ID of the card.
- did: The ID of the deck the card belongs to.
- ord: The order number of the card's template.
- mod: The last modification timestamp of the card.
- usn: The update sequence number of the card (used for syncing).
- type: The type of the card (0 = new, 1 = learning, 2 = review).
- queue: The type of the card's queue (0 = new, 1 = learning, 2 = review, 3 = day learning, 4 = preview, -1 = suspended, -2 = sibling buried, -3 = manually buried).
- due: The due date of the card. For new cards, it represents the due order. For review cards, it represents the due date.
- ivl: The current interval (in days) of the card.
- factor: The current ease factor of the card.
- reps: The number of reviews of the card.
- lapses: The total number of lapses of the card.
- left: The remaining number of learning steps of the card.
- odue: The original due date (used only in filtered decks).
- odid: The original deck ID (used only in filtered decks).
- random(): Randomize the order.

--- Japanese Translation
- id: カードの一意の識別子 (ID)。
- nid: カードのノートID。
- did: カードが属しているデッキのID。
- ord: カードのテンプレートの順序番号。
- mod: カードの最終更新タイムスタンプ。
- usn: カードの更新シーケンス番号 (同期に使用)。
- type: カードのタイプ (0 = 新規, 1 = 学習中, 2 = 復習)。
- queue: カードのキューのタイプ (0 = 新規, 1 = 学習中, 2 = 復習, 3 = 日付別学習, 4 = プレビュー, -1 = 一時停止, -2 = シブリング埋め, -3 = 手動埋め)。
- due: カードの予定日。新規カードの場合は、予定順。復習カードの場合は、予定日。
- ivl: カードの現在の間隔 (日)。
- factor: カードの現在のイージングファクター。
- reps: カードの復習回数。
- lapses: カードの総ラプス回数。
- left: カードの学習ステップの残り回数。
- odue: オリジナルの予定日（フィルターされたデッキでのみ使用）。
- odid: オリジナルのデッキID（フィルターされたデッキでのみ使用）。
- random(): 順番をランダマイズ。
