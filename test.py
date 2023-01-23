import time

class_start_time = "9:00 AM"

while True:
    student_name = input("What is your name? ")
    student_arrival_time = input("What time did you arrive to class? (Format: HH:MM AM/PM) (Type 'q' to quit)")
    if student_arrival_time == 'q':
        break
    class_start_time_seconds = time.mktime(time.strptime(class_start_time, "%I:%M %p"))
    student_arrival_time_seconds = time.mktime(time.strptime(student_arrival_time, "%I:%M %p"))

    if student_arrival_time_seconds > class_start_time_seconds:
        print(f"{student_name}, you were late to class.")
    else:
        print(f"{student_name}, you were on time to class.")