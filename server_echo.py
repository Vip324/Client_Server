import select
from socket import *
from common.project_const import *
from common.utils import *


def server_echo():
    address = ('', DEF_PORT)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(address)
        s.listen(5)
        s.settimeout(0.2)  # Таймаут для операций с сокетом

        clients = []

        while True:
            try:
                client, client_adr = s.accept()
                logger_server.debug(f'Открыта сессия с клиентом : {client_adr}.')

            except OSError as e:
                pass

            else:
                clients.append(client)

            finally:
                wait = 5
                r = []
                w = []
                try:
                    r, w, e = select.select(clients, clients, [], wait)

                except:
                    pass  # Ничего не делать, если какой-то клиент отключился

                requests = read_requests(r, clients)
                if requests:
                    write_responses(requests, w, clients)


if __name__ == '__main__':
    server_echo()
