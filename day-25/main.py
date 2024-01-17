import csv

# Import CSV file

# Classic mode
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        temperatures.append(row[1])
        print(row)

    temperatures.remove("temp")
    print(temperatures)


# Using pandas
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

# Mean
new_temp_list = data["temp"].to_list()
print(sum(new_temp_list) / len(new_temp_list))
print(data["temp"].mean())

# Max value
print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

# Create a dataframe from scratch
data_dict = {
    "students": ["Luna", "Nebie", "Hermi"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
