def load_questions_database():
    """
    טוענת את בנק השאלות מבסיס הנתונים

    :returns:
        dict: מילון השאלות
    """
    questions_db = {
        2313: {
            "question": "How much is 2+2?",
            "answers": ["3", "4", "2", "1"],
            "correct": 2,
        },
        4122: {
            "question": "What is the capital of France?",
            "answers": ["Lion", "Marseille", "Paris", "Montpelier"],
            "correct": 3,
        },
        3421: {
            "question": "What color is the sun?",
            "answers": ["Blue", "Yellow", "Green", "Pink"],
            "correct": 2,
        },
        7632: {
            "question": "Which animal says 'meow'?",
            "answers": ["Dog", "Cow", "Cat", "Duck"],
            "correct": 3,
        },
        5274: {
            "question": "How many legs does a spider have?",
            "answers": ["4", "6", "8", "10"],
            "correct": 3,
        },
        6510: {
            "question": "What do we use to eat soup?",
            "answers": ["Fork", "Knife", "Spoon", "Hands"],
            "correct": 3,
        },
    }

    return questions_db
