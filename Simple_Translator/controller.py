# -*- coding: utf-8 -*-

__author__ = "Juno Park"
__github__ = "https://github.com/junopark00"


import sys
from PySide2 import QtWidgets, QtCore
from model import API, TRANSLATE_LANGUAGES, DETECT_LANGUAGES
from view import TranslatorView


class SimpleTranslator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.__vars()
        self.view = TranslatorView()
        self.__set_timer()
        self.__connections()
        
    def __vars(self) -> None:
        """
        Set variables.
        """
        self._api = API()

    def __set_timer(self) -> None:
        """
        Set timer for textChanged event.
        """
        self._timer = QtCore.QTimer(self)
        self._timer.setSingleShot(True)

    def __connections(self) -> None:
        """
        Connect signals and slots.
        """
        self.view._btn_translate.clicked.connect(self.__translate)
        self.view._btn_clear.clicked.connect(self.__clear)
        self.view._btn_swap.clicked.connect(self.__swap_language)
        self.view._source_text.textChanged.connect(self.__start_timer)
        self.view._combo_source.currentIndexChanged.connect(self.__translate)
        self.view._combo_translated.currentIndexChanged.connect(self.__translate)
        self._timer.timeout.connect(self.__detect)
        
    def __start_timer(self) -> None:
        """
        Start timer for textChanged event.
        """
        self._timer.start(1000)
        
    def __detect(self) -> None:
        """
        Detect language from source text.
        """
        source_text = self.view._source_text.toPlainText()
        detected_language = self._api.detect(source_text)
        if detected_language:
            if detected_language != "Korean":
                self.view._combo_translated.setCurrentText("Korean")
                self.view._combo_source.setCurrentText(detected_language)
            else:
                self.view._combo_source.setCurrentText("Korean")
                self.view._combo_translated.setCurrentText("English")
        else:
            pass
        
        self.__translate()
        
    def __translate(self) -> None:
        """
        Start translation.
        """
        source_text = self.view._source_text.toPlainText()
        if not source_text:
            return
        source_language = TRANSLATE_LANGUAGES.get(self.view._combo_source.currentText())
        target_language = TRANSLATE_LANGUAGES.get(self.view._combo_translated.currentText())
        
        if source_language == target_language:
            self.view._translated_text.setText(source_text)
        
        translated_text = self._api.translate(
            source_text, source_language, target_language
            )
        
        self.view._translated_text.setText(translated_text)
        
    def __clear(self) -> None:
        """
        Clear texts.
        """
        self.view._source_text.clear()
        self.view._translated_text.clear()
        
    def __swap_language(self) -> None:
        """
        Swap languages.
        """
        # Stop timer
        self.view._source_text.blockSignals(True)
        self.view._translated_text.blockSignals(True)
        self.view._combo_source.blockSignals(True)
        self.view._combo_translated.blockSignals(True)
        self._timer.stop()
        
        source_index = self.view._combo_source.currentIndex()
        translated_index = self.view._combo_translated.currentIndex()
        
        source_text_box = list(self.view._source_text.toPlainText())
        translated_text_box = list(self.view._translated_text.toPlainText())
        
        self.view._combo_source.setCurrentIndex(translated_index)
        self.view._source_text.setText("".join(translated_text_box))
        self.view._combo_translated.setCurrentIndex(source_index)
        self.view._translated_text.setText("".join(source_text_box))
        
        # Restart timer
        self.view._source_text.blockSignals(False)
        self.view._translated_text.blockSignals(False)
        self.view._combo_source.blockSignals(False)
        self.view._combo_translated.blockSignals(False)
        self._timer.start(700)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = SimpleTranslator()
    controller.view.show()
    sys.exit(app.exec_())

