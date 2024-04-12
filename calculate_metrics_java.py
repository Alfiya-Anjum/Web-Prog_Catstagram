import os

code_dir_path = r"C:\Users\SAMSUNG\OneDrive\Documents\Web_Dev\Catstagram\Catstagram"  # Directory Path

# Initialize metrics
loc = 0  # Lines of Code
ploc = 0  # Physical Lines of Code (ignoring blank lines and comment lines)
comments = 0  # Comment lines

# Iterate over files in the directory
for filename in os.listdir(code_dir_path):
    file_path = os.path.join(code_dir_path, filename)
    # Ensure it's a file
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
                loc += len(lines)
                for line in lines:
                    stripped_line = line.strip()
                    if stripped_line.startswith("#"):
                        comments += 1
                    elif stripped_line:
                        ploc += 1
        except UnicodeDecodeError as e:
            print(f"Error reading file {file_path}: {e}")
        except Exception as e:
            print(f"An error occurred with file {file_path}: {e}")

print(f"LOC (Lines of Code): {loc}")
print(f"PLOC (Physical Lines of Code): {ploc}")
print(f"Comments: {comments}")
