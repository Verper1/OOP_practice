# Calculating Student Results: Develop a class to accept a student's name and marks in three subjects,
# then calculate and display the total and average marks.


class Student_Results:
    def __init__(self, name: str, marks: list):
        self.marks = marks
        self.name = name

        print(self.calculating())

    def calculating(self):
        total_marks = len(self.marks)
        average_mark = sum(self.marks) / total_marks
        return f"Имя студента: {self.name}\nВсего отметок: {total_marks}\nСредняя арифметическая: {average_mark}"


bill = Student_Results("Валера", [5, 3, 4])

