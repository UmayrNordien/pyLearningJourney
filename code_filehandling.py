# Operation      Syntax    Description
# Read Only      r         Open text file for reading only.
# Read and Write r+        Open the file for reading and writing.
# Write Only     w         Open the file for writing.
# Write and Read w+        Open the file for reading and writing. Unlike “r+” it doesn’t raise an I/O error if the file doesn’t exist.
# Append Only    a         Open the file for writing and creates a new file if it doesn’t exist. All additions are made at the end of the file, and no existing data can be modified.
# Append and Read a+       Open the file for reading and writing and creates a new file if it doesn’t exist. All additions are made at the end of the file, and no existing data can be modified.


#reading from files
# with open('./data.txt', 'r') as file:
#     data = file.read()
#     # data = file.readline(5)
#     print(data)



#writing from files
userInput = input('Enter your message you wish to save: ')

with open('./insert_data.txt', 'a') as file:
    data = file.write(userInput + '\n')