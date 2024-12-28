import os

def list_files_and_dirs(path):
    """
    Lists all files and directories in the given path.

    Args:
        path (str): The path to list.

    Returns:
        list: A list of files and directories in the path.
    """
    try:
        return os.listdir(path)
    except OSError as e:
        print(f"Error listing files and directories: {e}")
        return []

def make_dir(dir_name):
    """
    Creates a new directory with the given name in the current working directory.

    Args:
        dir_name (str): The name of the directory to create.
    """
    try:
        # Use path joining with error handling for MicroPython compatibility
        new_dir_path = os.getcwd() + "/" + dir_name if not hasattr(os, 'path') else os.path.join(os.getcwd(), dir_name) 
        os.mkdir(new_dir_path)
        print(f"Directory '{dir_name}' created successfully.")
    except OSError as e:
        if e.errno == 17:  # File exists
            print(f"Directory '{dir_name}' already exists.")
        elif e.errno == 13:  # Permission denied
            print(f"Permission denied: Cannot create directory '{dir_name}'.")
        else:
            print(f"Error creating directory: {e}")

def change_directory(path):
    """
    Changes the current working directory to the given path.

    Args:
        path (str): The path to change to.
    """
    try:
        os.chdir(path)
        print(f"Current directory changed to '{os.getcwd()}'")
    except OSError as e:
        print(f"Error changing directory: {e}")

def copy_files(source, destination):
    """
    Copies selected files from the source path to the destination path.

    Args:
        source (str): The path to the source directory.
        destination (str): The path to the destination directory.
    """
    try:
        files_in_source = os.listdir(source)
    except OSError as e:
        print(f"Error listing files in source directory: {e}")
        return

    print("Files in source directory:")
    for i, file in enumerate(files_in_source):
        print(f"{i+1}. {file}")

    selected_files_str = input("Enter the numbers of the files to copy (separated by commas): ").strip()
    selected_file_indices = []
    for i in selected_files_str.split(","):
        try:
            index = int(i.strip()) - 1
            if 0 <= index < len(files_in_source):
                selected_file_indices.append(index)
            else:
                print(f"Invalid file number: {index+1}")
        except ValueError:
            print(f"Invalid input: '{i}'. Please enter valid integer numbers.")

    for index in selected_file_indices:
        source_file = os.path.join(source, files_in_source[index]) if hasattr(os, 'path') else source + "/" + files_in_source[index]
        destination_file = os.path.join(destination, files_in_source[index]) if hasattr(os, 'path') else destination + "/" + files_in_source[index] 
        try:
            with open(source_file, 'rb') as src, open(destination_file, 'wb') as dst:
                dst.write(src.read())
            print(f"File '{files_in_source[index]}' copied successfully.")
        except OSError as e:
            print(f"Error copying file '{files_in_source[index]}': {e}")

def move_files(source, destination):
    """
    Moves selected files from the source path to the destination path.

    Args:
        source (str): The path to the source directory.
        destination (str): The path to the destination directory.
    """
    try:
        files_in_source = os.listdir(source)
    except OSError as e:
        print(f"Error listing files in source directory: {e}")
        return

    print("Files in source directory:")
    for i, file in enumerate(files_in_source):
        print(f"{i+1}. {file}")

    selected_files_str = input("Enter the numbers of the files to move (separated by commas): ").strip()
    selected_file_indices = []
    for i in selected_files_str.split(","):
        try:
            index = int(i.strip()) - 1
            if 0 <= index < len(files_in_source):
                selected_file_indices.append(index)
            else:
                print(f"Invalid file number: {index+1}")
        except ValueError:
            print(f"Invalid input: '{i}'. Please enter valid integer numbers.")

    for index in selected_file_indices:
        source_file = os.path.join(source, files_in_source[index]) if hasattr(os, 'path') else source + "/" + files_in_source[index]
        destination_file = os.path.join(destination, files_in_source[index]) if hasattr(os, 'path') else destination + "/" + files_in_source[index] 
        try:
            os.rename(source_file, destination_file)
            print(f"File '{files_in_source[index]}' moved successfully.")
        except OSError as e:
            print(f"Error moving file '{files_in_source[index]}': {e}")

def delete_files(source):
    """
    Deletes selected files from the source path.

    Args:
        source (str): The path to the source directory.
    """
    try:
        files_in_source = os.listdir(source)
    except OSError as e:
        print(f"Error listing files in source directory: {e}")
        return

    print("Files in source directory:")
    for i, file in enumerate(files_in_source):
        print(f"{i+1}. {file}")

    selected_files_str = input("Enter the numbers of the files to delete (separated by commas): ").strip()
    selected_file_indices = []
    for i in selected_files_str.split(","):
        try:
            index = int(i.strip()) - 1
            if 0 <= index < len(files_in_source):
                selected_file_indices.append(index)
            else:
                print(f"Invalid file number: {index+1}")
        except ValueError:
            print(f"Invalid input: '{i}'. Please enter valid integer numbers.")

    for index in selected_file_indices:
        file_to_delete = os.path.join(source, files_in_source[index]) if hasattr(os, 'path') else source + "/" + files_in_source[index] 
        try:
            os.remove(file_to_delete)
            print(f"File '{files_in_source[index]}' deleted successfully.")
        except OSError as e:
            print(f"Error deleting file '{files_in_source[index]}': {e}")

def rmdir_recursive(path):
    """
    Recursively deletes a directory and all its contents.

    Args:
        path (str): The path to the directory to delete.
    """
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item) if hasattr(os, 'path') else path + "/" + item
            if os.path.isdir(item_path):
                rmdir_recursive(item_path)
            else:
                os.remove(item_path)
        os.rmdir(path)
        print(f"Directory '{path}' and its contents deleted successfully.")
    except OSError as e:
        print(f"Error deleting directory: {e}")

def display_menu():
    """
    Displays the file manager menu.
    """
    print("_______________________________")
    print("\nFile Manager Menu:")
    print("1. List files and directories")
    print("2. Make directory")
    print("3. Change directory")
    print("4. Copy files")
    print("5. Move files")
    print("6. Delete files")
    print("7. Delete directory recursively")
    print("8. Exit")
    print("_______________________________")

def main():
    """
    Main function to run the file manager.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        print("")

        if choice == '1':
            path = input("Enter the path to list: ")
            files_and_dirs = list_files_and_dirs(path)
            print(f"Files and directories in '{path}':")
            print("")
            for item in files_and_dirs:
                print(item)
        elif choice == '2':
            dir_name = input("Enter the name of the directory to create: ")
            make_dir(dir_name)
        elif choice == '3':
            path = input("Enter the path to change to: ")
            change_directory(path)
        elif choice == '4':
            source = input("Enter the source directory: ")
            destination = input("Enter the destination directory: ")
            copy_files(source, destination)
        elif choice == '5':
            source = input("Enter the source directory: ")
            destination = input("Enter the destination directory: ")
            move_files(source, destination)
        elif choice == '6':
            source = input("Enter the directory to delete files from: ")
            delete_files(source)
        elif choice == '7':
            path = input("Enter the directory to delete recursively: ")
            rmdir_recursive(path)
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()
