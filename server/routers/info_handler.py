from protocol import chatlib
import global_vars
from network.socket_utils import build_and_send_message


def handle_getscore_message(conn, username):
    """
    מבצע טיפול בבקשת 'צפייה בנקודות שלי' שנשלחה לשרת דרך צינור הלקוח

    :param:
        conn (socket): צינור לקוח מחובר
        username (str): שם משתמש הלקוח המחובר
    """
    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["your_score_msg"], str(global_vars.users[username]["score"]))


def handle_highscore_message(conn):
    """
    מבצע טיפול בבקשת 'צפייה בטבלת הנקודות' שנשלחה לשרת דרך צינור הלקוח

    :param:
        conn (socket): צינור לקוח מחובר
    """
    data_rsp = "\n".join(f"{user}: {global_vars.users[user]['score']}" for user in global_vars.users)
    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["all_score_msg"], data_rsp)


def handle_logged_message(conn):
    """
    מבצע טיפול בבקשת 'צפייה ברשימת המחוברים' שנשלחה לשרת דרך צינור הלקוח

    :param:
        conn (socket): צינור לקוח מחובר
    """
    data_rsp = ", ".join(user for user in global_vars.logged_users.values())
    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["logged_answer_msg"], data_rsp)
