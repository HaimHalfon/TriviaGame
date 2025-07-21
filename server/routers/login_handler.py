from protocol import chatlib

import global_vars
from network.error import send_error
from network.socket_utils import build_and_send_message


def handle_login_message(conn, data):
    """
    מבצע טיפול בבקשת 'לוגאין' שנשלחה לשרת דרך צינור הלקוח

    :param:
        conn (socket): צינור לקוח מחובר
        data (str): שדה הנתונים שיכיל פרטי התחברות
    """

    data_split = chatlib.split_data(data, 2)  # 2 because: username and password
    username = data_split[0]
    password = data_split[1]

    if username not in global_vars.users:
        send_error(conn, "Username does not exist")
        return

    if password != global_vars.users[username]["password"]:
        send_error(conn, "Password does not match")
        return

    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["login_ok_msg"], "")
    global_vars.logged_users[conn.getpeername()] = username


def handle_logout_message(conn):
    """
    מבצע טיפול בבקשת 'לוגאאוט' שנשלחה לשרת דרך צינור הלקוח

    :param:
        conn (socket): צינור לקוח מחובר
    """
    global_vars.logged_users.pop(conn.getpeername())
    conn.close()
