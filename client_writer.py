from socket import *
from common.project_const import *
from log.client_log_config import logger_client


def client_w():
    with socket(AF_INET, SOCK_STREAM) as cl_sock:
        try:
            cl_sock.connect(('localhost', DEF_PORT))
            logger_client.debug(f'Сокет {cl_sock.getsockname()} открыт и установил соединение с сервером.')

        except:
            logger_client.critical('Соединение с сервером не может быть установлено.')

        while True:
            msg = input('Введите ваше сообщение или ''exit'' для выхода: ')
            if msg == 'exit':
                break

            cl_sock.send(msg.encode(CODE))
            logger_client.debug(f'Сокет {cl_sock.getsockname()} отправил сообщение на сервер.')


        logger_client.debug(f'Сокет {cl_sock.getsockname()} закрыт.')


if __name__ == '__main__':
    client_w()
