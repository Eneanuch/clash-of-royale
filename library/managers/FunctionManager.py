class FunctionManager:
    def __init__(self, main_log, *functions):
        self.functions = dict()
        self.main_log = main_log
        # adding and initing functions (if you will give it in constructor)
        for i in functions:
            self.functions[i.__name__] = i(main_log, self)
            self.main_log.write_log(f'not inited function {i.__name__} has been added', self)

    def add_function(self, func):
        # There are should be inited function
        self.functions[func.__class__.__name__] = func
        self.main_log.write_log(f'inited function {func.__class__.__name__} has been added', self)

    def add_not_inited_function(self, func):
        # initing class and add to functions dict
        self.functions[func.__name__] = func(self.main_log, self)
        self.main_log.write_log(f'not inited function {func.__name__} has been added', self)

    def get_function(self, func_name):
        # its returning function (inited class)
        self.main_log.write_log(f'returning {self.functions[func_name]} (get_func)', self)
        return self.functions[func_name]

    def delete_function(self, func_name):
        # there are deleting of function (i dont now how we will use it)
        self.functions.pop(func_name)
        self.main_log.write_log(f'delete {func_name} from functions manager', self)
