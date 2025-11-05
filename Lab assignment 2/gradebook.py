"""
GradeBook Analyzer
Name: Shamaya Dhariwal 
Roll No.: 2501410020
Course: Programming for Problem Solving using Python

Description:
A command-line tool to analyze and report student grades.
Supports manual entry or CSV import, statistical analysis,
grade assignment, and formatted summary output.
"""

import csv
import statistics

print("=== Welcome to GradeBook Analyzer ===")

def manual_entry():
    data = {}
    print("Enter student names and marks (type 'done' to stop)")
    while True:
        name = input("Name: ")
        if name.lower() == 'done':
            break
        try:
            marks = float(input("Marks: "))
            data[name] = marks
        except:
            print("Please enter a number for marks!")
    return data

def load_csv():
    data = {}
    filename = input("Enter CSV file name (with .csv): ")
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)   # skip header
            for row in reader:
                if len(row) >= 2:
                    data[row[0]] = float(row[1])
    except Exception as e:
        print("Error reading file:", e)
    return data

def avg(m):
    return sum(m.values()) / len(m)

def med(m):
    return statistics.median(m.values())

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

while True:
    print("\n1. Manual Entry")
    print("2. Load from CSV")
    print("3. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        marks = manual_entry()
    elif choice == "2":
        marks = load_csv()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice!")
        continue

    if not marks:
        print("No data found!")
        continue

    # stats
    print("\n--- Summary ---")
    print("Average:", round(avg(marks), 2))
    print("Median :", med(marks))
    print("Highest:", max(marks.values()))
    print("Lowest :", min(marks.values()))

    # grades
    grades = {}
    for n, m in marks.items():
        grades[n] = grade(m)

    dist = {"A":0,"B":0,"C":0,"D":0,"F":0}
    for g in grades.values():
        dist[g] += 1

    print("\nGrade distribution:")
    for k,v in dist.items():
        print(k, ":", v)

    # pass/fail
    passed = [n for n,m in marks.items() if m >= 40]
    failed = [n for n,m in marks.items() if m < 40]

    print("\nPassed:", ", ".join(passed))
    print("Failed:", ", ".join(failed))

    print("\nName\tMarks\tGrade")
    print("-"*25)
    for n,m in marks.items():
        print(f"{n}\t{m}\t{grades[n]}")

    again = input("\nDo you want to analyze again? (y/n): ")
    if again.lower() != 'y':
        print("Program ended.")
        break
