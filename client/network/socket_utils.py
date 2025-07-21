from protocol import chatlib


def build_and_send_message(conn, cmd, data):
    """
    יוצרת הודעת פרוטוקול חוקית ושולחת אותה בצינור הלקוח

    :param:
        conn (socket): צינור לקוח מחובר
        cmd (str): שם פקודה
        data (str): שדה נתונים
    """
    full_msg = chatlib.build_message(cmd, data)
    conn.send(full_msg.encode())


def recv_message_and_parse(conn):
    """
    מושכת מצינור הלקוח את הודעת הפרוטוקול שהתקבלה ומחלצת ממנה את שדה הפקודה ושדה הנתונים

    :param:
        conn (socket): צינור לקוח מחובר

    :return:
        (str, str): טאפל של שדה הפקודה ושדה הנתונים
    """
    full_msg = conn.recv(1024).decode()
    msg_code, data = chatlib.parse_message(full_msg)
    return msg_code, data


def build_send_recv_parse(conn, cmd, data):
    """
    יוצרת הודעת פרוטוקול חוקית ושולחת אותה בצינור הלקוח
    לאחר מכן, מושכת מצינור הלקוח את הודעת הפרוטוקול שהתקבלה ומחלצת ממנה את שדה הפקודה ושדה הנתונים

    :param:
        conn (socket): צינור לקוח מחובר
        cmd (str): שם פקודה
        data (str): שדה נתונים

    :return:
        (str, str): טאפל של שדה הפקודה ושדה הנתונים
    """
    build_and_send_message(conn, cmd, data)
    msg_code, data = recv_message_and_parse(conn)
    return msg_code, data
