import click
from socket import *
import json
from datetime import datetime

from common.utils import *


@click.command()
@click.option('--adr', '-a', prompt='Enter address of the server: ', help='Address of the Server.')
@click.option('--port', '-p', default=DEF_PORT, help='Port of the Server.')
def client_run(adr, port):
    if not ip_adr_validator(adr) or not port_validation(port):
        return None

    client_msg = {
        ACTION: PRESENCE,
        TIME: int(datetime.now().timestamp()),
        USER: {
            ACC_NAME: 'C0deMaver1ck',
            STATUS: 'Yep, I am here!'
        }
    }

    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((adr, port))

        data_out = json.dumps(client_msg)
        data_out = len_client_data_validator(data_out)  # проверка сообщение на длину
        s.send(data_out.encode(CODE))

        data_in = s.recv(MAX_LEN_JSON_DATA)
        server_msg = json.loads(data_in.decode(CODE))

        if not server_client_msg_validation(server_msg):
            s.close()
            return None

        print(f'Сообщение от сервера: {server_msg}')

    except:
        print('Соединение с сервером не может быть установлено.')

    s.close()


if __name__ == '__main__':
    client_run()
