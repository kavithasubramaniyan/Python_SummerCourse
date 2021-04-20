class Student:

    Scores = {}
    Scores1={}
    Scores2={}
    
    # initializing the constructor method

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def getScores(self):

        answer_key = []
       
        answer_key = [line.strip() for line in open("answers.txt", 'r')]
        
        student_answers = []
       
        student_answers = [line.strip().split(',') 
                           for line in open("data.txt", 'r')]
        
       
        total_score = 100
             
        Student.Scores[self.getName()] = total_score        
        Student.Scores1[self.getName()] = self.getGrade()        
        return answer_key,student_answers

    def getName(self):
        return self.name.title()
    def getGrade(self):
        return self.grade
    def getFinalGrade(self,answer_key,student_answers):
        answer_length=len(answer_key)
        student_length=len(student_answers)
        elem_to_find=self.getName()
        
        names_list = [ sublist[0].lower() for sublist in student_answers]
        #print("names-----:",names_list)
        #res1 = any(elem_to_find.lower() in names_list)
        pos=[[i,j] for i in range(len(student_answers)) for j in range(len(student_answers[i])) if student_answers[i][j].lower()==elem_to_find.lower()]
                   
        
        if elem_to_find.lower() in names_list:

            i=pos[0][0]
            k=1
                
            total_score=100
              
            for j in range(len(answer_key)):    
                if(student_answers[i][k]==answer_key[j]):
                        
                        total_score1=total_score
                        
                else:
                        
                        total_score1=total_score-10
                        
                        total_score=total_score1
                           
                j=j+1
                k=k+1           
            
                  
            Student.Scores2[elem_to_find] = total_score1
        else:
            total_score1=100
            Student.Scores2[elem_to_find]=total_score1
    
       
    
    @staticmethod
    def sortDict():
        return sorted(Student.Scores.items())
    
    def sortDict1():
        return sorted(Student.Scores1.items())
    
    def sortDict2():
        
        return sorted(Student.Scores2.items())
    #---end the class definition#

student_objs = [

    Student('Sammy Student', 65),
    Student('Betty sanchez', 45),
    Student('Alice brown', 100),
    Student('tom Schulz', 50),
]

name=input("Enter the student name:")
mark=int(input("Enter the score:"))
grade=input("Enter the answers:")
student_objs.append(Student(name,mark))
with open("data.txt", "a") as myfile:
        line = '\n'
        line1=","
        myfile.write(line+name+line1+grade)
        myfile.close()
        #lines = filter(lambda x: x.strip(), lines)
#print("File data written")
student_objs.append(Student(name,mark))

for index in range(0,len(student_objs)):
    
    answer_key,student_answers =student_objs[index].getScores()
    #print(answer_key,student_answers)
    student_objs[index].getFinalGrade(answer_key,student_answers)


sortList = Student.sortDict()

sortList1 = Student.sortDict1()

sortList2 = Student.sortDict2()


avg=[] 
grade_range=[]
for  (k1,v1),(k2,v2) in zip(sortList1,sortList2):
    avg1=(v1+v2)/2
    avg.append(avg1)
    grade=abs(v1-v2)
    grade_range.append(grade)
    #print (k, v)
    print(k1,"has old score:",v1)
    print (k2,"has new score:" ,v2)
    print("Average Grade:",(v1+v2)/2)
    print("Grade Range:",abs(v1-v2))
#print(avg)
#print(grade_range)
print("Overall Average Grade:",sum(avg)/len(avg))
print("Overall Average Grade Range:",sum(grade_range)/len(grade_range))
