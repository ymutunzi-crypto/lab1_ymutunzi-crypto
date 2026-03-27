#!/bin/bash

# Check if archive directory exists, if not, create it
if [ ! -d "archive" ]; then
    mkdir archive
fi

# Generate timestamp
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# Define filenames
ORIGINAL_FILE="grades.csv"
NEW_FILENAME="grades_${TIMESTAMP}.csv"

# Check if grades.csv exists before trying to move it
if [ -f "$ORIGINAL_FILE" ]; then
    # Rename and move to archive
    mv "$ORIGINAL_FILE" "archive/$NEW_FILENAME"

    # Create a new, empty grades.csv
    touch "$ORIGINAL_FILE"

    # Log the action
    echo "Archived on: $(date). Original: $ORIGINAL_FILE -> Archived as: archive/$NEW_FILENAME" >> organizer.log

    echo "Archival complete. Check organizer.log for details."
else
    echo "Error: $ORIGINAL_FILE does not exist in the current directory."
fi
