from config import *
from disseminator import *

introducer_server = None

class Introducer():

    def __init__(self, member_list):
        self.member_list = member_list
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.setblocking(True)
        self.server_socket.bind((socket.gethostname(), introducer_port))
        self.server_socket.listen(len(target_machines))

    def wait_for_join(self):
        print("Introducer waiting for order on")
        print("host:{} port:{}".format(socket.gethostname(), introducer_port))
        connection, joiner_address = self.server_socket.accept()
        print("{} requested to be introduced".format(joiner_address))
        connection.close()
        return joiner_address

    def send_state(self, joiner_address):
        for member in self.member_list:
            send_message('a{}'.format(member), [joiner_address[0]])

    def introduce(self):
        joiner_address = self.wait_for_join()
        send_message('a{}'.format(joiner_address), self.member_list)
        self.send_state(joiner_address)

    def shutdown(self):
        self.server_socket.close()

