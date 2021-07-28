"""Create a note-taking program. When a user starts it up, it should prompt them for a filename.

If they enter a file name that doesn't exist, it should prompt them to enter the text they want
to write to the file. After they enter the text, it should save the file and exit.

If they enter a file name that already exists, it should ask the user if they want:

A) Read the file

B) Delete the file and start over

C) Append the file

If the user wants to read the file it should simply show the contents of the file on the screen.
If the user wants to start over then the file should be deleted and another empty one made in its
place. If a user elects to append the file, then they should be able to enter more text, and that
text should be added to the existing text in the file. """
from os.path import exists as file_exists



f_to_open = input("Please input a file to open: ")
it_exists = file_exists(f_to_open)
if it_exists == False:
    file = open(f_to_open, "w")
    text_to_enter = input("Please enter the text you wish to save: ")
    file.write(text_to_enter)
    file.close()
else:
    repeat = True
    while repeat == True:
        repeat = False
        option = input("""Do you want to: 
        A) Read the file
        
        B) Delete the file and start over
        
        C) Append the file
        
        D) Replace a single line
        """)
        if option.upper() == "A":
            file = open(f_to_open, 'r')
            contents = file.read()
            print(contents)
            file.close()
        elif option.upper() == "B":
            file = open(f_to_open, "w")
            text_to_enter = input("Please enter the text you wish to save: ")
            file.write(text_to_enter)
            file.write('\n')
            file.close()
        elif option.upper() == "C":
            file = open(f_to_open, "a")
            text_to_enter = input("Please enter the text you wish to save: ")
            file.write(text_to_enter)
            file.write("\n")
            file.close()
        elif option.upper() == "D":
            where_to_insert = int(input("Where do you want to insert this line? "))
            what_to_insert = input(f"What text do you want to input in line {where_to_insert}? ")
            file = open(f_to_open, 'r')
            contents = file.read()
            contents = contents.split()
            file.close()
            file = open(f_to_open, "w")

            for i in range(len(contents)):
                if i == where_to_insert:
                    file.write(what_to_insert)
                    file.write('\n')
                else:
                    file.write(contents[i])
                    file.write('\n')
            file.close()

        else:
            print("That didn't make any sense. Try A, B, or C for a response.")
            repeat = True

file = open(f_to_open)
contents = file.read()
print(contents)
file.close()
