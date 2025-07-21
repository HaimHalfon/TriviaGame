import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from network.client_socket import connect, disconnect
from logic.login import login, logout
from logic.question import play_question
from logic.score import get_score, get_high_score
from logic.logged_user import get_logged_users


def main():
    conn = connect()
    login(conn)

    while True:
        print("=" * 35, "Play a Trivia question - press 1", "Get my score - press 2", "Get high score - press 3", "Get logged users - press 4", "Quit - press 0", "=" * 35, sep="\n")

        inp = input()

        if inp == "1":
            play_question(conn)
        elif inp == "2":
            get_score(conn)
        elif inp == "3":
            get_high_score(conn)
        elif inp == "4":
            get_logged_users(conn)
        elif inp == "0":
            logout(conn)
            break

    disconnect(conn)


if __name__ == "__main__":
    main()
