"""
Problem 3_6:
Write a program (not just a function, but a stand alone program or script) that
reads through a file and writes another file that gives the length of each line
in the first file.  If line is the line that you've read into your program, use
line.strip("\n") to strip away the invisible newline character at the end of
each line.  Otherwise, your count will be one higher than the autograder's.
Note that since this is a program running from the Command Window (or terminal
or cmd.exe), it won't be runnable as our usual functions are by entering
Shift-Enter.  You should use the File menu in Spyder to create you own file.
But, if you prefer, there is a starter file called problem3_6starter.py.

Here is a run of my solution program using the HumptyDumpty.txt file. The run
is followed by a printout of HumptyDumpty.txt and the written file
HumptyLength.txt. Note that your program does not print anything out.  It does
write a text file though.  To see these files we have to use type on a PC ( but
it would be cat for Mac or Linux).

C:>python problem3_6.py humptydumpty.txt humptylength.txt

C:>type humptydumpty.txt
Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.
C:>type humptylength.txt
28
31
44
35
"""
# First attempt
def problem3_6(fileName):

    file_n = open(fileName, "r")
    emp = []
    for line in file_n:
        line = line.strip('\n')
        emp.append(line)
        print(len(line))
    f = open('guru.txt',"w+")
    for line in emp:
        f.write(str(len(line))+'\n')


#print(problem3_6('HumptyDumpty.txt'))

# Second attempt:

import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

infile = open(inputfile)
outfile = open(outputfile, 'w')

for line in inputfile:
    line = line.strip("\n")
    outputfile.write(str(len(line)) + "\n")

inputfile.close()
outputfile.close()