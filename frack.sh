#!/bin/bash

# This is a Bash script that checks if Python is installed, installs it if not,
# and then runs a list of Python scripts.

# Define an array of Python script paths
python_scripts=(
    "/path/to/your/script1.py"
    "/path/to/your/script2.py"
    "/path/to/your/script3.py"
    # Add more script paths as needed
)

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python not found. Installing Python..."
    sudo apt-get update
    sudo apt-get install python3
    echo "Python installed successfully."
fi

# Iterate through the array and run each Python script
for script in "${python_scripts[@]}"; do
    if [ -f "$script" ]; then
        echo "Running script: $script"
        python3 "$script"
    fi
done
