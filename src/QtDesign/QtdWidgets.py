from PySide2 import QtCore, QtGui, QtWidgets

import typing


class QCardWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        # Set QPushButton as the container for Card widgets
        self.__button = QtWidgets.QPushButton()

        # Create QGridLayout so QPushButton can be added to QWidget
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.__button)
        layout.setContentsMargins(0, 0, 0, 0)
        super().setLayout(layout)

    def layout(self) -> QtWidgets.QLayout:
        return self.__button.layout()

    def setLayout(self, arg__1: QtWidgets.QLayout) -> None:
        return self.__button.setLayout(arg__1)

    @property
    def clicked(self):
        return self.__button.clicked

class QRichTabBar(QtWidgets.QTabBar):
    def __init__(self, parent):
        super().__init__(parent)

    def setTabText(self, index: int, text: str):
        label = QtWidgets.QLabel(self)
        label.setText(text)
        label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.setTabButton(index, QtWidgets.QTabBar.LeftSide, label)

    def tabText(self, index: int):
        doc = QtGui.QTextDocument()
        doc.setHtml(self.tabButton(index, QtWidgets.QTabBar.LeftSide).text())
        return doc.toPlainText()

class QRichTabWidget(QtWidgets.QTabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self._tabBar = QRichTabBar(self)
        self.setTabBar(self._tabBar)

    @typing.overload
    def addTab(self, widget: QtWidgets.QWidget, arg__2: str) -> int: ...
    @typing.overload
    def addTab(self, widget: QtWidgets.QWidget, icon: QtGui.QIcon, label: str) -> int: ...

    def addTab(self, *args, **kwargs) -> int:
        index = super().addTab(*args, **kwargs)
        self._tabBar.setTabText(index, super().tabText(index))
        super().setTabText(index, "")
        return index

    def setTabText(self, index: int, text: str):
        self._tabBar.setTabText(index, text)

    def tabText(self, index: int):
        return self._tabBar.tabText(index)