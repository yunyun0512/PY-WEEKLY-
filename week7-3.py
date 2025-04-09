class IndividualGradeError(Exception):
    def __init__(self,grade):
        self.grade=grade
        super().__init__(f"成绩无效:{grade}")
    
class Student:
    def __init__(self,name):
        self.name=name
        self.grades=[]
    def add_grade(self,grade):
        if grade<0 or grade>100:
            raise IndividualGradeError(grade)
        self.grades.append(grade)
    def total_grade(self):
        return sum(self.grades)
    def average_grade(self):
        if len(self.grades)==0:
            return 0
        else:
            return self.total_grade()/len(self.grades)
        
if __name__=="__main__":
    student=Student(input())
    grades=list(map(int,input().split()))
    for grade in grades:
        try:
            student.add_grade(grade)
        except IndividualGradeError as e:
            print(e)
    print(f"总成绩:{student.total_grade()},平均成绩:{student.average_grade():.1f}")