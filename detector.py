from config import *
from disseminator import *

class Detector():

    def __init__ (self, member_list):
        self.member_list = member_list
        self.name = socket.gethostbyname(socket.gethostname())

    def re_join_group(self):
        join_request = ping_message
        introducer_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        introducer_connection.connect((introducer_hostname, introducer_port))
        introducer_connection.close()

    def get_neighbours(self):
        index = None
        try:
            index = self.member_list.index(self.name)
        except:
            print("joining again")
            self.re_join_group()
            return

        if len(self.member_list) < 4:
            neighbors = set(self.member_list)
            neighbors.remove(self.name)
            return neighbors

        neighbors = set()
        neighbors.add(self.member_list[index-2])
        neighbors.add(self.member_list[index-1])
        neighbors.add(self.member_list[index+1])
        neighbors.add(self.member_list[index+2])
        return neighbors

    def ping_neighbors(self):
        global ping_message
        print(self.member_list)
        neighbors = self.get_neighbors()
        for neighbor in neighbors:
            listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                listener.connect((neighbor, listener_port))
                listener.sendall(ping_message)
                listener.close()
            except socket.error:
                send_message("r{}".format(neighbor), self.member_list)

