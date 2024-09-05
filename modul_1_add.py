grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
abc_students = sorted(students)
av_grade_1 = sum(grades[0]) / len(grades[0])
av_grade_2 = sum(grades[1])  / len(grades[1])
av_grade_3 = sum(grades[2])  / len(grades[2])
av_grade_4 = sum(grades[3])  / len(grades[3])
av_grade_5 = sum(grades[4]) / len(grades[4])
av_grades_for_all = {abc_students[0]: av_grade_1,
                     abc_students[1]: av_grade_2,
                     abc_students[2]: av_grade_3,
                     abc_students[3]: av_grade_4,
                     abc_students[4]: av_grade_5}
print(av_grades_for_all)