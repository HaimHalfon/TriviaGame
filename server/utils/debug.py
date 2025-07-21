from colorama import Fore, Style


def debug_info(txt):
    """
    מדפיסה הודעת דיבוג בצבע כחול

    :param:
        txt (str): הודעה
    """
    print(f"{Fore.BLUE}{txt}{Style.RESET_ALL}")
