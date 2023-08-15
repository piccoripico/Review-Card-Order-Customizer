import anki
from aqt import mw
# from aqt.utils import showText
from anki.consts import QUEUE_TYPE_REV

# ERROR_MSG = "[Add-on] Review Card Order Customizer\n\n{}"

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
        # time.localtime(cards.id/1000) = date created
        orders = ['order1', 'order2', 'order3', 'order4', 'order5']
        labeled_order_by_items = {
            "(None)": "",
            "1)Card ID": "cards.id",
            "2)Note ID": "cards.nid",
            "3)Deck ID": "cards.did",
            "4)Card template order": "cards.ord",
            "5)Card modified timestamp": "cards.mod",
            "6)Card update sequence": "cards.usn",
            "7)Card type": "cards.type",
            "8)Card queue type": "cards.queue",
            "9)Card due date": "cards.due",
            "A)Card interval days": "cards.ivl",
            "B)Card ease factor": "cards.factor",
            "C)Card review times": "cards.reps",
            "D)Card lapse times": "cards.lapses",
            "E)Card remaining steps": "cards.left",
            "F)Card original due date": "cards.odue",
            "G)Deck original ID": "cards.odid",
            "H)Note type name": "notetypes.name",
            "I)Note sort field": "notes.sfld",
            "J)Deck name": "decks.name",
            "Randomize cards": "random()",
            "1)desc": "cards.id desc",
            "2)desc": "cards.nid desc",
            "3)desc": "cards.did desc",
            "4)desc": "cards.ord desc",
            "5)desc": "cards.mod desc",
            "6)desc": "cards.usn desc",
            "7)desc": "cards.type desc",
            "8)desc": "cards.queue desc",
            "9)desc": "cards.due desc",
            "A)desc": "cards.ivl desc",
            "B)desc": "cards.factor desc",
            "C)desc": "cards.reps desc",
            "D)desc": "cards.lapses desc",
            "E)desc": "cards.left desc",
            "F)desc": "cards.odue desc",
            "G)desc": "cards.odid desc",
            "H)desc": "notetypes.name desc",
            "I)desc": "notes.sfld desc",
            "J)desc": "decks.name desc",
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
            order_by = "cards.due, random()"  # Anki's default: "due, random()"

        # queue types: 0=new, 1=(re)lrn, 2=rev, 3=day (re)lrn,
        #   4=preview, -1=suspended, -2=sibling buried, -3=manually buried
        # Addon note: 'order by {order_by}' is replaced from 'order by due, random()'
        sql_pre = "select cards.id from cards"
        sql_var = ""
        sql_suf = f" where cards.did in %s and cards.queue = {QUEUE_TYPE_REV} and cards.due <= ? order by {order_by} limit ?"

        if 'decks.name' in order_by:
            sql_var += " join decks on cards.did = decks.id"
        if 'notetypes.name' in order_by or 'notes.sfld' in order_by:
            sql_var += " join notes on cards.nid = notes.id"
        if 'notetypes.name' in order_by:
            sql_var += " join notetypes on notes.mid = notetypes.id"

        sql_query = sql_pre + sql_var + sql_suf

        try:
            self._revQueue = self.col.db.list(
                sql_query
                % self._deck_limit(),
                self.today,
                lim,
            )
        except anki.errors.DBError as e:
            return False
            # showText(ERROR_MSG.format(str(e)))
        except:
            return False
            # custom_error_message = "[Add-on] Review Card Order Customizer: An unexpected error occurred. Continuing with Anki's default order..."
            # showText(ERROR_MSG.format(str(custom_error_message)))

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

'''
### version handling suggested by ChatGPT ###
import anki

# Get the Anki version
anki_version = tuple(int(x) for x in anki.version.split("."))

def _fillRev_v1(...):
    # Implementation for Anki version 1.x
    ...

def _fillRev_v2(...):
    # Implementation for Anki version 2.x
    ...

# Select the appropriate function and use the same name in the global scope
if anki_version[0] == 1:
    _fillRev = _fillRev_v1
elif anki_version[0] == 2:
    _fillRev = _fillRev_v2
else:
    # Unsupported version
    raise NotImplementedError("This Anki version is not supported")

# Assign the selected function to Anki's Scheduler
anki.scheduler.v2.Scheduler._fillRev = _fillRev
'''