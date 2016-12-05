from config import *
from disseminator import *
from maple import *
from juice import *


class Listener():

    def __init__(self, member_list, juice_inst, maple_inst):
        self.member_list = member_list
        self.name = socket.gethostbyname(socket.gethostname())
        self.juice_inst = juice_inst
        self.maple_inst = maple_inst

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.setblocking(True)
        self.server_socket.bind((socket.gethostname(), listener_port))
        self.server_socket.listen(len(target_machines))

    def wait_for_order(self):
        print("Listening for updates on:")
        print("host:{} port:{}".format(self.name, listener_port))
        connection, sender_address = self.server_socket.accept()
        print("Message Recieved from {}".format(sender_address))
        data = connection.recv(200)
        print("Message = {}".format(data))
        return data

    def parse_order(self, order):
        global ping_message
        if order == ping_message:
            return

        elif order[0] == 'a':
            joiner_address = order[1:]
            if joiner_address in self.member_list:
                return
            else:
                self.member_list.append(joiner_address)
                self.member_list.sort()

        elif order[0] == 'r':
            leaver_address = order[1:]
            if leaver_address in self.member_list:
                self.member_list.remove(leaver_address)
                self.member_list.sort()
            else:
                return

        elif order[0] == 'm':
            maple_order = order[1:]
            maple_args = maple_order.split()
            self.maple_inst.start(maple_args)
            # do maple thing

        elif order[0] == 'j':
            juice_order = order[1:]
            juice_args = juice_order.split()
            self.juice_inst.start(juice_args)
            # do juice thing




