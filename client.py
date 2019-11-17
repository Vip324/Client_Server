import click
from socket import *
import json
from datetime import datetime
from common.utils import *
from log.client_log_config import logger_client


@click.command()
@click.option('--adr', '-a', prompt='Enter address of the server: ', help='Address of the Server.')
@click.option('--port', '-p', default=DEF_PORT, help='Port of the Server.')
def client_run(adr, port):
    if not ip_adr_validator(adr):
        logger_client.critical('IP-адрес задан не корректно!')
        return None
    if not port_validation(port):
        logger_client.critical('Порт задан не корректно!')
        return None

    client_msg = {
        ACTION: PRESENCE,
        TIME: int(datetime.now().timestamp()),
        USER: {
            ACC_NAME: 'C0deMaver1ck',
            STATUS: 'Hello World!'

        }
    }

    s = socket(AF_INET, SOCK_STREAM)
    logger_client.debug('Сокет открыт.')

    try:
        s.connect((adr, port))
        logger_client.debug('Соединение с сервером установлено.')

        data_out = json.dumps(client_msg)
        logger_client.debug('Сообщение сформировано.')

        # проверка сообщение на длину
        data_out = len_client_data_validator(data_out)

        s.send(data_out.encode(CODE))
        logger_client.debug('Сообщение отправлено на сервер.')

        data_in = s.recv(MAX_LEN_JSON_DATA)
        logger_client.debug('Сообщение от сервера получено.')
        server_msg = json.loads(data_in.decode(CODE))

        if not server_client_msg_validation(server_msg):
            s.close()
            return None

        logger_client.debug('Сообщение от сервера: {server_msg}')

    except:
        logger_client.critical('Соединение с сервером не может быть установлено.')

    s.close()
    logger_client.debug('Сокет закрыт.')


if __name__ == '__main__':
    client_run()
