# clash-of-royale
ITs best game in the our world, it will broke play market and appstore, ETO NORMALNO VOOBSHE??? GREMLINI VPERED


Немного про менеджеры<br>
Далее main_log - класс для логирования, fm - FunctionManager<br>
На данный момент есть слудующие менеджеры с слудующими функциями:<br>
<br>
Главный менеджер<br>
FunctionManager(main_log, *functions) - добавляет НЕ инициализированные классы из списка functions в список функций, образуя словарь {"Имя класса": <обьект класса>} <br>
  add_function(func) - добавляет инициализированный класс в словарь функций<br>
  add_not_inited_function(func) - инициалиизирует класс и добавляет его в словарь функций<br>
  get_function(func_name) - возвращает класс из словаря (НЕТ обработчика ошибок)<br>
  delete_function(func_name) - удаляет класс из словаря по имени класса<br>
<br>
Менеджер конфигурации<br>
CFGManager(main_log, fm) <br>
  load_config() - загружает стандартный конфиг<br>
  reload_config() - перезагружает конфиг<br>
  read_var_from_cfg(word, default) - возвращает значение переменной с ключом word, если такой нет, то возвращает default<br>
  write_var_to_cfg(word, parameter) - задает значение переменной с ключом word значение parameter<br>
<br>
Менеджер БД<br>
DBManager(main_log, fm)<br>
  connect_to_database() - загружает бд<br>
  do_request(request) - выполняет запрос к базе данных, возвращает значение полученное при запросе или 0 в случае ошибки<br>
<br>
Менеджер перевода<br>
TranstaleManger(main_log, fm)<br>
  set_current_language(lang) - устанавливает текуций язык по его номеру <br>
  translate(word) - возвращает переведенное слово по ключевому слову на выбранный язык, при ошибке возвращет ключевое слово<br>
  get_languages() - возвращает словарь языков<br>
<br>
Менеджер изображений<br>
IMGManager(main_log, fm)<br>
  set_pygame(pygame) - для работы необходима установка pygame (чтобы не импортировать повторно, т.к грузит он долго), устанавливает pygame<br>
  load_image(name, colorkey=None) - возвращает изображение (если такое же загружалось ранее, то возвращает загруженное)<br>

