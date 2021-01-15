class CFGManager:
    PATH_TO_CFG = "./data/config/"
    GENERAL_SECTION = "GENERAL"

    def __init__(self, main_log, fm):
        from configparser import ConfigParser
        self.main_log = main_log
        self.fm = fm
        self.cfg_main = ConfigParser()

        self.load_config()

    def load_config(self):
        try:
            self.cfg_main.read(self.PATH_TO_CFG + 'main.cfg', encoding='utf-8')  # load config file
            # print(self.cfg_main[self.GENERAL_SECTION])
            self.main_log.write_log("Config has been loaded", self)
        except Exception as e:
            # print(e)
            self.main_log.write_log("Can't read config", self, self.main_log.CANT_LOAD_STATE)
            self.main_log.write_log("Error " + str(e), self, self.main_log.ERROR_STATE)

    def reload_cfg(self):
        self.load_config()

    def read_var_from_cfg(self, word, default):
        # its reading some var from cfg, if while reading have error it will return 'default'
        try:
            self.main_log.write_log(f"Read '{word}' in cfg", self)
            return self.cfg_main[self.GENERAL_SECTION][word]
        except Exception as e:
            self.main_log.write_log(f"Can't read '{word}' from cfg", self, self.main_log.CANT_LOAD_STATE)
            return default

    def write_var_to_cfg(self, word, parameter):
        # set parameter (with name 'word') var 'parameter'
        self.cfg_main.set(self.GENERAL_SECTION, word, parameter)
        with open(self.PATH_TO_CFG + "main.cfg", "w", encoding="utf-8") as a:
            self.cfg_main.write(a)
