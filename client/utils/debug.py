from colorama import Fore, Style


def error_and_exit(error_msg):
    """
    מדפיסה הודעת שגיאה בצבע אדום ויוצאת מכל התכנית

    :param:
        error_msg (str): הודעה
    """
    print(f"{Fore.RED}{error_msg}{Style.RESET_ALL}")
    exit()


def debug_info(txt):
    """
    מדפיסה הודעת דיבוג בצבע כחול

    :param:
        txt (str): הודעה
    """
    print(f"{Fore.BLUE}{txt}{Style.RESET_ALL}")
