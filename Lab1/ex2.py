def readTxtFile(path= "loremipsum.txt"):
    """reads a txt files and returns a list of all lines"""
    file = open(path)
    lines = []

    for l in file:
        lines.append(l.strip())
    
    file.close()
    return lines

def capitalizeWords(string: str):
    """given a string capitalizes each word"""
    output=""
    string=string.split(" ")

    for i in string:
        output+= i[0].upper() + i[1:] + " "

    return output

def writeTxtFile(list: list, path= "output.txt"):
    """given a list of strings, writes them to a file as separate lines"""

    file = open(path, "x")
    for l in list:
        file.writelines(l + "\n")

    file.close()



lines = readTxtFile()

for i in range(len(lines)):
    lines[i]=(capitalizeWords(lines[i]))

writeTxtFile(lines)

