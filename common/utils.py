import json
import re
from datetime import datetime
from common.my_decoraters import log
from common.project_const import *
from log.client_log_config import logger_client
from log.server_log_config import logger_server


# проверка на корректность данных
@log
def ip_adr_validator(str):
    res = re.match(r'localhost|all|^localhost|^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}'
                   r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$', str)
    if res is None:
        return False
    return True


@log
def port_validation(port):
    if type(port) != int:
        return False
    if port < 1023 or port > 65535:
        return False
    return True


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


# обработка полученных сообщений сервером
@log
def server_processing_msg(client_adr, client_msg):
    # сообщение не валидно или отсутсвует правильная команда 'action'
    if not client_server_msg_validation(client_msg) or not (client_msg[ACTION] in ACTION_COMM):
        logger_server.warning('Что то пошло не так!!! Не знаю что с этим делать!!!')
        return SERVER_MSG_400

    # правильная команда 'action'
    if client_msg[ACTION] == PRESENCE:
        if STATUS in client_msg[USER]:
            logger_server.debug(f'Клиент {client_adr} подтверждает '
                                f'свою доступность в {datetime.fromtimestamp(client_msg[TIME])}. '
                                f'Статус: {client_msg[USER][STATUS]}')
        else:
            logger_server.debug(f'Клиент {client_adr} подтверждает '
                                f'свою доступность в {datetime.fromtimestamp(client_msg[TIME])}.')
        return SERVER_MSG_200

    # пока не описанные команды 'action'
    logger_server.info('Пока не умеею работать с это командой')
    return SERVER_MSG_444


# процедуры для server_echo
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
        if sock in requests:
            resp = requests[sock].encode(CODE)

            try:
                for sock_r in clients_r:
                    sock_r.send(resp)

            except:
                logger_server.warning(f'Клиент {sock.fileno()} {sock.getpeername()} отключился.')
                all_clients.remove(sock)
