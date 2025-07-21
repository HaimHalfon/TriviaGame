from functools import reduce

# Example: [LOGIN           |0009|aaaa#bbbb]

CMD_FIELD_LENGTH = 16  # האורך המדויק של שדה הפקודה
LENGTH_FIELD_LENGTH = 4  # האורך המדויק של שדה הגודל

MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # האורך המדויק של שדות הכותרת
MAX_DATA_LENGTH = 10**LENGTH_FIELD_LENGTH - 1  # האורך המקסימלי של שדה הנתונים
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # האורך המקסימלי של כל ההודעה

DELIMITER = "|"  # התו המפריד בין שדות הפרוטוקול
DATA_DELIMITER = "#"  # התו המפריד בין הפרמטרים בתוך שדה הנתונים

PROTOCOL_CLIENT = {
    "login_msg": "LOGIN",
    "logout_msg": "LOGOUT",
    "my_score_msg": "MY_SCORE",
    "highscore_msg": "HIGHSCORE",
    "get_question_msg": "GET_QUESTION",
    "send_answer_msg": "SEND_ANSWER",
    "logged_msg": "LOGGED",
}

PROTOCOL_SERVER = {
    "login_ok_msg": "LOGIN_OK",
    "logged_answer_msg": "LOGGED_ANSWER",
    "your_score_msg": "YOUR_SCORE",
    "all_score_msg": "ALL_SCORE",
    "your_question_msg": "YOUR_QUESTION",
    "no_question_msg": "NO_QUESTIONS",
    "correct_answer_msg": "CORRECT_ANSWER",
    "wrong_answer_msg": "WRONG_ANSWER",
    "error_msg": "ERROR",
}

ERROR_RETURN = None


def build_message(cmd, data):
    """
    יוצרת הודעת פרוטוקול חוקית

    :param:
        cmd (str): שם פקודה
        data (str): שדה נתונים

    :return:
        ERROR_RETURN: אם קרתה תקלה
        str: הודעה בפורמט הפרוטוקול
    """
    if len(cmd) > CMD_FIELD_LENGTH or len(data) > MAX_DATA_LENGTH:
        return ERROR_RETURN

    full_msg = str(cmd) + " " * (CMD_FIELD_LENGTH - len(cmd))
    full_msg += DELIMITER
    full_msg += str(len(data)).zfill(LENGTH_FIELD_LENGTH)
    full_msg += DELIMITER
    full_msg += data

    return full_msg


def parse_message(msg):
    """
    מחלצת את שדה הפקודה ושדה הנתונים

    :param:
        msg (str): הודעת פרוטוקול חוקית

    :return:
        ERROR_RETURN, ERROR_RETURN: אם קרתה תקלה
        (str, str): טאפל של שדה הפקודה ושדה הנתונים
    """
    msg_split = msg.split(DELIMITER)
    if len(msg_split) != 3:
        return ERROR_RETURN, ERROR_RETURN

    cmd = msg_split[0]
    if len(cmd) != CMD_FIELD_LENGTH:
        return ERROR_RETURN, ERROR_RETURN

    len_field = msg_split[1]
    if len(len_field) != LENGTH_FIELD_LENGTH or not len_field.replace(" ", "").isdigit():
        return ERROR_RETURN, ERROR_RETURN

    data = msg_split[2]
    if len(data) != int(len_field):
        return ERROR_RETURN, ERROR_RETURN

    return cmd.strip(), data


def split_data(msg, expected_fields):
    """
    מפצלת את שדה הנתונים לרשימת פרמטרים ע"י התו המפריד

    :param:
        msg (str): שדה נתונים
        expected_fields (ind): מספר הפרמטרים הצפויים בשדה הנתונים

    :return:
        ERROR_RETURN: אם קרתה תקלה
        list: רשימת הפרמטרים
    """
    if msg.count(DATA_DELIMITER) != expected_fields - 1:
        return ERROR_RETURN

    return msg.split(DATA_DELIMITER)


def join_data(msg_fields):
    """
    מצרפת את כל הפרמטרים לשדה נתונים אחד ע"י התו המפריד

    :param:
        msg_fields (list): רשימה של פרמטרים

    :return:
        str: שדה נתונים בפורמט הפרוטוקול
    """
    return reduce(lambda x, y: f"{x}{DATA_DELIMITER}{y}", msg_fields)
