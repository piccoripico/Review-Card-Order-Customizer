from aqt import mw
from aqt.qt import *

class ConfigUI(QDialog):
    def __init__(self, addon_parent):
        super(ConfigUI, self).__init__(addon_parent)
        
        self.addon_parent = addon_parent
        self.config = self.addon_parent.addonManager.getConfig(__name__)

        self.setWindowTitle("Config")

        # Whole layout & categorical layouts
        self.layout = QVBoxLayout(self)
        self.box12345 = QGroupBox("(1) Select item(s) to sort the order of cards")
        self.layout12345 = QHBoxLayout()
        self.box1 = QGroupBox("1st Priority")
        self.box2 = QGroupBox("2nd Priority")
        self.box3 = QGroupBox("3rd Priority")
        self.box4 = QGroupBox("4th Priority")
        self.box5 = QGroupBox("5th Priority")
        self.boxUser = QGroupBox("(2) Optional: You can directly input your own ORDER BY clause. Please note that this feature is only available when all of the above 5 items are set to (None). See the add-on page for the item list. (No review shown if error.)")
        self.layout1 = QVBoxLayout()
        self.layout2 = QVBoxLayout()
        self.layout3 = QVBoxLayout()
        self.layout4 = QVBoxLayout()
        self.layout5 = QVBoxLayout()
        self.layoutUser = QHBoxLayout()
        self.layoutOKCancel = QHBoxLayout()

        # radiobutton group: order1 to order5
        self.order1_radiobuttons = create_order_radiobuttons(self, self.layout1, 'order1')
        self.order2_radiobuttons = create_order_radiobuttons(self, self.layout2, 'order2')
        self.order3_radiobuttons = create_order_radiobuttons(self, self.layout3, 'order3')
        self.order4_radiobuttons = create_order_radiobuttons(self, self.layout4, 'order4')
        self.order5_radiobuttons = create_order_radiobuttons(self, self.layout5, 'order5')

        # input by user: orderUser
        self.text_input = QLineEdit(self)
        self.text_input.setText(self.config.get('orderUser', ''))
        self.layoutUser.addWidget(self.text_input)

        # OK and Cancel buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.save_config)
        self.button_box.rejected.connect(self.reject)

        # Combine the layouts
        self.box1.setLayout(self.layout1)
        self.box2.setLayout(self.layout2)
        self.box3.setLayout(self.layout3)
        self.box4.setLayout(self.layout4)
        self.box5.setLayout(self.layout5)
        self.layout12345.addWidget(self.box1)
        self.layout12345.addWidget(self.box2)
        self.layout12345.addWidget(self.box3)
        self.layout12345.addWidget(self.box4)
        self.layout12345.addWidget(self.box5)
        self.box12345.setLayout(self.layout12345)

        self.boxUser.setLayout(self.layoutUser)

        self.layoutOKCancel.addWidget(self.button_box)

        self.layout.addWidget(self.box12345)
        self.layout.addWidget(self.boxUser)

        # Create a scroll area and set its properties
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            # Create a widget to hold the entire layout
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)

        # Set the initial size of the dialog
        self.scroll_widget.adjustSize()
        scrollbar_width = self.scroll_area.verticalScrollBar().width()
        initial_width = self.scroll_widget.width() + scrollbar_width  # Add the scrollbar width
        screen_height = QApplication.primaryScreen().geometry().height()
        initial_height = min(initial_width, screen_height * 0.8)  # Set the height to 80% of the screen height or the width, whichever is smaller

        self.resize(initial_width, initial_height)

            # Set the scroll area's widget to the layout widget
        self.scroll_area.setWidget(self.scroll_widget)

            # Create a new main layout and add the scroll area to it
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.scroll_area)
        self.main_layout.addLayout(self.layoutOKCancel)

            # Set the dialog's layout to the main layout
        self.setLayout(self.main_layout)

    def save_config(self):
        for order_radiobuttons, config_key in [(self.order1_radiobuttons, 'order1'),
                                               (self.order2_radiobuttons, 'order2'),
                                               (self.order3_radiobuttons, 'order3'),
                                               (self.order4_radiobuttons, 'order4'),
                                               (self.order5_radiobuttons, 'order5')]:
            for radiobutton in order_radiobuttons:
                if radiobutton.isChecked():
                    self.config[config_key] = radiobutton.text()
                    break

        self.config['orderUser'] = self.text_input.text()
        self.addon_parent.addonManager.writeConfig(__name__, self.config)
        self.accept()

def create_order_radiobuttons(self, layout, config_key):
    radiobuttons = []
    gridLayout = QGridLayout()  # Create a new grid layout
    none_items = [i for i in all_order_by_items if i in order_by_none]
    asc_items = [i for i in all_order_by_items if i in order_by_asc_items]
    desc_items = [i for i in all_order_by_items if i in order_by_desc_items]
    row_offset = 2 if none_items else 0

    for i, order in enumerate(none_items):
        radiobutton = QRadioButton(order)
        radiobutton.setChecked(order in self.config.get(config_key, []))
        gridLayout.addWidget(radiobutton, 0, i)  # Add to top row
        radiobuttons.append(radiobutton)

    if none_items:
        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        hline.setFrameShadow(QFrame.Sunken)
        gridLayout.addWidget(hline, 1, 0, 1, 2)  # Add horizontal line. Span across 2 columns

    for i, order in enumerate(asc_items):
        radiobutton = QRadioButton(order)
        radiobutton.setChecked(order in self.config.get(config_key, []))
        gridLayout.addWidget(radiobutton, i + row_offset, 0)  # Add to rows below none_items and horizontal line, left column
        radiobuttons.append(radiobutton)

    for i, order in enumerate(desc_items):
        radiobutton = QRadioButton(order)
        radiobutton.setChecked(order in self.config.get(config_key, []))
        gridLayout.addWidget(radiobutton, i + row_offset, 1)  # Add to rows below none_items and horizontal line, right column
        radiobuttons.append(radiobutton)

    layout.addLayout(gridLayout)  # Add grid layout to the main layout
    layout.addStretch(1)
    return radiobuttons
    
def open_config_dialog():
    dialog = ConfigUI(mw)
    dialog.exec_()

order_by_asc_items = [
    "1)Card ID",
    "2)Note ID",
    "3)Deck ID",
    "4)Card template order",
    "5)Card modified timestamp",
    "6)Card update sequence",
    "7)Card type",
    "8)Card queue type",
    "9)Card due date",
    "A)Card interval days",
    "B)Card ease factor",
    "C)Card review times",
    "D)Card lapse times",
    "E)Card remaining steps",
    "F)Card original due date",
    "G)Card original deck ID",
    "H)Card flags",
    "K)Note GUID",
    "L)Note model ID",
    "M)Note modified timestamp",
    "N)Note update sequence",
    "O)Note tags",
    "P)Note fields",
    "I)Note sort field",
    "Q)Notetype name",
    "R)Notetype modified timestamp",
    "S)Notetype update sequence",
    "J)Deck name",
    "T)Deck modified timestamp",
    "U)Deck update sequence",
    "V)Template name",
    "W)Template modified timestamp",
    "X)Template update sequence",
    "Randomize cards",
]

order_by_desc_items = [
    "1)desc",
    "2)desc",
    "3)desc",
    "4)desc",
    "5)desc",
    "6)desc",
    "7)desc",
    "8)desc",
    "9)desc",
    "A)desc",
    "B)desc",
    "C)desc",
    "D)desc",
    "E)desc",
    "F)desc",
    "G)desc",
    "H)desc",
    "K)desc",
    "L)desc",
    "M)desc",
    "N)desc",
    "O)desc",
    "P)desc",
    "I)desc",
    "Q)desc",
    "R)desc",
    "S)desc",
    "J)desc",
    "T)desc",
    "U)desc",
    "V)desc",
    "W)desc",
    "X)desc",
]

order_by_none = ["(None)"]

all_order_by_items = order_by_none + order_by_asc_items + order_by_desc_items

mw.addonManager.setConfigAction(__name__, open_config_dialog)