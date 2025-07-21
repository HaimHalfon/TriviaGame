from protocol import chatlib
from network.socket_utils import build_send_recv_parse
from utils.debug import error_and_exit


def get_score(conn):
    """
    שולחת בקשת 'צפייה בנקודות שלי' לשרת דרך צינור הלקוח

    :param:
        socket: צינור לקוח מחובר
    """
    msg_code, data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["my_score_msg"], "")

    if msg_code == chatlib.PROTOCOL_SERVER["your_score_msg"]:
        print(f"Your score is: {data}")
    elif msg_code == chatlib.PROTOCOL_SERVER["error_msg"]:
        error_and_exit(data)


def get_high_score(conn):
    """
    שולחת בקשת 'צפייה בטבלת הנקודות' לשרת דרך צינור הלקוח

    :param:
        socket: צינור לקוח מחובר
    """
    msg_code, data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["highscore_msg"], "")

    if msg_code == chatlib.PROTOCOL_SERVER["all_score_msg"]:
        print(f"{'Name':<20} {'Value':<5}")
        for name, value in [line.split(": ") for line in data.strip().split("\n")]:
            print(f"{name:<20} {value:<5}")
    elif msg_code == chatlib.PROTOCOL_SERVER["error_msg"]:
        error_and_exit(data)
