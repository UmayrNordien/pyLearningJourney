#dictionaries
employee = {
    "name":"John Smith",
    "age":"39",
    "salary":"$10,000",
    "Designation":"Manager",
}

# print(employee["name"], employee["age"])

#display the key
# for i in employee:
#     print(i)

## display the key values
# for i in employee.values():
#     print(i)

#display the entire dictionary
for key in employee:
    print(key + ":" + str(employee[key]))
