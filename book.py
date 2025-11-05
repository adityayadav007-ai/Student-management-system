
# GradeBook Analyzer
# Author: [Aditya yadav]
# roll n0: 2501420020
# Date: 2025-11-05
# Title: Quick Student Grade Analysis Tool
# -------------------------------------------------------------

import statistics
MARKS = {}
GRADES = {}



def display_menu():
    """Prints the welcome header and menu options."""
    print("\n" + "="*45)
    print("  GradeBook Analyzer Tool ")
    print("="*45)
    print("1. Enter Student Marks")
    print("2. Run Analysis & View Report")
    print("3. Exit Program")
    print("="*45)



def data_entry():
    """Collects student names and marks from the user."""
    MARKS.clear() 
    GRADES.clear()

    while True:
        try:
            num_students = int(input("How many students are in the class? "))
            if num_students > 0:
                break
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("\n--- Start Data Input ---")
    for i in range(num_students):
        name = input(f"Enter name for student {i+1}: ").strip().title()
        while True:
            try:
                mark = int(input(f"Enter mark (0-100) for {name}: "))
                if 0 <= mark <= 100:
                    MARKS[name] = mark
                    break
                else:
                    print("Mark must be between 0 and 100.")
            except ValueError:
                print("Invalid mark. Enter a number.")

    print(f" Successfully stored data for {len(MARKS)} students.")



def run_statistics():
    """Calculates and displays mean, median, max, and min scores."""
    if not MARKS:
        return

    scores = list(MARKS.values())

    # Helper functions and calculations
    average = sum(scores) / len(scores)
    median = statistics.median(scores)
    max_score = max(scores)
    min_score = min(scores)

    print(" Class Statistics ---")
    print(f"Average Score (Mean):  {average:.2f}")
    print(f"Median Score:          {median:.2f}")
    print(f"Highest Score (Max):   {max_score}")
    print(f"Lowest Score (Min):    {min_score}")



def assign_grade(mark):
    """Assigns letter grade based on mark using if-elif-else."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else: # mark < 60
        return "F"

def analyze_grades():
    """Assigns grades to all students and counts distribution."""
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for name, mark in MARKS.items():
        grade = assign_grade(mark)
        GRADES[name] = grade
        grade_counts[grade] += 1

    print(" Grade Distribution ---")
    print(f"A (90+): {grade_counts['A']} students")
    print(f"B (80-89): {grade_counts['B']} students")
    print(f"C (70-79): {grade_counts['C']} students")
    print(f"D (60-69): {grade_counts['D']} students")
    print(f"F (<60): {grade_counts['F']} students")



def filter_pass_fail():
    """Uses list comprehensions to separate passing (>=60) and failing (<60) students."""
    

    passed_students = [name for name, mark in MARKS.items() if mark >= 60]
  
    failed_students = [name for name, mark in MARKS.items() if mark < 60]

    print(" Pass/Fail Summary (Pass >= 60) ")
    print(f"Passed ({len(passed_students)}): {', '.join(passed_students) if passed_students else 'None'}")
    print(f"Failed ({len(failed_students)}): {', '.join(failed_students) if failed_students else 'None'}")
def display_results_table():
    """Prints a neatly formatted final report table."""
    
    print(" Detailed Student Report ")
    if not MARKS:
        name_width = 10
    else:
        name_width = max(len(name) for name in MARKS.keys()) + 2 
    print(f"{'Name':<{name_width}} {'Marks':>5} {'Grade':>5}")
    print("-" * (name_width + 12)) 
    for name, mark in MARKS.items():
        grade = GRADES.get(name, 'N/A')
        print(f"{name:<{name_width}} {mark:>5} {grade:>5}")
    print("-" * (name_width + 12))


def run_full_analysis():
    """Runs all analysis tasks if data is present."""
    if not MARKS:
        print(" Please enter student data first (Option 1).")
        return
    run_statistics()        
    analyze_grades()        
    filter_pass_fail()      
    display_results_table() 
def main_loop():
    """The main control loop for the program."""
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            data_entry()
        elif choice == '2':
            run_full_analysis()
        elif choice == '3':
            print(" Exiting GradeBook Analyzer. Have a great day!")
            break
        else:
            print(" Invalid choice. Please try again.")
if __name__ == "__main__":
    main_loop()