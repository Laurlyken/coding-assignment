import os
import re
import sys

def scan_files(directory, regex_pattern):
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    pattern = re.compile(regex_pattern)

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                for line_number, line in enumerate(file, 1):
                    if pattern.search(line):
                        print(f"{filename}:{line_number}")
                        break  # Only report the first matching line per file

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <regex_pattern>")
        sys.exit(1)

    directory_path = sys.argv[1]
    regex_pattern = sys.argv[2]

    scan_files(directory_path, regex_pattern)
