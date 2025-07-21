from protocol import chatlib
from network.socket_utils import build_and_send_message


def send_error(conn, error_msg):
    """
    שולחת הודעת 'שגיאה' לצינור הלקוח

    :param:
        conn (socket): צינור לקוח מחובר
        error_msg (str): הודעה
    """
    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["error_msg"], error_msg)
