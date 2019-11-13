import unittest
from datetime import datetime

from common.utils import *


class Test_Utils(unittest.TestCase):
    # проверка IP адреса
    def test_ip_adr_good(self):
        self.assertEqual(ip_adr_validator('127.0.0.1'), True)

    def test_ip_adr_bad_1(self):
        self.assertEqual(ip_adr_validator('727.0.0.1'), False)
        self.assertEqual(ip_adr_validator('127.300.0.1'), False)
        self.assertEqual(ip_adr_validator('127.0.400.1'), False)
        self.assertEqual(ip_adr_validator('127.0.0.256'), False)

    def test_ip_adr_bad_2(self):
        self.assertEqual(ip_adr_validator('127.0.0'), False)

    # проверка порта
    def test_port_good(self):
        self.assertEqual(port_validation(3333), True)

    def test_port_small(self):
        self.assertEqual(port_validation(1000), False)

    def test_port_biger(self):
        self.assertEqual(port_validation(66000), False)

    def test_port_not_int(self):
        self.assertEqual(port_validation('abc'), False)

    # проверка длины сообщения
    def test_len_msg_good(self):
        data = json.dumps({
            ACTION: PRESENCE,
            TIME: int(datetime.now().timestamp()),
            USER: {
                ACC_NAME: 'C0deMaver1ck',
                STATUS: 'Yep, I am here!'
            }
        })
        self.assertEqual(len_client_data_validator(data), json.dumps({
            ACTION: PRESENCE,
            TIME: int(datetime.now().timestamp()),
            USER: {
                ACC_NAME: 'C0deMaver1ck',
                STATUS: 'Yep, I am here!'
            }
        }))

    def test_len_msg_long(self):
        data = json.dumps({
            'a': 'a' * 650
        })
        self.assertEqual(len_client_data_validator(data), json.dumps({'0': '0'}))

    # проверка формата сообщения клиента
    def test_client_msg_good(self):
        data = {
            ACTION: PRESENCE,
            TIME: int(datetime.now().timestamp())}
        self.assertEqual(client_server_msg_validation(data), True)

    def test_client_msg_no_action(self):
        data = {
            TIME: int(datetime.now().timestamp())}
        self.assertEqual(client_server_msg_validation(data), False)

    def test_client_msg_no_time(self):
        data = {
            ACTION: PRESENCE}
        self.assertEqual(client_server_msg_validation(data), False)

    # проверка формата сообщения сервера
    def test_server_msg_good_alert(self):
        self.assertEqual(server_client_msg_validation(SERVER_MSG_200), True)

    def test_server_msg_good_error(self):
        self.assertEqual(server_client_msg_validation(SERVER_MSG_444), True)

    def test_server_msg_no_alert_and_error(self):
        msg = {
            RESPONCE: 444}
        self.assertEqual(server_client_msg_validation(msg), False)

    def test_server_msg_no_response(self):
        msg = {
            ALERT: 'Ужас!!!'}
        self.assertEqual(server_client_msg_validation(msg), False)

    # обработка полученных сообщений сервером
    def test_server_processing_good(self):
        client_msg = {
            ACTION: PRESENCE,
            TIME: int(datetime.now().timestamp())
        }
        client_adr = ('127.0.0.1', 5123)
        self.assertEqual(server_processing_msg(client_adr, client_msg), SERVER_MSG_200)

    def test_server_processing_no_time(self):
        client_msg = {
            ACTION: PRESENCE
        }
        client_adr = ('127.0.0.1', 5123)
        self.assertEqual(server_processing_msg(client_adr, client_msg), SERVER_MSG_400)

    def test_server_processing_no_action(self):
        client_msg = {
            TIME: int(datetime.now().timestamp())
        }
        client_adr = ('127.0.0.1', 5123)
        self.assertEqual(server_processing_msg(client_adr, client_msg), SERVER_MSG_400)

    def test_server_processing_unknow_com(self):
        client_msg = {
            ACTION: JOIN,
            TIME: int(datetime.now().timestamp())
        }
        client_adr = ('127.0.0.1', 5123)
        self.assertEqual(server_processing_msg(client_adr, client_msg), SERVER_MSG_444)



if __name__ == '__main__':
    unittest.main()
