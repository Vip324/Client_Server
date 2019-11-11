# параметры настройки соединения
DEF_PORT = 7777
DEF_ADR_CLIENT = 'all'

# параметры json сообщения
MAX_LEN_JSON_DATA = 640
MAX_LEN_ACTION = 15
MAX_LEN_RESPONSE = 3
MAX_LEN_NAME = 25
MAX_LEN_MSG = 500
CODE = 'utf-8'

# поля json сообщения
ACTION = 'action'
TIME = 'time'
USER = 'user'
TYPE = 'type'
STATUS = 'status'
PASSWORD = 'password'
ACC_NAME = 'account_name'
RESPONCE = 'response'
ALERT = 'alert'
ERROR = 'error'

# команды 'action'
PRESENCE = 'presence'
PROBE = 'prоbe'
MSG = 'msg'
QUIT = 'quit'
AUTH = 'authenticate'
JOIN = 'join'
LEAVE = 'leave'
ACTION_COMM = [PRESENCE, PROBE, MSG, QUIT, AUTH, JOIN, LEAVE]

# ответы сервера
SERVER_MSG_444 = {
    RESPONCE: 444,
    ERROR: 'Пока не умеею работать с это командой'
}
SERVER_MSG_400 = {
    RESPONCE: 400,
    ERROR: 'Неправильный запрос/JSON-объект'
}
SERVER_MSG_200 = {
    RESPONCE: 200,
    ALERT: "Ok"
}
