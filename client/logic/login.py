from protocol import chatlib
from network.socket_utils import build_and_send_message, build_send_recv_parse


def login(conn):
    """
    קולטת מהמשתמש פרטי התחברות ושולחת בקשת 'לוגאין' לשרת דרך צינור הלקוח

    :param:
        conn (socket): צינור לקוח מחובר
    """
    while True:
        username = input("Please enter username: \n")
        password = input("Please enter password: \n")

        msg_code, data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["login_msg"], chatlib.join_data([username, password]))

        if msg_code == chatlib.PROTOCOL_SERVER["login_ok_msg"]:
            print(f"Welcome {username}!")
            return
        elif msg_code == chatlib.PROTOCOL_SERVER["error_msg"]:
            print(f"Failed. {data}! Try again.")


def logout(conn):
    """
    שולחת בקשת 'לוגאאוט' לשרת דרך צינור הלקוח

    :param:
        socket: צינור לקוח מחובר
    """
    build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["logout_msg"], "")
    print("GoodBye")
