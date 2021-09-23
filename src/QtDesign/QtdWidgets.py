from typing import Optional, overload
from PySide2.QtCore import Qt
from PySide2.QtGui import QTextDocument
from PySide2.QtWidgets import QGridLayout, QLabel, QPushButton, QTabBar, QTabWidget, QWidget


class QCardWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        # Create QGridLayout as the layout manager for all Card widgets
        self.cardLayout = QGridLayout()

        # Set QPushButton as the container for Card widgets
        self.centralContainer = QPushButton()
        self.centralContainer.setLayout(self.cardLayout)

        # Create QGridLayout so QPushButton can be added to QWidget
        self.centralLayout = QGridLayout()
        self.centralLayout.addWidget(self.centralContainer)
        self.setLayout(self.centralLayout)

        # Make QPushButton fill QGridLayout
        self.centralLayout.setContentsMargins(0, 0, 0, 0)

    @overload
    def addWidget(self, arg__1: QWidget, row: int, column: int, rowSpan: int, columnSpan: int, alignment: Optional[Qt.Alignment]) -> None: ...
    @overload
    def addWidget(self, arg__1: QWidget, row: int, column: int, alignment: Optional[Qt.Alignment]) -> None: ...
    @overload
    def addWidget(self, w: QWidget) -> None: ...
    
    def addWidget(self, *args, **kwargs) -> None:
        widget      = args[0] if len(args) > 0 else kwargs.get("arg__1", kwargs["w"])
        row         = args[1] if len(args) > 1 else kwargs.get("row", None)
        column      = args[2] if len(args) > 2 else kwargs.get("column", None)
        rowSpan     = args[3] if len(args) > 3 else kwargs.get("rowSpan", None)
        columnSpan  = args[4] if len(args) > 4 else kwargs.get("columnSpan", None)
        alignment   = args[5] if len(args) > 5 else kwargs.get("alignment", None)

        widget.setParent(self.centralContainer)

        if not None in [row, column, rowSpan, columnSpan, alignment]:
            self.cardLayout.addWidget(widget, row, column, rowSpan, columnSpan, alignment)
        elif not None in [row, column, rowSpan, columnSpan]:
            self.cardLayout.addWidget(widget, row, column, rowSpan, columnSpan)
        elif not None in [row, column, alignment]:
            self.cardLayout.addWidget(widget, row, column, alignment)
        elif not None in [row, column]:
            self.cardLayout.addWidget(widget, row, column)
        else:
            self.cardLayout.addWidget(widget)

        self.centralContainer.setMinimumSize(self.cardLayout.sizeHint())

    @property
    def clicked(self):
        return self.centralContainer.clicked

class QRichTabBar(QTabBar):
    def __init__(self, parent):
        super().__init__(parent)

    def tabLabelText(self, index: int):
        doc = QTextDocument()
        doc.setHtml(self.tabButton(index, QTabBar.LeftSide).text())
        return doc.toPlainText()

    def setTabLabelText(self, index: int, text: str):
        label = QLabel(self)
        label.setText(text)
        label.setAttribute(Qt.WA_TranslucentBackground)
        label.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.setTabButton(index, QTabBar.LeftSide, label)

class QRichTabWidget(QTabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.tab = QRichTabBar(self)
        self.setTabBar(self.tab)

    def tabLabelText(self, index: int):
        return self.tab.tabLabelText(index)

    def setTabLabelText(self, index: int, text: str):
        self.tab.setTabLabelText(index, text)