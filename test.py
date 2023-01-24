import time , datetime
database = []
students_marked = 0
registered_no_of_students = 10
lecture_time = "10:00"

# Functions
#################################################################################
def welcome():
    print("Welcome to Introduction to Computer Programming Lecture")
    print(f"*****Lecture starts at {lecture_time}*****")
    print("Please Ensure you mark your attendance")
    print("Remain attentive to your lecturer and stay quiet")

def load(message):
    # for i in range(1,6):
    #     time.sleep(1)
    #     print(f"Loading Program.{'.'*i}")
    loading_dots = [message + "."*i for i in range(1,6)]

    for dot in loading_dots:
        time.sleep(1)
        print(dot)

def sep():
    sep = "-" * 50
    print(sep)

def logic():
    current_time = datetime.datetime.now().time()
    current_date = datetime.datetime.now().date()
    hardcoded_time = datetime.datetime.strptime(lecture_time,"%H:%M").time()
    status = None

    # print(type(current_time), type(hardcoded_time))
    if current_time < hardcoded_time:
        status = "Early" 
        database.append({
            student[1]: {
                "time_arrived": current_time,
                "date": current_date,
                "punctuality_status": status 
            }
        })
        
        return True 

    else: 
        status = "Late"
        return False
def lecturer_admin_dashboard():
    print("I am a lecturer")
#################################################################################

# Main Program Function
def main(logging_status=False):
    global students_marked, student
    logging_status = False
    while students_marked < registered_no_of_students - 1:
        students_marked = len(database)

        if logging_status == False:
            user = input("Who are you logging in as??\n1.Lecturer\t2.Student\nPlease Enter either 1 or 2: ")
            if user == 1:
                lecturer_admin_dashboard()
            elif user == 2:
                main(True)

        if logging_status:
            sep()
            welcome()
            sep()
            load("Loading Program.")
            # time.sleep(5)
            student = input("Enter your name and registration number \n[Sample Entry: Micah Shallom Bawa,U18CO1034]\nPress 'q' to quit: ").split(',')
            if student[0] == "q":
                print("Please dont skip the attendance.\n \
                    Enter your details this time")
                sep()
                time.sleep(2)
                main(False)
            sep()
            logic_result = logic()
            time.sleep(4)
            load("Processing_Punctuality_Status.")
            if logic_result:
                sep()
                print("You were right on time 🎉🎉🎉🎊🎊🎊🎊🎊.\nGo and have your seat 🧑‍🎓📚📚📚")
            else:
                sep()
                print("Please get out of my class.❌❌⚔️⚔️⚔️⚔️⚔️☠️☠️")
            print("NEXT STUDENT PLEASE⏭️⏭️⏭️⏭️⏭️")
            time.sleep(3)
            load("Initializing Next Student.")
            # print(logic_result)
            
            # print(students_marked,database)
main()



if __name__ == "__main__" :
    pass