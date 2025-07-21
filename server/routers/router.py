from protocol import chatlib

import global_vars

from routers.login_handler import handle_login_message
from routers.game_handler import handle_question_message, handle_answer_message
from routers.info_handler import handle_getscore_message, handle_highscore_message, handle_logged_message
from network.error import send_error


def route_messages(conn, cmd, data):
    """
    מנתב את בקשת הפקודה לפונקציה הנכונה

    :param:
        conn (socket): צינור לקוח מחובר
        cmd (str): שם פקודה
        data (str): שדה נתונים
    """

    if conn.getpeername() in global_vars.logged_users:
        flag_login = True
        username = global_vars.logged_users[conn.getpeername()]
    else:
        flag_login = False
        username = None

    if cmd == chatlib.PROTOCOL_CLIENT["login_msg"] and not flag_login:
        handle_login_message(conn, data)

    elif cmd == chatlib.PROTOCOL_CLIENT["get_question_msg"] and flag_login:
        handle_question_message(conn, username)

    elif cmd == chatlib.PROTOCOL_CLIENT["send_answer_msg"] and flag_login:
        handle_answer_message(conn, username, data)

    elif cmd == chatlib.PROTOCOL_CLIENT["my_score_msg"] and flag_login:
        handle_getscore_message(conn, username)

    elif cmd == chatlib.PROTOCOL_CLIENT["highscore_msg"] and flag_login:
        handle_highscore_message(conn)

    elif cmd == chatlib.PROTOCOL_CLIENT["logged_msg"] and flag_login:
        handle_logged_message(conn)

    else:
        send_error(conn, "The command is not recognized")
