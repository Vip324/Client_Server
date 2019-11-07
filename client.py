import click
from socket import *
import json
import time
import re


@click.command()
@click.option('--adr', '-a', prompt='Enter address of the server: ', help='Address of the Server.')
@click.option('--port', '-p', default=7777, help='Port of the Server.')
def client_run(adr, port):
    res = re.match(r'^localhost|^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}'
                   r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$', adr)

    if res and port > 1023:

        client_msg = {
            "action": "presence",
            "time": time.ctime(time.time()),
            "type": "status",
            "user": {
                "account_name": "C0deMaver1ck",
                "status": "Yep, I am here!"
            }
        }

        s = socket(AF_INET, SOCK_STREAM)
        try:
            s.connect((adr, port))

            data_out = json.dumps(client_msg)
            s.send(data_out.encode('utf-8'))

            data_in = s.recv(600)
            server_msg = json.loads(data_in.decode('utf-8'))

            if server_msg['response'] < 300:
                print(f"Сообщение от сервера: {server_msg['alert']} , код : {server_msg['response']}")
            else:
                print(f"Сообщение от сервера: {server_msg['error']} , код : {server_msg['response']}")

        except:
            print('Соединение с сервером не может быть установлено.')

        s.close()

    else:
        print('Адрес и порт сервера заданы не корректно!')


if __name__ == '__main__':
    client_run()
