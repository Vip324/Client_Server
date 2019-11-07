import click
from socket import *
import json
import re


@click.command()
@click.option('--port', '-p', default=7777, help='Port of the Server.')
@click.option('--adr', '-a', default='ALL', help='Address of the Client.')
def server_run(port, adr):
    res = re.match(r'ALL|^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}'
                   r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$', adr)

    if res is not None and port > 1023:

        s = socket(AF_INET, SOCK_STREAM)
        s.bind(('localhost', port))
        s.listen()

        try:
            while True:
                client, client_adr = s.accept()

                if adr == 'ALL' or re.match(adr, client_adr[0]):
                    data_in = client.recv(600)
                    client_msg = json.loads(data_in.decode('utf-8'))

                    if client_msg['action'] == 'presence':
                        print(f"Сообщение: {client_msg['user']['status']}, "
                              f"было отправлено клиентом: {client_adr}, {client_msg['time']}")
                        server_msg = {
                            "response": 202,
                            "alert": 'Подтверждение'
                        }
                    else:
                        print(f"Что то пошло не так!!! Не знаю что с этим делать!!!")
                        server_msg = {
                            "response": 400,
                            "error": 'Неправильный запрос/JSON-объект'
                        }

                    data_out = json.dumps(server_msg)
                    client.send(data_out.encode('utf-8'))
                client.close()

        except:
            s.close()
    else:
        print('Адрес и порт сервера заданы не корректно!')

if __name__ == '__main__':
    server_run()
