# This program reads and displays the content of the philosophers.txt file
def main():
    # Open a file named philosophers.txt
    infile = open("philosophers.txt", "r")

    # Read the file's contents
    # file_contents = infile.read()
    line1 = infile.readline().rstrip("\n")
    line2 = infile.readline().rstrip("\n")
    line3 = infile.readline().rstrip("\n")

    # Print the data that was read into memory
    # print(file_contents)
    print(line1)
    print(line2)
    print(line3)

    infile.close()


# Call the main function
main()
