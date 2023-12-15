#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <N>"
    exit 1
fi

# Extract the value of N from the command line argument
N=$1

# Create a folder named DayN
folder_name="Day$N"
mkdir "$folder_name"

# Create dNp1.py inside the folder
touch "$folder_name/d${N}p1.py"

# Create dNp2.py inside the folder
touch "$folder_name/d${N}p2.py"

# Create input.txt inside the folder
touch "$folder_name/input.txt"

# Create test.txt inside the folder
touch "$folder_name/test.txt"

echo "Folder '$folder_name' and files created successfully."
