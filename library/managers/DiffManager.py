class DiffManager:
    def __init__(self, main_log, fm):
        self.main_log = main_log
        self.fm = fm
        self.diff = 0

        self.load_diff()

    def set_diff(self, diff):
        self.diff = diff

    def get_diff(self):
        return self.diff

    def add_diff(self, diff):
        self.diff = self.fm.get_function("SimpleFunctionsManager").not_round_round(self.diff+diff, 2, 10)

    def save_diff(self):
        self.fm.get_function('CFGManager').write_var_to_cfg("difficult", str(self.diff))

    def load_diff(self):
        self.diff = int(self.fm.get_function("CFGManager").read_var_from_cfg("difficult", 1))