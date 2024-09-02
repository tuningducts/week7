from os import system
from time import sleep
room_numbers = {"csc101" : "3004","csc102" : "4501", "csc103" : "6755","net110" : "1244", "com241" : "1411"}
instructors = {"csc101" : "Haynes","csc102" : "Alvarado", "csc103" : "Rich","net110" : "Burke", "com241" : "Lee"}
meeting_times = {"csc101" : "8:00 am","csc102" : "9:00 am", "csc103" : "10:00 am","net110" : "11:00 am", "com241" : "1:00 pm"}


def course_lookup():
    """take user input check if it is a valid course and print details about course"""
    system('clear')
    course_number = input("Enter Course Number: ").lower()
    if course_number in room_numbers.keys():
        message = f"""
Course Number: {course_number}
Room Number: {room_numbers.get(course_number)}
Intructor: {instructors.get(course_number)}
Meeting Time: {meeting_times.get(course_number)}
"""
        print(message)
        return_to_menu()
        
    else:
        print(f"{course_number} not found please enter a valid course number")
        sleep(2)
    
def list_courses():
    """lists available course"""
    system('clear')
    print("list of available courses:")
    for key in room_numbers.keys():
        print(key)
    return_to_menu()
    

def return_to_menu():
    """waits for user to press any key"""
    return_to_menu = input("Press Any Key to Return to Main Menu")

def menu():
    system('clear')
    menu_message = f"""Course Lookup Menu
    1 - Look up course details
    2 - List courses
    q - exit
    """
    print(menu_message)
    selection = input("Select Menu Item: ").lower()
    if selection == "1":
        course_lookup()
        menu()
    elif selection == "2":
        list_courses()
        menu()
    elif selection == "q":
        print("Have a great day!")
        exit
    else:
        print("invalid selection enter 1,2, or q")
        sleep(2)
        menu()


if __name__ == "__main__":
    menu()
