from datetime import datetime


class NoNameLog:
    pass


# очень полезный класс, точно не затычка


class MainLog:  # it will build and write logs
    ERROR_STATE = 2  # some error
    CANT_LOAD_STATE = 3  # if you cant load file
    DEFAULT_STATE = 1  # its good
    NO_NAME_LOG_STATE = 1

    PATH_TO_LOGS = "./logs/"

    def __init__(self, print_logs, log_it):
        self.print_logs = print_logs  # is program need to print logs
        self.log_it = log_it  # do logs ?(действительно, а для кого я тогда эту хрень делаю???)

        self.start_log_it = 0
        self.file = 0

    def write_log(self, message, class_=NO_NAME_LOG_STATE, state=DEFAULT_STATE):
        if class_ == self.NO_NAME_LOG_STATE:
            class_ = NoNameLog()
        if state == self.DEFAULT_STATE:
            message = f":) {class_.__class__.__name__}: {message} | " \
                      f"{datetime.today().strftime('%H:%M:%S')}\n"
        elif state == self.ERROR_STATE:
            message = f"!! Error in {class_.__class__.__name__}: {message} | " \
                      f"{datetime.today().strftime('%H:%M:%S')}\n"
        elif state == self.CANT_LOAD_STATE:
            message = f"?? {message}  ({class_.__class__.__name__}) | " \
                      f"{datetime.today().strftime('%H:%M:%S')}\n"
        if self.log_it:
            if not self.start_log_it:
                self.start_log_it = 1
                self.file = open(self.PATH_TO_LOGS + 'logs.' +
                                 datetime.today().strftime('%Y-%m-%d-%H.%M.%S') + '.log',
                                 mode="w", encoding='utf-8')
            self.file.write(message)
        if self.print_logs:
            print(message[:-1])
