import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import select

from protocol import chatlib

import global_vars
from config import SERVER_IP, SERVER_PORT

from db.users import load_users_database
from db.questions import load_questions_database

from utils.debug import debug_info

from network.server_socket import setup_socket
from network.socket_utils import recv_message_and_parse

from routers.login_handler import handle_logout_message

from routers.router import route_messages


def main():
    debug_info(f"Welcome to Trivia Server! ({SERVER_IP}, {SERVER_PORT})")

    global_vars.users = load_users_database()
    global_vars.questions = load_questions_database()

    server_socket = setup_socket()
    client_sockets = []

    while True:
        ready_to_read, ready_to_write, in_error = select.select([server_socket] + client_sockets, client_sockets, [])

        if not ready_to_read:
            continue

        for current_socket in ready_to_read:

            if current_socket is server_socket:  # לקוח חדש מבקש להתחבר
                client_socket, client_address = server_socket.accept()
                debug_info(f"Connection established with {client_address}")
                client_sockets.append(client_socket)

            else:  # לקוח קיים שלח הודעה
                try:
                    cmd, data = recv_message_and_parse(current_socket)

                    if cmd == chatlib.PROTOCOL_CLIENT["logout_msg"]:
                        debug_info(f"Disconnection established with {current_socket.getpeername()}")
                        client_sockets.remove(current_socket)
                        handle_logout_message(current_socket)
                    else:
                        route_messages(current_socket, cmd, data)

                except ConnectionError:  # סגירה בלתי צפויה של הלקוח
                    debug_info(f"Disconnection abruptly established with {current_socket.getpeername()}")
                    client_sockets.remove(current_socket)
                    handle_logout_message(current_socket)

        for msg in global_vars.messages_to_send:
            current_socket, rsp = msg
            if current_socket in ready_to_write:
                current_socket.send(rsp.encode("utf-8"))
                global_vars.messages_to_send.remove(msg)


if __name__ == "__main__":
    main()
