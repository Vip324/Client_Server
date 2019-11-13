import click
import json
from socket import *
from common.utils import *


@click.command()
@click.option('--port', '-p', default=DEF_PORT, help='Port of the Server.')
@click.option('--adr', '-a', default=DEF_ADR_CLIENT, help='Address of the Client.')
def server_run(port, adr):
    if not ip_adr_validator(adr) or not port_validation(port):
        return None

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen()
    try:
        while True:
            client, client_adr = s.accept()

            if adr != DEF_ADR_CLIENT and re.match(adr, client_adr[0]) is None:
                client.close()
                return None

            data_in = client.recv(MAX_LEN_JSON_DATA)
            client_msg = json.loads(data_in.decode(CODE))

            server_msg = server_processing_msg(client_adr, client_msg)

            data_out = json.dumps(server_msg)
            client.send(data_out.encode(CODE))
            client.close()

    except:
        s.close()


if __name__ == '__main__':
    server_run()
