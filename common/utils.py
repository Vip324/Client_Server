import json
import re
from common.project_const import *


# проверка на корректность данных

def ip_adr_validator(str):
    res = re.match(r'localhost|all|^localhost|^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}'
                   r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$', str)
    if res is None:
        print('IP-адрес задан не корректно!')
        return False
    return True


def port_validation(port):
    if type(port) != int:
        return False
    if port < 1023 or port > 65535:
        print('Порт задан не корректно!')
        return False
    return True


def len_client_data_validator(data):
    if len(data) > MAX_LEN_JSON_DATA:
        print(f'Сообщение больше чем {MAX_LEN_JSON_DATA} символов не может быть отправлено и было отправлено пустое.')
        data = json.dumps({'0': '0'})
    return data


def client_server_msg_validation(msg):
    if not (ACTION in msg.keys()) or not (TIME in msg.keys()):
        print('Формат сообщение от клиента не корректный!')
        return False
    return True


def server_client_msg_validation(msg):
    if not (ALERT in msg.keys()) ^ (ERROR in msg.keys()) or not (RESPONCE in msg.keys()):
        print('Формат сообщение от сервера не корректный!')
        return False
    return True


# обработка полученных сообщений сервером

def server_processing_msg(client_adr, client_msg):
    # сообщение не валидно или отсутсвует правильная команда 'action'
    if not client_server_msg_validation(client_msg) or not (client_msg[ACTION] in ACTION_COMM):
        print(f'Что то пошло не так!!! Не знаю что с этим делать!!!')
        return SERVER_MSG_400

    # правильная команда 'action'
    if client_msg[ACTION] == PRESENCE:
        print(f'Сообщение было отправлено клиентом: {client_adr}, {client_msg[TIME]}')
        return SERVER_MSG_200

    # пока не описанные команды 'action'
    print(f'Пока не умеею работать с это командой')
    return SERVER_MSG_444