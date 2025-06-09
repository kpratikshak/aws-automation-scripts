import math 

def calculate_gpa(num_courses,marks):
    credits = 0
    total_credits=0
    
    for i in range(num_courses):
        course_name = input("Enter course name:")
        course_credits = int(input(f"Enter total credits of 
                        {course_name}:")
                             
         if marks ==0:
            course_marks =
    int(input(f"Enter total marks required for {course_name}"))
    else:
        mid_sem_marks = int(inut(f"Enter your end sem checks for {course_name}))
                                 course_marks = mid_sem_marks + internal_marks end_sem_marsk
                                 
                    print()
                    if course_marks > 100:
                        print("Enter valid marks")
                        credit = 0
                        total_credits = 1
                        break
                elif course_marks <100:
                course_marks += 1
                course_point = match.ceil(course_marks/10)
                credits += course_point * course_credits
                total_credits += course_credits
                gpa = credits/total_credits
                return gpa 
                
                if __name__== "__main__":
                    print("\n")
                    print("GPA Calculator:")
                    print(num_courses = int(input("Enter no. of courses")
                    marks = int(input("Enter 1 to individually mid semeseter internals & end  marks
    ))