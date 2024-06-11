# Simple Translator by Papago

Simple Translator is a lightweight PySide2 app utilizing Naver's Papago Translate API.

## Purpose

The purpose of this project is to provide a simple translation tool where users can input text in various languages and get it translated into their selected language.

## Usage

1. **Language Selection**: Choose the original language of the text to be translated and the target language.
2. **Text Input**: Enter the text to be translated into the text box with the placeholder "Enter text."
3. **Translation**: Click the "Translate" button or wait for 1 second of text input pause for translation to occur.
4. **Language Swap**: Click the "Swap" button to exchange the original and target languages.
5. **Clear Text**: Click the "Clear" button to clear all text.

## Components

This project consists of:

- **model.py**: Contains the `API` class interacting with the Papago API.
- **view.py**: Includes the `SimpleTranslatorUI` class constructing the UI using `PySide2`.
- **controller.py**: Connects the `model` and `view` and handles interactions with the `SimpleTranslatorController` class.

## Requirements

To run this project, you'll need `Python3` and the `PySide2` library. Also, you'll require `client_id` and `client_secret` from Naver's Papago API.

## License

This project is released under the MIT License. For more information, see the [LICENSE](LICENSE) file.
