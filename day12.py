class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName, lastName, idNum)
        self.scores = scores
        
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function 
    def calculate(self):
        total= sum(self.scores) / len(self.scores)

        if total >= 90 and total <= 100: 
            return 'O'
        elif total < 90 and total >= 80: 
            return 'E'
        elif total < 80 and total >= 70: 
            return 'A'
        elif total < 70 and total >= 55: 
            return 'P'
        elif total < 55 and total >= 40: 
            return 'D'
        elif total < 40: 
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

# Heraldo Memelli 8135627
# 2
# 100 80