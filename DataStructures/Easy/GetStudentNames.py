import unittest

"""
Get Student Names
Create a function that takes a dictionary of
student names and returns a list of student names
in alphabetical order.

Examples
get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}) ➞ ["Becky", "John", "Steve"]

Notes
* Don't forget to return your result.
* If you get stuck on a challenge, find help in the Resources tab.
* If you're really stuck, unlock solutions in the Solutions tab.
"""

def get_student_names(students):
    return sorted(students.values())

class GetStudentNames(unittest.TestCase):
    def test_get_student_names(self):
        self.assertEqual(get_student_names({
        	"Student 1":"Steve",
        	"Student 2":"Becky",
        	"Student 3":"John"
        }), ["Becky", "John", "Steve"])

        self.assertEqual(get_student_names({
        	"Student 1":"Jacek",
        	"Student 2":"Ewa",
        	"Student 3":"Zygmunt",
        	"Student 4":"Tomek"
        }), ["Ewa", "Jacek", "Tomek", "Zygmunt"])


if __name__ == '__main__':
    unittest.main()
