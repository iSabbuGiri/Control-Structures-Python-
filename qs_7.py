"""
Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age."""


tup = [('Sabbu', 'Giri', 22), ('Puzza', 'Yadav', 23), ('Kushal','Giri', 18)]
lst = []
total = 0
for i in range(len(tup)):
    a = tup[i][2]
    lst.append(a)
print(lst)    


for j in range(0, len(lst)):
    total = total + lst[j]
    avg = total/len(lst)
    print(avg)

for i in tup:
    if i[2]>avg:
        print(i[0] + ' ' + i[1] + 'is older')
    else:
        print(i[0]+ ' ' + i[1] + 'is younger')    
