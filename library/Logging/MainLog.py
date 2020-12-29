from datetime import datetime

ERROR_STATE = 2
CANT_LOAD_STATE = 3
DEFAULT_STATE = 1
NO_NAME_LOG_STATE = 1


class NoNameLog:
    pass
# очень полезный класс, точно не затычка


class MainLog:
    def __init__(self, log_path, print_logs, log_it):
        self.log_path = log_path  # path to logs
        self.print_logs = print_logs  # is program need to print logs
        self.log_it = log_it  # do logs ?(действительно, а для кого я тогда эту хрень делаю???)

    def write_log(self, message, class_=NO_NAME_LOG_STATE, state=DEFAULT_STATE):
        if class_ == NO_NAME_LOG_STATE:
            class_ = NoNameLog()
        if state == DEFAULT_STATE:
            message = f"{class_.__class__.__name__}: {message} | " \
                      f"{datetime.today().strftime('%H:%M:%S')}\n"
        elif state == ERROR_STATE:
            message = f"!! Error in {class_.__class__.__name__}: {message} | " \
                      f"{datetime.today().strftime('%H:%M:%S')}\n"
        elif state == CANT_LOAD_STATE:
            message = f"?? {message}  ({class_.__class__.__name__}) | " \
                      f"{datetime.today().strftime('%H:%M:%S')}\n"
        if self.log_it:
            global start_log_it
            global file
            if not start_log_it:
                start_log_it = 1
                file = open(self.log_path + 'logs.' +
                            datetime.today().strftime('%Y-%m-%d-%H.%M.%S') + '.log',
                            mode="w", encoding='utf-8')
            file.write(message)
        if self.print_logs:
            print(message[:-1])