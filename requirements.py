submissions_list = [
    {
        "quizName": "Slope Quiz",
        "quizModule": "Math",
        "quizScore": 95,
        "studentID": 147,
        "studentName": "Maria",
        "submissionDate": "09-05-2025",
    },
    {
        "quizName": "Linear Equations Quiz",
        "quizModule": "Math",
        "quizScore": 98,
        "studentID": 185,
        "studentName": "Laura",
        "submissionDate": "09-04-2025",
    },
    {
        "quizName": "World War I Quiz",
        "quizModule": "History",
        "quizScore": 89,
        "studentID": 196,
        "studentName": "David",
        "submissionDate": "09-10-2025",
    },
    {
        "quizName": "Biology Quiz",
        "quizModule": "Science",
        "quizScore": 92,
        "studentID": 136,
        "studentName": "Richard",
        "submissionDate": "09-12-2025",
    },
    {
        "quizName": "Chemistry Quiz",
        "quizModule": "Science",
        "quizScore": 85,
        "studentID": 125,
        "studentName": "John",
        "submissionDate": "09-12-2025",
    },
    {
        "quizName": "American History Quiz",
        "quizModule": "History",
        "quizScore": 95,
        "studentID": 147,
        "studentName": "Maria",
        "submissionDate": "09-10-2025",
    },
]


def filter_by_date(date, submissions_list):
    """
    Filters submissions by date when given a date and a list
    Returns an empty list when no data is found
    """
    return [
        student for student in submissions_list if student["submissionDate"] == date
    ]


def filter_by_student_id(student_id, submissions_list):
    """
    Filters data by student ID when given a student ID and a list
    Returns an empty list if no data is found
    """
    return [
        student for student in submissions_list if student["studentID"] == student_id
    ]


def find_unsubmitted(date, student_name, submissions_list):
    """
    Given a date and a list of names,
    this function returns a list of those students who have not completed a quiz
    on the given date
    """
    students_who_submitted = [
        student["studentName"]
        for student in submissions_list
        if student["submissionDate"] == date
    ]
    not_submitted = [
        student for student in student_name if student not in students_who_submitted
    ]
    return not_submitted


def get_average_score(submissions_list):
    """
    Returns the average score for all quizes
    """
    sum_of_scores = sum(student["quizScore"] for student in submissions_list)
    return round((sum_of_scores / len(submissions_list)), 2)


def get_average_score_by_module(submissions_list):
    """
    Returns the name of the module followed by the average score for that particular module
    """
    scores_by_module = {}
    total_quizes_by_module = {}
    for submission in submissions_list:
        quiz_module = submission["quizModule"]
        quiz_score = submission["quizScore"]
        if quiz_module not in scores_by_module:
            scores_by_module[quiz_module] = 0
            total_quizes_by_module[quiz_module] = 0
        scores_by_module[quiz_module] += quiz_score
        total_quizes_by_module[quiz_module] += 1

    module_average = {}
    for quiz_module in scores_by_module:
        module_average[quiz_module] = round(
            scores_by_module[quiz_module] / total_quizes_by_module[quiz_module], 2
        )
    return module_average
