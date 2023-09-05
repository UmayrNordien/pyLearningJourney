import pickle

# phonebook = {
#     'a' : '1',
#     'b' : '2',
#     'c' : '3'
# }

# with open('./phonebook.dat', 'wb') as bin:     # "wb" mode opens the file in binary format for writing while the "rb" option opens the file in binary format for reading
#     pickle.dump(phonebook, bin)

with open('./phonebook.dat', 'rb') as bin:
   data = pickle.load(bin)
   print(type(data))
   print(data)
