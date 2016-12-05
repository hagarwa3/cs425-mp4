import threading
from listener import *
from detector import *
from introducer import *

from config import *

member_list = []
keep_running = True
juice_inst = None
maple_inst = None

def listener_runner():
    global member_list, keep_running
    listening_server = Listener(member_list, juice_inst, maple_inst)
    while keep_running:
        incoming_order = listening_server.wait_for_order()
        listening_server.parse_order(incoming_order)
    
def detector_runner():
    global member_list, keep_running
    detector_inst = Detector(member_list)
    while keep_running:
        time.sleep(4)
        detector_inst.ping_neighbors()

def join_group():
    join_request = ping_message
    introducer_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    introducer_connection.connect((introducer_hostname, introducer_port))
    introducer_connection.close()

def introducer_runner():
    global member_list, keep_running
    member_list.append(socket.gethostbyname(socket.gethostname()))
    itroducer_server = Introducer(member_list)
    while keep_running:
        itroducer_server.introduce()

def main(is_introducer = False):
    global member_list, keep_running
    keep_running = True
    member_list = []

    if is_introducer:
        introducer_thread = threading.Thread(target=introducer_runner)
        introducer_thread.start()
        time.sleep(3)

    listener_thread = threading.Thread(target=listener_runner)
    listener_thread.start()

    detector_thread = threading.Thread(target=detector_runner)
    detector_thread.start()

    join_group()

    listener_thread.join()
    detector_thread.join()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        main(True)
