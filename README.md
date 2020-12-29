# clash-of-royale
ITs best game in the our world, it will broke play market and appstore, ETO NORMALNO VOOBSHE??? GREMLINI VPERED


Немного про менеджеры
Далее main_log - класс для логирования, fm - FunctionManager
На данный момент есть слудующие менеджеры с слудующими функциями:

Главный менеджер
FunctionManager(main_log, *functions) - добавляет НЕ инициализированные классы из списка functions в список функций, образуя словарь {"Имя класса": <обьект класса>}
  add_function(func) - добавляет инициализированный класс в словарь функций
  add_not_inited_function(func) - инициалиизирует класс и добавляет его в словарь функций
  get_function(func_name) - возвращает класс из словаря (НЕТ обработчика ошибок)
  delete_function(func_name) - удаляет класс из словаря по имени класса

Менеджер конфигурации
CFGManager(main_log, fm) 
  load_config() - загружает стандартный конфиг
  reload_config() - перезагружает конфиг
  read_var_from_cfg(word, default) - возвращает значение переменной с ключом word, если такой нет, то возвращает default
  write_var_to_cfg(word, parameter) - задает значение переменной с ключом word значение parameter

Менеджер БД
DBManager(main_log, fm)
  connect_to_database() - загружает бд
  do_request(request) - выполняет запрос к базе данных, возвращает значение полученное при запросе или 0 в случае ошибки

Менеджер перевода
TranstaleManger(main_log, fm)
  set_current_language(lang) - устанавливает текуций язык по его номеру 
  translate(word) - возвращает переведенное слово по ключевому слову на выбранный язык, при ошибке возвращет ключевое слово
  get_languages() - возвращает словарь языков

Менеджер изображений
IMGManager(main_log, fm)
  set_pygame(pygame) - для работы необходима установка pygame (чтобы не импортировать повторно, т.к грузит он долго), устанавливает pygame
  load_image(name, colorkey=None) - возвращает изображение (если такое же загружалось ранее, то возвращает загруженное)

