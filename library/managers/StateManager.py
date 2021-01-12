class StateManager:
    def __init__(self, main_log, fm):
        self.current_state = 0
        self.fm = fm
        self.main_log = main_log
        self.status = list()
        main_log.write_log("Its loaded", self)

    def add_state(self, state):
        self.status.append(state)
        self.fm.get_main_log().write_log(f"state added '{state}'", self)

    def set_state(self, num_state):
        self.status[self.current_state].stop_state()
        self.current_state = num_state
        self.status[self.current_state].start_state()
        self.fm.get_main_log().write_log(f"state setted with num '{num_state}'", self)

    def get_state(self, num_state):
        return self.status[num_state]

    def get_current_state(self):
        return self.current_state