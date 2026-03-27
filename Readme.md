# Lab 1: Grade Evaluator & Archiver

This repository contains a Python application to evaluate student grades and a Bash script to automate the archiving of the grade records.

## Files Included
- `grade-evaluator.py`: Python script that reads `grades.csv`, validates scores and weights, calculates GPA, and determines pass/fail status.
- `organizer.sh`: Bash script that moves the current `grades.csv` into an `archive/` folder with a timestamp and creates a fresh, empty `grades.csv`.

## How to Run

### 1. Python Grade Evaluator
Ensure you have Python 3 installed. Run the following command in your terminal:
`python3 grade-evaluator.py`
When prompted, type `grades.csv` and press Enter.

### 2. Bash Shell Organizer
Execute the script to archive your files:
`./organizer.sh`
This will move `grades.csv` to the `archive` folder, create a new empty `grades.csv`, and log the action in `organizer.log`.
