class TranslateManager:
    PATH_TO_TRANSLATE = "./data/translate/"

    def __init__(self, main_log, fm):
        from configparser import ConfigParser
        self.main_log = main_log
        self.fm = fm
        self.trans_main = ConfigParser()
        self.language = {1: "RU", 2: "EN"}
        self.current_lang = 1

    def set_current_language(self, lang):
        self.current_lang = lang

    def load_translate(self):
        try:
            self.trans_main.read(self.PATH_TO_TRANSLATE + "main.phrases.txt", encoding='utf-8')
            self.main_log.write_log("File-translate has been loaded", self)
        except Exception as e:
            self.main_log.write_log("Can't read translate file", self, self.main_log.CANT_LOAD_STATE)
            self.main_log.write_log("Error " + str(e), self, self.main_log.ERROR_STATE)

    def translate(self, word):
        try:
            trans = self.trans_main[self.language[self.current_lang]][word]
            self.main_log.write_log(f"Translated '{word}' into '{trans}'", self)
            return trans
        except Exception as e:
            self.main_log.write_log(f"No such translate '{word}'", self, self.main_log.ERROR_STATE)
            return word

    def get_languages(self):
        return self.language
