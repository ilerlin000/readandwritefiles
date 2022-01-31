# This program writes three lines of data to a file
def main():
    # Open a file named philosphers.txt
    outfile = file_object = open("philosophers.txt", "w")

    # Write the names of three philosophers to the file-
    # John Locke, David Hume, Edmund Burke
    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")

    # Close the file
    outfile.close()


def add_my_name():
    outfile = open("philosophers.txt", "a")

    outfile.write("Lindsey Iler\n")

    outfile.close()


# Call the main function
main()
add_my_name()
