#  take 10 names from the user and
#  display count of the name who's length is more than 5 letters

def count(lst):
    c = 0
    for x in lst:
        if len(x) >= 5:
            c += 1
    return c


lst = ["Amit", "Dhiraj", "Ganesh", "Kunal", "Laxman", "Manish", "Nishant", "Om", "Rohit", "Virat"]

result = count(lst)
print("The count is: {}".format(result))
