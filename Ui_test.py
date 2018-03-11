import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class WSlideBar(QWidget):
    """WSlideBar is a personalized slide bar."""

    w_container = None
    v_layout_container = None
    v_scroll_area = None
    v_layout_preview = None


    def __init__(self):
        """Init UI."""

        super(WSlideBar, self).__init__()
        self.init_ui()

    def init_ui(self):
        """Init all ui object requirements."""


        self.setFixedSize(100,500)

        self.setStyleSheet("""
            background: gray;
        """)

        # Container Widget
        self.w_container = QWidget()
        self.w_container.setFixedWidth(100)

        # Layout of Container Widget
        self.v_layout_container = QVBoxLayout()
        self.v_layout_container.setSpacing(100)

        aux = QWidget()
        aux.setFixedSize(10,10)
        aux.setStyleSheet("""background: red;""")

        aux2 = QWidget()
        aux2.setFixedSize(20, 20)
        aux2.setStyleSheet("""background: blue;""")

        aux3 = QWidget()
        aux3.setFixedSize(15, 15)
        aux3.setStyleSheet("""background: yellow;""")

        aux4 = QWidget()
        aux4.setFixedSize(50,50)
        aux4.setStyleSheet("""background: rgb(0,255,0,30%);""")

        aux5 = QWidget()
        aux5.setFixedSize(40, 40)
        aux5.setStyleSheet("""background: green;""")

        aux6 = QWidget()
        aux6.setFixedSize(40, 40)
        aux6.setStyleSheet("""background: green;""")

        self.v_layout_container.addWidget(aux)
        self.v_layout_container.addWidget(aux2)
        self.v_layout_container.addWidget(aux3)
        self.v_layout_container.addWidget(aux4)
        self.v_layout_container.addWidget(aux5)
        self.v_layout_container.addWidget(aux6)

        self.w_container.setLayout(self.v_layout_container)

        self.v_scroll_area = QScrollArea(self)
        self.v_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.v_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.v_scroll_area.setWidget(self.w_container)

        # Scroll Area Layer add
        self.v_layout_preview = QVBoxLayout()
        self.setLayout(self.v_layout_preview)

        self.v_layout_preview.addWidget(self.v_scroll_area)

def run():
    app = QApplication(sys.argv)
    GUI = WSlideBar()
    GUI.show()
    sys.exit(app.exec_())


run()
