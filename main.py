def calculate_class_averages(classrooms):
    # create result dictionary to return
    # probably use for loop to get each class and students
    # create variable to sum all scores
    # loop thrhough students and get each grade and add them to the sum variable.
    # average divide sum by number of scores
    # add k/v pair into fesult dict (class:average_score)
    class_averages = {}
    # if no student
    # set average to 0
    for classroom, students in classrooms.items():
        if not students:
            class_averages[classroom] = 0
            continue
        scores = 0
        num_grades = 0

        for grades in students.values():
            for grade in grades:
                scores += grade
                num_grades += 1

        avg = scores/num_grades
        class_averages[classroom] = avg
    return class_averages

    # pass


# # {
#     "Math": {
#         "Alice": [85, 90, 78],
#         "Bob": [72, 88, 91],
#         "Charlie": [95, 100, 92]
#     },
#     "Science": {
#         "Alice": [80, 85, 88],
#         "Bob": [78, 82, 85],
#         "Diana": [90, 91, 89]
#     },
#     "History": {
#         "Charlie": [70, 75, 80],
#         "Diana": [88, 92, 84]
#     }


# }
# {
#     "Math": 88.17,
#     "Science": 85.67,
#     "History": 81.5
# }
