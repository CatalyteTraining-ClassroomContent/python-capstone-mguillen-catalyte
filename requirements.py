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


def filter_by_date(date, submission):
    """
    Filters submissions by date
    """
    filtered_dates = []
    for submission_date in submissions_list:
        if submission_date["submissionDate"] == date:
            filtered_dates.append(submission_date)
    return filtered_dates


# print(filter_by_date("09-10-2025", submissions_list))


def filter_by_student_id(student_id, submission):
    """
    Filters data by student ID
    """
    filtered_id = []
    for student in submissions_list:
        if student["studentID"] == student_id:
            filtered_id.append(student)
    return filtered_id


# print(filter_by_student_id(147, submissions_list))


# def find_unsubmitted():

# def get_average_score():

# def get_average_score_by_module():
