from config import *

def send_message(message, machines, port=listener_port):
    """Given a message and a list of machines, send the message to all the machines."""
    print("Sending Order: {}".format(message))
    for machine in machines:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # machine_address = ()
            tcp_socket.connect(machine, port)
            tcp_socket.sendall(message)
            # response = executor.recv(len(execution_ack_string))
            # print("Message to {}. Responded with {}".format(machine_address,response))
            print("Message Sent to {}".format(machine_address))
        except socket.error:
            print("Could not connect to {}.".format(machine))
