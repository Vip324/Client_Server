import json
import re
from datetime import datetime
from common.my_decoraters import log
from common.project_const import *
from log.client_log_config import logger_client
from log.server_log_config import logger_server

'''
    Блок проверок на корректность данных
'''


@log
def ip_adr_validator(str):
    res = re.match(r'localhost|all|^localhost|^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}'
                   r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$', str)
    return bool(res)


@log
def port_validation(port):
    if isinstance(port, int) and port in range(1023, 65535):
        return True
    else:
        return False


@log
def len_client_data_validator(data):
    if len(data) > MAX_LEN_JSON_DATA:
        logger_client.warning(f'Сообщение больше чем {MAX_LEN_JSON_DATA} символов '
                              f'не может быть отправлено и было отправлено пустое.')
        data = json.dumps({'0': '0'})
    return data


@log
def client_server_msg_validation(msg):
    if not (ACTION in msg.keys()) or not (TIME in msg.keys()):
        logger_server.warning('Формат сообщение от клиента не корректный!')
        return False
    return True


@log
def server_client_msg_validation(msg):
    if not (ALERT in msg.keys()) ^ (ERROR in msg.keys()) or not (RESPONCE in msg.keys()):
        logger_client.warning('Формат сообщение от сервера не корректный!')
        return False
    return True


'''
    Блок обработки полученных сообщений сервером
'''


@log
def server_processing_msg(client_adr, client_msg):
    if not client_server_msg_validation(client_msg) or not (client_msg[ACTION] in ACTION_COMM):
        # сообщение не валидно или отсутсвует правильная команда 'action'
        logger_server.warning('Что то пошло не так!!! Не знаю что с этим делать!!!')
        return SERVER_MSG_400

    if client_msg[ACTION] == PRESENCE:
        # правильная команда 'action'
        if STATUS in client_msg[USER]:
            logger_server.debug(f'Клиент {client_adr} подтверждает '
                                f'свою доступность в {datetime.fromtimestamp(client_msg[TIME])}. '
                                f'Статус: {client_msg[USER][STATUS]}')
        else:
            logger_server.debug(f'Клиент {client_adr} подтверждает '
                                f'свою доступность в {datetime.fromtimestamp(client_msg[TIME])}.')
        return SERVER_MSG_200

    logger_server.info('Пока не умеею работать с это командой')
    # пока не описанные команды 'action'
    return SERVER_MSG_444


'''
    Блок процедур для server_echo
'''


def read_requests(clients_r, all_clients):
    responses = {}
    for sock in clients_r:
        try:
            data = sock.recv(640).decode(CODE)

            if not data:
                logger_server.info(f'Сокет {sock.getpeername()} закрылся.')
                all_clients.remove(sock)
                break

            responses[sock] = data

        except:
            all_clients.remove(sock)

    return responses


def write_responses(requests, clients_r, all_clients):
    for sock in all_clients:
        if bool(requests.get(sock)):
            resp = requests[sock].encode(CODE)

            try:
                for sock_r in clients_r:
                    sock_r.send(resp)

            except:
                logger_server.warning(f'Клиент {sock.fileno()} {sock.getpeername()} отключился.')
                all_clients.remove(sock)
