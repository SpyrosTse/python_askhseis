from shutil import copyfile
import numpy as np
import matplotlib.pyplot as plt

src = input("Give me the name of the file")
copyfile(src,"temp.txt")

file1 = open("temp.txt", "r")
file2 = open(src,"w")
char1 = file1.read(1)
while char1:
    number = ord(char1)
    if(number % 2 != 0):
        file2.write(number)
    char1 = file1.read(1)
file1.close()
file2.close()

characters = [chr(i) for i in range(127)]
parameters = []
file1 = open("temp.txz", 'r')
char2 = file1.read(1)
while char2:
    parameters[ord(char2) - 32 ] = parameters[ord(char2) - 32 ] + 1
    char2 = file1.read(1)
file1.close()

figures = plt.figure(figsize = (10, 5))

plt.bar(characters, parameters, color = 'red', width=0.4)
plt.title("Frequency of ASCII characters")
plt.show()

