from typing import Optional, overload
from PySide2.QtCore import Qt
from PySide2.QtGui import QTextDocument
from PySide2.QtWidgets import QGridLayout, QLabel, QLayout, QPushButton, QTabBar, QTabWidget, QWidget


class QCardWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        # Create QGridLayout as the layout manager for all Card widgets
        self.__layout = QGridLayout()
        self.__layout.setSizeConstraint(QLayout.SetMinimumSize)

        # Set QPushButton as the container for Card widgets
        self.__button = QPushButton()
        self.__button.setLayout(self.__layout)

        # Create QGridLayout so QPushButton can be added to QWidget
        layout = QGridLayout()
        layout.addWidget(self.__button)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    @overload
    def addWidget(self, arg__1: QWidget, row: int, column: int, rowSpan: int, columnSpan: int, alignment: Optional[Qt.Alignment]) -> None: ...
    @overload
    def addWidget(self, arg__1: QWidget, row: int, column: int, alignment: Optional[Qt.Alignment]) -> None: ...
    @overload
    def addWidget(self, w: QWidget) -> None: ...
    
    def addWidget(self, *args, **kwargs) -> None:
        widget: QWidget = args[0] if len(args) > 0 else kwargs.get("arg__1", kwargs["w"])
        row: Optional[int] = args[1] if len(args) > 1 else kwargs.get("row", None)
        column: Optional[int] = args[2] if len(args) > 2 else kwargs.get("column", None)
        rowSpan: Optional[int] = args[3] if len(args) > 3 else kwargs.get("rowSpan", None)
        columnSpan: Optional[int] = args[4] if len(args) > 4 else kwargs.get("columnSpan", None)
        alignment: Optional[Qt.Alignment] = args[5] if len(args) > 5 else kwargs.get("alignment", None)

        if not None in [row, column, rowSpan, columnSpan, alignment]:
            self.__layout.addWidget(widget, row, column, rowSpan, columnSpan, alignment)
        elif not None in [row, column, rowSpan, columnSpan]:
            self.__layout.addWidget(widget, row, column, rowSpan, columnSpan)
        elif not None in [row, column, alignment]:
            self.__layout.addWidget(widget, row, column, alignment)
        elif not None in [row, column]:
            self.__layout.addWidget(widget, row, column)
        else:
            self.__layout.addWidget(widget)

    def layout(self) -> QLayout:
        return self.__layout

    @property
    def clicked(self):
        return self.__button.clicked

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