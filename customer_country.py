import csv

customer_country = open("customers.csv", "r")

customer_country = csv.reader(customer_country, delimiter=",")

outfile = open(customer_country, "w")

next(customer_country)

counter = 0
for record in customer_country:
    outfile.write(record[1] + "," + record[2] + "," + record[4], +"\n")
    counter = 1

print(counter)
outfile.close()
