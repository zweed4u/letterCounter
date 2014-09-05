def countLetterWord(char, string):
    count = 0
    if string == " ":
        Print("Cannot process an empty string")
    else:
        for word in string:
            if word == char:
                count+= 1
    return count


def countLetterOpenFile(char, filename):
    file = open(filename)
    num = 0
    for string in file:
        string = string.strip()
        num+= countLetterWord(char, string)
    return num


def countLetterFileName(char, filename):
    print(countLetterOpenFile(char, filename))


def main():
    char = raw_input("Please Enter a character: ")
    print "\n"+str(char)
    print "\n"
    filename = raw_input("Please Enter the filename: ")
    print "\n"
    countLetterFileName(char, filename)
    print "\n"
    raw_input("Please Hit Enter to End")
    print "\n"
    raise SystemExit

main()
