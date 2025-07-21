def load_users_database():
    """
    טוענת את בנק המשתמשים מבסיס הנתונים

    :returns:
        dict: מילון המשתמשים
    """
    users_db = {
        "haim": {"password": "111", "score": 100, "questions_asked": []},
        "david": {"password": "111", "score": 50, "questions_asked": []},
        "avi": {"password": "111", "score": 200, "questions_asked": []},
    }

    return users_db
