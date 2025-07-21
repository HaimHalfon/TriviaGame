from protocol import chatlib
from network.socket_utils import build_send_recv_parse
from utils.debug import error_and_exit


def get_logged_users(conn):
    """
    שולחת בקשת 'צפייה ברשימת המחוברים' לשרת דרך צינור הלקוח

    :param:
        socket: צינור לקוח מחובר
    """
    msg_code, data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["logged_msg"], "")

    if msg_code == chatlib.PROTOCOL_SERVER["logged_answer_msg"]:
        print(f"Online now: {data}")
    elif msg_code == chatlib.PROTOCOL_SERVER["error_msg"]:
        error_and_exit(data)
