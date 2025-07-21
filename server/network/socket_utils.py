from protocol import chatlib
import global_vars
from utils.debug import debug_info


def build_and_send_message(conn, cmd, data):
    """
    יוצרת הודעת פרוטוקול חוקית ומוסיפה אותה לתור הדואר היוצא

    :param:
        conn (socket): צינור לקוח מחובר
        cmd (str): שם פקודה
        data (str): שדה נתונים
    """
    full_msg = chatlib.build_message(cmd, data)
    global_vars.messages_to_send.append((conn, full_msg))
    debug_info(f"[SERVER] {full_msg}")


def recv_message_and_parse(conn):
    """
    מושכת מצינור הלקוח את הודעת הפרוטוקול שהתקבלה ומחלצת ממנה את שדה הפקודה ושדה הנתונים

    :param:
        conn (socket): צינור לקוח מחובר

    :return:
        (str, str): טאפל של שדה הפקודה ושדה הנתונים
    """
    full_msg = conn.recv(1024).decode()
    debug_info(f"[CLIENT] {full_msg}")
    cmd, data = chatlib.parse_message(full_msg)
    return cmd, data
