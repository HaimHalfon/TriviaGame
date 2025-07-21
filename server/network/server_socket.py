import socket
from config import SERVER_IP, SERVER_PORT


def setup_socket():
    """
    יוצרת צינור שרת TCP חדש ומתחילה האזנה

    :return:
        socket: צינור שרת מאזין
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()
    return server_socket
