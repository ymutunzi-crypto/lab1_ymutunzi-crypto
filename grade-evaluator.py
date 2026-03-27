import csv
import sys
import os

def load_csv_data():
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    print("\n--- Processing Grades ---")
    
    # a) Check if all scores are percentage based (0-100)
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"Error: Invalid score {item['score']} for {item['assignment']}. Scores must be between 0 and 100.")
            return

    # b) Validate total weights
    total_weight = 0
    summative_weight = 0
    formative_weight = 0
    
    for item in data:
        total_weight += item['weight']
        if item['group'].strip().lower() == 'summative':
            summative_weight += item['weight']
        elif item['group'].strip().lower() == 'formative':
            formative_weight += item['weight']
            
    if total_weight != 100:
        print(f"Error: Total weight is {total_weight}, but must be exactly 100.")
        return
    if summative_weight != 40:
        print(f"Error: Summative weight is {summative_weight}, but must be exactly 40.")
        return
    if formative_weight != 60:
        print(f"Error: Formative weight is {formative_weight}, but must be exactly 60.")
        return

    # c) Calculate the Final Grade and GPA
    total_grade = 0
    formative_earned = 0
    summative_earned = 0
    
    for item in data:
        earned_points = item['score'] * (item['weight'] / 100)
        total_grade += earned_points
        
        if item['group'].strip().lower() == 'summative':
            summative_earned += earned_points
        elif item['group'].strip().lower() == 'formative':
            formative_earned += earned_points
            
    gpa = (total_grade / 100) * 5.0
    formative_percentage = (formative_earned / 60) * 100
    summative_percentage = (summative_earned / 40) * 100

    print(f"Total Grade: {total_grade:.2f}/100")
    print(f"GPA: {gpa:.2f} / 5.0")
    print(f"Formative Category Score: {formative_percentage:.2f}%")
    print(f"Summative Category Score: {summative_percentage:.2f}%")

    # d) Determine Pass/Fail status
    passed = formative_percentage >= 50 and summative_percentage >= 50

    # e) Check for failed formatives and find highest weight
    failed_formatives = [item for item in data if item['group'].strip().lower() == 'formative' and item['score'] < 50]
            
    resubmission_options = []
    if failed_formatives:
        highest_weight = max(item['weight'] for item in failed_formatives)
        resubmission_options = [item['assignment'] for item in failed_formatives if item['weight'] == highest_weight]

    # f) Print the final decision
    if passed:
        print("\nFinal Decision: PASSED")
    else:
        print("\nFinal Decision: FAILED")
        
    if not passed and resubmission_options:
        print(f"Recommended Resubmission(s) (Highest Weight Failed Formative): {', '.join(resubmission_options)}")

if __name__ == "__main__":
    course_data = load_csv_data()
    if course_data:
        evaluate_grades(course_data)
