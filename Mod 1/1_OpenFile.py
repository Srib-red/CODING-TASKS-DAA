try:
    file1 = open("SorupText.txt", "r")
    content = file1.read()
    print("file content: ")
    print(content)

except FileNotFoundError:
    print("File Doesnt exist")
except PermissionError:
    print("You donot have permission to open this file.")
except Exception as e:
    print("Unexpected error: {e}")

finally:
    # Always close the file (if it was opened)
    try:
        file1.close()
    except NameError:
        # file was never opened
        pass

# try:
#     # Open the file in read mode
#     with open("sample.txt", "r") as file:
#         content = file.read()
#         print("File content:")
#         print(content)

# except FileNotFoundError:
#     print("Error: The file was not found. Please check the file name or path.")

# except PermissionError:
#     print("Error: You don't have permission to access this file.")

# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
