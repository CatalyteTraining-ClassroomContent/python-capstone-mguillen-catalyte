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


# # def filter_by_date(date, submissions_list):
# #     """
# #     Filters submissions by date when given a date and a list
# #     Returns an empty list when no data is found
# #     """
# #     return [
# #         student for student in submissions_list if student["submissionDate"] == date
# #     ]


# # print(filter_by_date("09-01-2025", submissions_list))


# # def filter_by_student_id(student_id, submissions_list):
# #     """
# #     Filters data by student ID when given a student ID and a list
# #     Returns an empty list if no data is found
# #     """
# #     return [
# #         student for student in submissions_list if student["studentID"] == student_id
# #     ]


# # print(filter_by_student_id(123, submissions_list))


# def find_unsubmitted(date, student_name, submissions_list):
#     students_who_submitted = [
#         student["studentName"]
#         for student in submissions_list
#         if student["submissionDate"] == date
#     ]
#     not_submitted = [
#         student for student in student_name if student not in students_who_submitted
#     ]
#     return not_submitted


# # print(find_unsubmitted("09-12-2025", ["John", "Richard"], submissions_list))


# def get_average_score(submissions_list):
#     sum_of_scores = sum(student["quizScore"] for student in submissions_list)
#     return round((sum_of_scores / len(submissions_list)), 2)


# print(get_average_score(submissions_list))


def get_average_score_by_module(submissions_list):
    scores_by_module = {}
    total_quizes_by_module = {}
    for submission in submissions_list:
        module = submission["quizModule"]
        score = submission["quizScore"]
        scores_by_module[module] += score
        total_quizes_by_module[module] += 1

    module_average = {}
    for module in scores_by_module:
        module_average[module] = round(
            scores_by_module[module] / total_quizes_by_module[module], 2
        )
    return module_average


print(get_average_score_by_module(submissions_list))
