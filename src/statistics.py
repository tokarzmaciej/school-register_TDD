from src.students import *


class Statistics(Students):

    def averageSubject(self, id, name_student, surname_student, name_subject):
        if self.keys.__contains__((str(id), name_student, surname_student)):
            keysSubjects = self.students[(str(id), name_student, surname_student)]["subjects"]
            if [*keysSubjects].__contains__(
                    name_subject):
                valuesSubject = keysSubjects[name_subject].values()
                if valuesSubject:
                    return "average" + " " + name_subject, sum(valuesSubject) / len(valuesSubject)
                else:
                    raise Exception("Do_not_have_marks")
            else:
                raise Exception("Student_not_have_this_subject")
        else:
            raise Exception("There_is_not_such_student")
