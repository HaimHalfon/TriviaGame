from protocol import chatlib
from network.socket_utils import build_send_recv_parse
from utils.debug import error_and_exit


def play_question(conn):
    """
    שולחת בקשות 'תן שאלה' ו'קח תשובה' לשרת דרך צינור הלקוח

    :param:
        socket: צינור לקוח מחובר
    """
    msg_code, data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["get_question_msg"], "")

    if msg_code == chatlib.PROTOCOL_SERVER["your_question_msg"]:

        data_split = chatlib.split_data(data, 6)  # 6 because: id, quastion and 4 answers
        question_id = data_split[0]
        question_content = data_split[1]
        answer_options = data_split[2:]

        print(question_content)

        i = 1
        for ans in answer_options:
            print(f"({i}) {ans}")
            i += 1

        inp = 0
        while True:
            try:
                inp = int(input())
                break
            except ValueError:
                print("Numbers only! Try again.")
                continue

        msg_code, data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["send_answer_msg"], chatlib.join_data([question_id, inp]))

        if msg_code == chatlib.PROTOCOL_SERVER["correct_answer_msg"]:
            print("Very good :-) correct answer")
        elif msg_code == chatlib.PROTOCOL_SERVER["wrong_answer_msg"]:
            print(f"Oh no :-( wrong answer - The correct answer is ({data})")
        elif msg_code == chatlib.PROTOCOL_SERVER["error_msg"]:
            error_and_exit(data)
        else:
            print(data)

    elif msg_code == chatlib.PROTOCOL_SERVER["no_question_msg"]:
        print("No more questions - Game Over!")

    elif msg_code == chatlib.PROTOCOL_SERVER["error_msg"]:
        error_and_exit(data)
