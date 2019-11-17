import click
import json
from socket import *
from common.utils import *
from log.server_log_config import logger_server


@click.command()
@click.option('--port', '-p', default=DEF_PORT, help='Port of the Server.')
@click.option('--adr', '-a', default=DEF_ADR_CLIENT, help='Address of the Client.')
def server_run(port, adr):
    if not ip_adr_validator(adr):
        logger_server.critical('IP-адрес задан не корректно!')
        return None
    if not port_validation(port):
        logger_server.critical('Порт задан не корректно!')
        return None

    s = socket(AF_INET, SOCK_STREAM)
    logger_server.debug(f'Сокет открыт.')
    s.bind(('', port))
    s.listen()
    logger_server.debug('Сервер запущен и находится в режиме прослушиваия.')

    try:
        while True:
            client, client_adr = s.accept()
            logger_server.debug(f'Открыта сессия с клиентом : {client_adr}.')

            if adr != DEF_ADR_CLIENT and re.match(adr, client_adr[0]) is None:
                logger_server.warning(f'Клиенту с адресом: {client_adr[0]} связь с сервером не разрешена.')
                client.close()
                logger_server.debug('Закрыта сессия с клиентом.')
                return None

            data_in = client.recv(MAX_LEN_JSON_DATA)
            logger_server.debug(f'Поступило сообщение от клиента: {client_adr}.')
            client_msg = json.loads(data_in.decode(CODE))

            server_msg = server_processing_msg(client_adr, client_msg)
            logger_server.debug('Сервер обработал сообщение.')

            data_out = json.dumps(server_msg)
            client.send(data_out.encode(CODE))
            logger_server.debug('Сервер отправил ответ.')

            client.close()
            logger_server.debug('Закрыта сессия с клиентом.')


    except:
        logger_server.critical('Не корректное завершение работы сервера!')
        s.close()
        logger_server.debug('Сокет закрыт.')


if __name__ == '__main__':
    server_run()
