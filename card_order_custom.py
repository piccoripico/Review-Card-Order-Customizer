# Modified from Anki's opensourced codes at GitHub

import anki, json, random
from anki.scheduler.v2 import Scheduler
from aqt import mw
from anki.consts import *
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
        orders = ['order1', 'order2', 'order3', 'order4', 'order5']
        labeled_order_by_items = {
            "(None)": "",
            "1)Card ID": "id",
            "2)Note ID": "nid",
            "3)Deck ID": "did",
            "4)Card template order": "ord",
            "5)Card modified timestamp": "mod",
            "6)Card update sequence": "usn",
            "7)Card type": "type",
            "8)Card queue type": "queue",
            "9)Card due date": "due",
            "A)Card interval days": "ivl",
            "B)Card ease factor": "factor",
            "C)Card review times": "reps",
            "D)Card lapse times": "lapses",
            "E)Card remaining steps": "left",
            "F)Card original due date": "odue",
            "G)Deck original ID": "odid",
            "Randomize cards": "random()",
            "1)desc": "id desc",
            "2)desc": "nid desc",
            "3)desc": "did desc",
            "4)desc": "ord desc",
            "5)desc": "mod desc",
            "6)desc": "usn desc",
            "7)desc": "type desc",
            "8)desc": "queue desc",
            "9)desc": "due desc",
            "A)desc": "ivl desc",
            "B)desc": "factor desc",
            "C)desc": "reps desc",
            "D)desc": "lapses desc",
            "E)desc": "left desc",
            "F)desc": "odue desc",
            "G)desc": "odid desc",
        }
        order_values = []
        for order in orders:
            value = config.get(order, "")
            # Lookup the value in the labeled_order_by_items dictionary
            value = labeled_order_by_items.get(value, value)
            if value:
                order_values.append(value)
        order12345 = ', '.join(order_values)

        orderUser = config.get('orderUser', "")

        if order12345:
            order_by = order12345
        elif orderUser:
            order_by = orderUser
        else:
            order_by = "due, random()"

        # queue types: 0=new, 1=(re)lrn, 2=rev, 3=day (re)lrn,
        #   4=preview, -1=suspended, -2=sibling buried, -3=manually buried
        # Addon note: 'order by {order_by}' is replaced from 'order by due, random()'
        self._revQueue = self.col.db.list(
            f"""
select id from cards where
did in %s and queue = {QUEUE_TYPE_REV} and due <= ?
order by {order_by}
limit ?"""
            % self._deck_limit(),
            self.today,
            lim,
        )

        ''' # for debugging at a glance
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