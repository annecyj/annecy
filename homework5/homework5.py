# ----- 3.1 Vocabulary Review -----
# 1) Git is the tool to do tasks like keeping track of changes or managing different versions. Github is remote and allows hosting for git repositories. git is local while github is a remote system.
# 2) Terminal is when the user interacts with the computer's operating system while a command line is where you enter commands.
# 3) A local repository is stored on your device while a remote repository is stored on a server like github. local repositories can be pushed to remote repositories.
# 4) Version control tracks and manages changes to files over time and allows users to perform actions such as revert files. An example of a version control system is Git.
# 5) Staging area is like a rough draft zone where useres can make changes before commiting files to saved history
# 6) Git add adds files to our repository
# 7) Git commit takes the files from the staging area and commits them to your version history
# 8) Git push pushes the commited changes to your remote repository.
# 9) git status tells you the status of your repository, for example, if any commits have been made.
# 10) git pull downloads content from a remote repository and updates the local repository to match that content.
# 11) prints the working directory, show the current file path
# 12) ls lists the files and folders in the current working directory
# 13) cd changes directories. by itself, it changes to the parent directory but if you add a .., it goes back one directory.
# 14) nano opens up a text file editor. if you use nano with a python file, you can edit the python file on the terminal.
# 15) touch creates a new, empty file
# 16) mv moves files and can be used to rename too.
# 17) rm removes files and can be used to delete the specified file.
# 18) cat means concatenate which prints out all the contents of a file.

# ----- 3.2 A directory tree -----
# 1) pwd
# 2) ls
# 3) git pull homework.py brianna_repo, git pull origin main
# 4) mv homework.py ~/python_decal/judy_decal/homework/
# 5) cd homework
# 6) cat homework.py
# 7) git add., git commit -m "done with hw", git push origin main
# 8) this error means Judy tried pushing work to the remote repository but the local branch doesn't have those changes yet. git add ., git commit, git push origin main
# 9) cd ~/Recent/

# ----- 4.1 Data Types -----
def checkDataType(data_input):
    return(type(data_input))

# ----- 4.2 Conditionals -----
def evenOrOdd(integer):
    if integer % 2 == 0:
        return "Even"
    elif integer % 1 == 0:
        return "Odd"

# ----- 5 Loops -----
def sumWithLoop(integer_list):
    sum = 0
    for number in integer_list:
        sum += number
    return sum

# ----- 6.1 Lists -----
def duplicateList(list):
    new_list = []
    for element in list:
        new_list.append(element)
        new_list.append(element)
    return new_list

# ----- 6.2 Debugging -----
def square(num):
    return num * num
# forgot the : after defining the function

print(sumWithLoop([1, 2, 3, 4, 5]))

