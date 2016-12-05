from config import *
from disseminator import *

class Detector():

    def __init__ (self, member_list):
        self.member_list = member_list
        self.name = socket.gethostbyname(socket.gethostname())

    def get_neighbours(self):
        index = None
        try:
            index = self.member_list.index(self.name)
        except:
            print("joining again")
            self.re_join_group()
            return
        
        if (len(self.member_list) < 4):
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
        print(self.member_list)
        ping_message= length_padder(len(ping_message)) + ping_message
        send_message(ping_message, self.member_list)