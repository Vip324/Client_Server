from socket import *
from common.project_const import *
from log.client_log_config import logger_client


def client_r():
    with socket(AF_INET, SOCK_STREAM) as cl_r_sock:
        try:
            cl_r_sock.connect(('localhost', DEF_PORT))
            logger_client.debug(f'Сокет {cl_r_sock.getsockname()} открыт '
                                f'и установил соединение с сервером.')

        except:
            logger_client.critical('Соединение с сервером не может быть установлено.')

        else:
            while True:
                server_msg = cl_r_sock.recv(640)

                if server_msg != b'':
                    logger_client.debug(f'Сокет {cl_r_sock.getsockname()} сообщение '
                                        f'от сервера получил: {server_msg.decode(CODE)}')
                    # print(f'Сообщение от сервера получено: {server_msg.decode(CODE)}')


if __name__ == '__main__':
    client_r()
