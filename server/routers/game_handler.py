import random
from protocol import chatlib

import global_vars

from network.error import send_error
from network.socket_utils import build_and_send_message


def handle_question_message(conn, username):
    """
    מבצע טיפול בבקשת 'תן שאלה' שנשלחה לשרת דרך צינור הלקוח

    :param:
        conn (socket): צינור לקוח מחובר
    """

    questions_not_asked = [q for q in global_vars.questions.keys() if q not in global_vars.users[username]["questions_asked"]]

    if not questions_not_asked:
        build_and_send_message(conn, chatlib.PROTOCOL_SERVER["no_question_msg"], "")
        return

    q_id = random.choice(questions_not_asked)
    data_rsp = chatlib.join_data([q_id, global_vars.questions[q_id]["question"]] + global_vars.questions[q_id]["answers"])

    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["your_question_msg"], data_rsp)


def handle_answer_message(conn, username, data):
    """
    מבצע טיפול בבקשת 'שלח תשובה' שנשלחה לשרת דרך צינור הלקוח

    :param:
        conn (socket): צינור לקוח מחובר
        username (str): שם משתמש הלקוח המחובר
        data (str): שדה הנתונים
    """

    data_split = chatlib.split_data(data, 2)  # 2 because: question_id and choice_answer
    question_id = int(data_split[0])

    if question_id in global_vars.users[username]["questions_asked"]:
        send_error(conn, "You have already answered this question.")
        return

    choice_answer = data_split[1]
    correct_answer = str(global_vars.questions[question_id]["correct"])

    if choice_answer == correct_answer:
        build_and_send_message(conn, chatlib.PROTOCOL_SERVER["correct_answer_msg"], "")
        global_vars.users[username]["score"] += 5
        global_vars.users[username]["questions_asked"].append(question_id)
    else:
        build_and_send_message(conn, chatlib.PROTOCOL_SERVER["wrong_answer_msg"], correct_answer)
