'''Task Description #3: Refactoring Using Classes and Methods (Eliminating Redundant Conditional Logic)
Refactor a Python script that contains repeated if–elif–else grading logic by implementing a structured, object-oriented solution using a class and a method.
Problem Statement
The given script contains duplicated conditional statements used to assign grades based on student marks. This redundancy violates clean code principles and reduces maintainability.
You are required to refactor the script using a class-based design to improve modularity, reusability, and readability while preserving the original grading logic.
Mandatory Implementation Requirements
1.	Class Name: GradeCalculator
2.	Method Name: calculate_grade(self, marks)
3.	The method must:
o	Accept marks as a parameter.
o	Return the corresponding grade as a string.
o	The grading logic must strictly follow the conditions below:
	Marks ≥ 90 and ≤ 100 → "Grade A"
	Marks ≥ 80 → "Grade B"
	Marks ≥ 70 → "Grade C"
	Marks ≥ 40 → "Grade D"
	Marks ≥ 0 → "Fail"
      Note: Assume marks are within the valid range of 0 to 100.
4.	Include proper docstrings for:
o	The class
o	The method (with parameter and return descriptions)
5.	The method must be reusable and called multiple times without rewriting conditional logic.
• Given code:
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
marks = 72
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
Expected Output:
•	 Define a class named GradeCalculator.
•	Implement a method calculate_grade(self, marks) inside the class.
•	Create an object of the class.
•	Call the method for different student marks.
•	Print the returned grade values.

'''

class GradeCalculator:
    """
    A class to calculate grades based on student marks.
    """

    def calculate_grade(self, marks):
        """
        Calculate the grade based on the given marks.

        Parameters:
        marks (int): The marks obtained by the student (0-100).

        Returns:
        str: The grade corresponding to the marks.
        """
        if 90 <= marks <= 100:
            return "Grade A"
        elif marks >= 80:
            return "Grade B"
        elif marks >= 70:
            return "Grade C"
        elif marks >= 40:
            return "Grade D"
        elif marks >= 0:
            return "Fail"
        else:
            raise ValueError("Marks should be between 0 and 100.")
# Create an instance of the GradeCalculator class
grade_calculator = GradeCalculator()
# List of marks to calculate grades for
marks_list = [85, 72, 95, 60, 30]
# Calculate and print the grades for each mark
for marks in marks_list:
    grade = grade_calculator.calculate_grade(marks)
    print(f"Marks: {marks} - {grade}")
