# This is a Menu-Driven Program working with files
import Module_File  # Correct import statement

print("Below are the choices : ")
print("1. Write a file")
print("2. Read a file")
print("3. Append to a file")
print("4. Exit")

while True:
    choice = input("Enter your choice : ")

    if choice == '1':  # Write to file option
        filename = input("Enter a filename  : ")
        if not filename.endswith('.xml'):
            print("You have not entered a valid filename\n")
            continue
        texts = input("Enter the text to be inserted into the file " + filename + " :\n ")
        Module_File.write_to_a_file(filename, texts)  # Corrected reference to the imported module
        print("\nFile written successfully\n")

    elif choice == '2':  # Read from file option
        filename = input("Enter the filename to be read with  : ")
        Module_File.read_a_file(filename)  # Corrected reference to the imported module

    elif choice == '3':  # Append to file option
        filename = input("Enter the filename to append with a  : ")
        texts = input("Enter the text to be appended to the file : \n ")
        Module_File.append_to_a_file(filename, texts)  # Corrected reference to the imported module
        print("\nFile appended successfully\n")

    elif choice == '4':  # Exit option
        print("\nYou have successfully exited the program\n")
        break

    else:  # Invalid choice handler
        print("Wrong Choice, you will have to enter your choice again\n")
