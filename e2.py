import csv

with open("files3/weather.csv", 'r') as file:
    data = list(csv.reader(file))
print(data)
city = input("Enter the name of the city: ")
for row in data[1:]:
    if row[0] == city:
        print(row[1])