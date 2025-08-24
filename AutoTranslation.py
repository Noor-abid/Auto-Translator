from translate import Translator

def translate_text(text, source_lang="en", target_lang="ur"):
    """
    Translates text using the 'translate' library.
    - text: input string
    - source_lang: source language code (default = 'en')
    - target_lang: target language code (default = 'ur')
    """
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    return translator.translate(text)


if __name__ == "__main__":
    text = "This is a useful library!"
    translated_text = translate_text(text, source_lang="en", target_lang="es")

    print("Original:", text)
    print("Translated:", translated_text)
