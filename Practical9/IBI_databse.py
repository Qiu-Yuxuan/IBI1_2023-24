class student:
    def __init__(self,name,major,code_portfolio_score,group_project_score,exam_score):
        self.name=name
        self.major=major
        self.code_portfolio_score=code_portfolio_score
        self.group_project_score=group_project_score
        self.exam_score=exam_score
    def present_detail(self):
        print('name:',self.name,', major:',self.major,', code portofolio score:',self.code_portfolio_score,', group project score:',self.group_project_score,', exam score',self.exam_score)
#example of how to call the function
person1= student ("Qiuyuxuan","BMI",84,68,78)
person1.present_detail() 