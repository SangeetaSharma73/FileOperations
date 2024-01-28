import os

def display_menu():
    print("\nMenu:")
    print("1. Read/Edit Text File")
    print("2. Create Directory")
    print("3. Delete Directory")
    print("4. List Files in Directory")
    print("5. Delete File")
    print("6. Rename File")
    print("0. Exit")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
            return content
    except FileNotFoundError:
        print("File not found.")
        return None

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
        print("Changes saved successfully.")

def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directory '{directory_path}' created successfully.")
    except OSError:
        print(f"Failed to create directory '{directory_path}'.")

def delete_directory(directory_path):
    try:
        os.rmdir(directory_path)
        print(f"Directory '{directory_path}' deleted successfully.")
    except OSError:
        print(f"Failed to delete directory '{directory_path}'. It may not be empty.")

def list_files(directory_path):
    try:
        files = os.listdir(directory_path)
        print(f"\nFiles in '{directory_path}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Directory not found.")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print("File not found.")

def rename_file(old_file_path, new_file_name):
    try:
        os.rename(old_file_path, new_file_name)
        print(f"File renamed to '{new_file_name}' successfully.")
    except FileNotFoundError:
        print("File not found.")

import os

# ... (rest of the functions remain the same)

def main():
    file_path = input("Enter the path of the text file: ")

    while True:
        display_menu()
        choice = input("Enter your choice (0-6): ")

        if choice == '0':
            print("Exiting the program. Goodbye!")
            break

        if choice == '1':
            content = read_file(file_path)
            if content is not None:
                new_content = input("\nEnter the new content: ")
                write_file(file_path, new_content)

        elif choice == '2':
            directory_path = input("Enter the path for the new directory: ")
            create_directory(directory_path)

        elif choice == '3':
            directory_path = input("Enter the path of the directory to delete: ")
            delete_directory(directory_path)

        elif choice == '4':
            directory_path = input("Enter the path of the directory to list files: ")
            list_files(directory_path)

        elif choice == '5':
            delete_file(file_path)

        elif choice == '6':
            old_file_path = input("Enter the path of the file to rename: ")
            new_file_name = input("Enter the new name for the file: ")
            rename_file(old_file_path, new_file_name)

        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()
