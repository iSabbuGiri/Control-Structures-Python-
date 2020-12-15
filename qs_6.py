'''Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.'''

names = ['Hari', 'Shyam', 'John', 'Gita']
search_lst = input("Whose name you want to search?")
for name in names:
   if search_lst == name:
       print("Found", name)
       break
else:
    print("Not Found")    