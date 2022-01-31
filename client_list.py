# python program that prints out a client list with numbering from the file - clients.txt

# Open a file named clients.txt
infile = open("clients.txt", "r")

# Print out the client list with numbering
counter = 1
for client in infile:
    print(counter, ". ", client.rstrip("\n"), sep="")
    counter += 1
