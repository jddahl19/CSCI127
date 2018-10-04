# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator
# Jesse Dahl
# Last Modified: September 25, 2018
# ---------------------------------------
"""
This program takes the number of classes the user is taking, as well as their grades and credits for each course
and it calculates their GPA using their inputed data, along with a predetermined grading scale.

*This program is very suboptimal in parts, especially the long ass for loop that determines the value for the inputted
 letter grades. I had to finish this program in a time crunch of 2 hours. Oops.
"""
# ---------------------------------------

def main():
    #Below creates empty lists in which the users information will be added to
    courses = []
    grades = []
    credits = []

    numberCourses = int(input("Enter the number of courses you are taking: ")) #Prompts the user to enter number of courses

    for i in range(numberCourses): #Go through this loop for as many times as the user entered above in "numberCourses"
        courses.append(i+1) #adds the number the loop is on to the "courses" list

    for i in range(len(courses)): #Go through this loop as many times as numbers there are in list "courses"
        print() #Adds a space between print statements for each loop
        getGrade = input("Enter grade for course %s : " %(courses[i])) #Prompts the user to enter their grade for the respected course
        grades.append(getGrade) #Adds that grade to the list "grades"
        getCredits = int(input("Enter credits for course %s : " %(courses[i]))) #Prompts the user to enter an integer respresenting the number of credits for the respected course
        credits.append(getCredits) #Adds that integer to the list "credits"
        print() #Does the same as the previous print() statement

    translate(grades, credits, courses) #Calls the translate function with parameters as the lists "grades", "credits", and "courses"

def translate(grades, credits, courses):
    #Creates empty lists
    gradeValue = []
    gradeCredit = []

    #Creates variables with valules of 0
    total = 0
    totalCred = 0

    #Unnecesarily long for loop that checks each element in list "grades" and based on the element in the list, a value for that grade will be added to the list "gradeValue"
    for element in grades:
        if element == "A" or element == "a":
            gradeValue.append(4.0)
        elif element == "A-" or element == "a-":
            gradeValue.append(3.7)
        elif element == "B+" or element == "b+":
            gradeValue.append(3.3)
        elif element == "B" or element == "b":
            gradeValue.append(3.0)
        elif element == "B-" or element == "b-":
            gradeValue.append(2.7)
        elif element == "C+" or element == "c+":
            gradeValue.append(2.3)
        elif element == "C" or element == "c":
            gradeValue.append(2.0)
        elif element == "C-" or element == "c-":
            gradeValue.append(1.7)
        elif element == "D+" or element == "d+":
            gradeValue.append(1.3)
        elif element == "D" or element == "d":
            gradeValue.append(1.0)
        elif element == "F" or element == "f":
            gradeValue.append(0.0)

    #References the empty list "gradeCredit" and adds sublists within the list with each sublist containing the values for "gradeValues" and "credits"
    gradeCredit.extend([list(a) for a in zip(gradeValue, credits)])

    for i in gradeCredit: #Loops through each sublist in list "gradeCredit"
        total+=(i[0]*i[1]) #Multiplies the first and second elements in each sublist and adds the total to variable 'total'
        totalCred += (i[1]) #Adds the credits in each sublist and adds that total to variable "totalCred"
    gpa = (total/totalCred) #Calculates the gpa


    print("Your GPA is: {:.2f}".format(gpa)) #formats the gpa to round to 2 decimal places and prints it

main() #calls function main()