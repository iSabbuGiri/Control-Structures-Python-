'''Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.'''

lst = []
tup1 = ('Sabbu', 'Giri', 22)
lst.append(tup1)
tup2 = ('Aditya', 'Shah', 21)
lst.append(tup2)
tup3 = ('Puzza', 'Yadav', 23)
lst.append(tup3)
tup4 = ('Kushal', 'Giri', 18)
lst.append(tup1)
tup5 = ('Aayush', 'Karki', 19)
lst.append(tup5)

print("Original list is {}".format(lst))


lst.sort(key= lambda x:x[2])
print("List sorted with third element is {}".format(lst))
