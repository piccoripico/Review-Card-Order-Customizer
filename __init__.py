import anki, json, random
from anki.scheduler.v2 import Scheduler
from aqt import mw
from PyQt5.QtWidgets import QMessageBox

def _fillRev(self, recursing: bool = False) -> bool:
    "True if a review card can be fetched."
    if self._revQueue:
        return True
    if not self.revCount:
        return False

    lim = min(self.queueLimit, self._currentRevLimit())
    if lim:
        # Load the add-on config
        config = mw.addonManager.getConfig(__name__)

        # Get the custom order by setting
        order_by = config.get('order_by', 'did, nid')

        # queue types: 0=new, 1=(re)lrn, 2=rev, 3=day (re)lrn,
        #   4=preview, -1=suspended, -2=sibling buried, -3=manually buried
        # 'queue = 2' is replaced from 'queue = {QUEUE_TYPE_REV}'
        # 'order by {order_by}' is replaced from 'order by due, random()'
        self._revQueue = self.col.db.list(
            f"""
select id from cards where
did in %s and queue = 2 and due <= ?
order by {order_by}
limit ?"""
            % self._deck_limit(),
            self.today,
            lim,
        )

        '''
        debug_info = "Deck limit: " + str(self._deck_limit()) + "\nRevQueue: " + str(self._revQueue)
        for card_id in self._revQueue:
            card = self.col.getCard(card_id)
            debug_info += f"\nCardID: {card_id}, DeckID: {card.did}, NoteID: {card.nid}"

        msg_box = QMessageBox()
        msg_box.setText(debug_info)
        msg_box.exec()
        '''

        if self._revQueue:
            # preserve order
            self._revQueue.reverse()
            return True

    if recursing:
        return False
    self._reset_counts()
    self._resetRev()
    return self._fillRev(recursing=True)

anki.scheduler.v2.Scheduler._fillRev = _fillRev