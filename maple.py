# Map
from config import *
from disseminator import *


class Maple():

    def __init__(self, member_list):
        self.member_list = member_list
        self.name = socket.gethostbyname(socket.gethostname())

    def start(self, maple_args):
        print("Maple start with: {}".format(maple_args))
        # start the maple exe

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("You can't run Maple without args")
        print("$ maple <maple_exe> <num_maples> <sdfs_intermediate_file_name> <sdfs_src_directory>")
        exit(1)

    order = " ".join(sys.argv[1:])
    order = 'm'+order
    print("Will send order: {}".format(order))
    send_message(order, target_machines) # TODO
