# -*- coding: utf-8 -*-

__author__ = "Juno Park"
__github__ = "https://github.com/junopark00"


import os
from PySide2 import QtWidgets, QtGui, QtCore
import qdarktheme
from model import TRANSLATE_LANGUAGES


class TranslatorView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.__initUI()
        self.__center_on_screen()
        self.__apply_styles()

    def __initUI(self) -> None:
        """
        Initialize UI.
        """
        self.setWindowTitle("Simple Translator by Papago")
        
        _vbox_main = QtWidgets.QVBoxLayout()
        _hbox_combo = QtWidgets.QHBoxLayout()
        _hbox_text = QtWidgets.QHBoxLayout()
        _hbox_button = QtWidgets.QHBoxLayout()
        
        self._combo_source = QtWidgets.QComboBox(self)
        self._combo_source.addItems(TRANSLATE_LANGUAGES.keys())
        self._combo_source.setCurrentText("Korean")
        self._combo_source.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        
        self._btn_swap = QtWidgets.QPushButton("", self)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon = os.path.join(current_dir, "resource", "change_white.png")
        if os.path.exists(icon):
            self._btn_swap.setIcon(QtGui.QIcon(icon))
        
        self._combo_translated = QtWidgets.QComboBox(self)
        self._combo_translated.addItems(TRANSLATE_LANGUAGES.keys())
        self._combo_translated.setCurrentText("English")
        self._combo_translated.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        
        self._source_text = QtWidgets.QTextEdit(self)
        self._source_text.setFixedSize(350, 250)
        self._source_text.setPlaceholderText("Enter text")

        self._translated_text = QtWidgets.QTextBrowser(self)
        self._translated_text.setFixedSize(350, 250)
        self._translated_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self._translated_text.setPlaceholderText("Translation")
        
        self._spacer = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self._btn_translate = QtWidgets.QPushButton("Translate", self)
        self._btn_clear = QtWidgets.QPushButton("Clear", self)
        
        _hbox_combo.addWidget(self._combo_source)
        _hbox_combo.addWidget(self._btn_swap)
        _hbox_combo.addWidget(self._combo_translated)
        
        _hbox_text.addWidget(self._source_text)
        _hbox_text.addWidget(self._translated_text)
        
        _hbox_button.addItem(self._spacer)
        _hbox_button.addWidget(self._btn_translate)
        _hbox_button.addWidget(self._btn_clear)
        
        _vbox_main.addLayout(_hbox_combo)
        _vbox_main.addLayout(_hbox_text)
        _vbox_main.addLayout(_hbox_button)
        
        self.setLayout(_vbox_main)
        
        self._combo_translated.setCurrentIndex(1)
        
    def __center_on_screen(self) -> None:
        """
        Set window on the center of the screen.
        """
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)
        
    def __apply_styles(self) -> None:
        """
        Apply styles to the widgets.
        """
        qdarktheme.setup_theme()
        self.setStyleSheet("""
            QTextEdit {
                font-size: 20pt;
                font-family: Arial;
                font-style: normal;
            }
            QTextEdit:placeholder {
                color: grey;
                font-size: 20pt; /* Change font size for placeholder text */
                font-style: italic; /* Change font style for placeholder text */
            }
            QComboBox {
                font-size: 12pt;
                font-family: Arial;
            }
        """)

