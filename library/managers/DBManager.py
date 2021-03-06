class DBManager:
    PATH_TO_DATABASE = "./data/database/"

    def __init__(self, main_log, fm):
        self.main_log = main_log
        self.fm = fm
        self.db = 0
        self.cur = 0

        self.connect_to_database()

    def connect_to_database(self):
        from sqlite3 import connect
        try:
            self.db = connect(self.PATH_TO_DATABASE + "clash_of_royale.db")
            self.cur = self.db.cursor()
            self.main_log.write_log("Database has been loaded", self)
        except Exception as e:
            self.main_log.write_log("Can't load database", self, self.main_log.CANT_LOAD_STATE)
            self.main_log.write_log("Error: " + str(e), self, self.main_log.ERROR_STATE)

    def do_request(self, request):
        try:
            request_result = self.cur.execute(request)
            self.db.commit()
            self.main_log.write_log(f"Do some operation with database: {request}", self)
        except Exception as e:
            self.main_log.write_log(f"fail to do que: {request}", self, self.main_log.ERROR_STATE)
            return 0
        return request_result
