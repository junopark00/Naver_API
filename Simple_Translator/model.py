# -*- coding: utf-8 -*-

__author__ = "Juno Park"
__github__ = "https://github.com/junopark00"


import urllib.request
from urllib.error import URLError, HTTPError
import json
from PySide2 import QtWidgets


TRANSLATE_LANGUAGES = {
    "Korean": "ko", "English": "en", "Japanese": "ja", "Chinese Simplified": "zh-CN", "Chinese Traditional": "zh-TW",
    "Vietnamese": "vi", "Thai": "th", "Indonesian": "id", "French": "fr", "Spanish": "es",
    "Russian": "ru", "German": "de", "Italian": "it"
}

DETECT_LANGUAGES = {
    "Korean": "ko", "English": "en", "Japanese": "ja", "Chinese Simplified": "zh-CN", "Chinese Traditional": "zh-TW",
    "Vietnamese": "vi", "Thai": "th", "Indonesian": "id", "French": "fr", "Spanish": "es",
    "Russian": "ru", "German": "de", "Italian": "it", "Portuguese": "pt", "Hindi": "hi"
}

class API:
    def __init__(self) -> None:
        self.__set_api()
        
    def __set_api(self) -> None:
        """
        Set API key and client ID.
        """
        self._client_id = "Your client ID here"
        self._client_secret = "Your client secret here"
        
    def translate(self, source_text: str, source_language="ko", target_language="en") -> str:
        """
        Translate text by Papago API.

        Args:
            source_text (str): original text to translate.
            source_language (str, optional): source language to translate. Defaults to "ko".
            target_language (str, optional): target language to translate. Defaults to "en".

        Returns:
            str: translated text.
        """
        try:
            url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
            encText = urllib.parse.quote(source_text)
            data = "source=%s&target=%s&text=%s" % (source_language, target_language, encText)
            request = urllib.request.Request(url)
            request.add_header("X-NCP-APIGW-API-KEY-ID", self._client_id)
            request.add_header("X-NCP-APIGW-API-KEY", self._client_secret)
            response = urllib.request.urlopen(request, data=data.encode("utf-8"))
            rescode = response.getcode()
            
            if rescode == 200:
                response_body = response.read()
                result_json = json.loads(response_body.decode("utf-8"))
                translated_text = result_json['message']['result']['translatedText']
                return translated_text
            elif rescode == 401:
                self.__error_message("Unauthorized", "Check your API key or client ID.")
                return
            elif rescode == 403:
                self.__error_message("Forbidden", "You don't have permission to access the server.")
                return
        except HTTPError as e:
            pass
        except Exception as e:
            self.__error_message("Error", str(e))
            return
    
    def detect(self, source_text: str) -> str:
        try:
            encQuery = urllib.parse.quote(source_text)
            data = "query=" + encQuery
            url = "https://naveropenapi.apigw.ntruss.com/langs/v1/dect"
            
            request = urllib.request.Request(url)
            request.add_header("X-NCP-APIGW-API-KEY-ID",self._client_id)
            request.add_header("X-NCP-APIGW-API-KEY",self._client_secret)

            response = urllib.request.urlopen(request, data=data.encode("utf-8"))
            rescode = response.getcode()
            
            if not rescode == 200:
                print("Error Code:" + rescode)
                
            response_body = response.read()
            result_json = json.loads(response_body.decode('utf-8'))
            langcode = result_json['langCode']
            if langcode in DETECT_LANGUAGES.values():
                detected_language = self.__get_key_from_value(DETECT_LANGUAGES, langcode)
                return detected_language
            else:
                return None
        except HTTPError as e:
            pass
        except Exception as e:
            self.__error_message("Error", str(e))
            return
        
    def __error_message(self, title, message) -> None:
        QtWidgets.QMessageBox.critical(None, title, message)
    
    @staticmethod
    def __get_key_from_value(dictionary, value):
        for k, v in dictionary.items():
            if v == value:
                return k
        return None

