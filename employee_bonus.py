import csv

employeepay = open("employeepay.csv", "r")

employeepay_file = csv.reader(employeepay, delimiter=",")

next(employeepay_file)

for record in employeepay_file:
    print("First Name:", record[1])
    print("Last Name:", record[2])
    print("Salary:", record[3])
    print("Bonus", record[4])
    print("Total Pay:", record[3 * 4])
