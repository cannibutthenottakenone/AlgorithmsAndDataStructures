
# capitalize the first letter of each word in the text
def capitalizeWords(text):

    cap_lines = []  # initialize the list of capitalized lines
    cap_words = []  # initialize the list of capitalized words

    for line in text:
        words = line.split() # create a list containing all the words of the current line
        cap_words.clear()  # empty the list of capitalized words
        for word in words:
            # cap_word = word.capitalize() # using the built-in method
            cap_word = word[0].upper() + word[1:]
            cap_words.append(cap_word)
        cap_line = " ".join(cap_words)  # merge the list of words in a single string
        cap_lines.append(cap_line)

    return cap_lines


# read a text file and return a list of lines
def readTxtFile(file_path):
    text = []
    with open(file_path, 'r') as f:
        current_line = f.readline()
        while current_line:
            # strip() is optional, it removes the newline character at the end of each line
            text.append(current_line)
            current_line = f.readline()
    f.close()
    return text


# write a text file line by line
def writeTxtFile(file_path, text):
    with open(file_path, 'w') as f:
        for line in text:
            f.write(line + "\n")  # add new line at the end of each line
    f.close()


if __name__ == "__main__":
    startText = readTxtFile('loremipsum.txt')
    capText = capitalizeWords(startText)
    writeTxtFile("loremipsum_cap.txt", capText)
