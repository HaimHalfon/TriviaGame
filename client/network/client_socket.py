import socket
from config import SERVER_IP, SERVER_PORT
from utils.debug import debug_info


def connect():
    """
    יוצרת צינור לקוח חדש ומבצעת חיבור בינו לשרת

    :return:
        socket: צינור לקוח מחובר
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    debug_info(f"You have connected to the server at ({SERVER_IP}, {SERVER_PORT})")
    return client_socket


def disconnect(conn):
    """
    מנתקת את חיבור הצינור מהשרת

    :param:
        conn (socket): צינור לקוח מחובר
    """
    conn.close()
    debug_info(f"You have disconnected from the server.")
