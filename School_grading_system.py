# ================================================
# School Grading System
# Author/Owner: TheUltimateUsername5000 (GitHub)
# License: MIT (You are free to use, modify, and share,
#          but please give credit to the author.)
# ================================================

def get_grade(score):
    if 80 <= score <= 100:
        return "A"
    elif 70 <= score <= 79:
        return "B"
    elif 60 <= score <= 69:
        return "C"
    elif 45 <= score <= 59:
        return "D"
    elif 35 <= score <= 44:
        return "E"
    elif 0 <= score <= 34:
        return "F"
    else:
        return "Invalid"


def run():
    print("=== School Grading System ===")
    name = input("Enter student name: ")
    
    try:
        score = int(input("Enter student score (0-100): "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return
    
    if score < 0 or score > 100:
        print("❌ Score must be between 0 and 100.")
        return

    grade = get_grade(score)
    
    # Simple grade system
    remarks = {
        "A": "Excellent 🎉",
        "B": "Very Good 👍",
        "C": "Good 🙂",
        "D": "Fair 😐",
        "E": "Pass 😅",
        "F": "Fail ❌"
    }
    
    print("\n--- Result ---")
    print(f"Student: {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print(f"Remarks: {remarks.get(grade, '❓ Invalid grade')}")
    print("----------------")


# Auto-run the program
run()