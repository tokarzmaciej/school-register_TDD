import unittest
from src.subjects import Subjects
from parameterized import parameterized, parameterized_class


class SubjectsDeleteParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Subjects()

    @parameterized.expand([
        (5, "Piotr", "Fantazja", "math", {'subjects': {'history': {}, 'art': {}}, 'remarks': {}}),
    ])
    def test_delete_subjects_positive_expand(self, id, name, surname, name_subject, expected):
        self.assertEqual(self.tmp.deleteSubject(id, name, surname, name_subject), expected)

    @parameterized.expand([
        (10, "Ania", "Zegan", "english", "There_is_not_such_student"),
        (5, "Piotr", "Fantazja", "geography", "Student_not_have_this_subject")
    ])
    def test_delete_subjects_exceptions_expand(self, id, name, surname, name_subject, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.deleteSubject, id, name, surname, name_subject)

    @parameterized.expand([
        (5, "Piotr", "Fantazja", 1234, "Bad_type_subject_name"),
    ])
    def test_delete_subjects_type_errors(self, id, name, surname, name_subject, expected):
        self.assertRaisesRegex(TypeError, expected, self.tmp.deleteSubject, id, name, surname, name_subject)

    @parameterized_class(("id", "name", "surname", "name_subject", "expected"), [
        (5, "Piotr", "Fantazja", "math", {'subjects': {'history': {}, 'art': {}}, 'remarks': {}}),

    ])
    class SubjectsDeleteParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Subjects()

        def test_delete_subjects_positive_class(self):
            self.assertEqual(self.tmp.deleteSubject(self.id, self.name, self.surname, self.name_subject), self.expected)


if __name__ == '__main__':
    unittest.main()
