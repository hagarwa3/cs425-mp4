# Reduce
from config import *
from disseminator import *
import os


class Juice():

    def __init__(self, member_list):
        self.member_list = member_list
        self.name = socket.gethostbyname(socket.gethostname())

    def start(self, juice_args):
        print("Juice start with: {}".format(juice_args))
        os.system(juice_args + " " + self.member_list.index[self.name])
        # start the maple exe

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("You can't run Juice without args")
        # TODO Write the warning string
        exit(1)

    order = " ".join(sys.argv[1:])
    order = 'j' + order
    print("Will send order: {}".format(order))
    send_message(order, target_machines) # TODO
