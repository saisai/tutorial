from itertools import count


# create a count iterator object
iterator = (count(start=0, step=2))

# print a odd list of integers
print("Even list:", list(next(iterator) for _ in range(5)))


print("Odd list:", list(next(iterator) for _ in range(5)))

# Program to emulate enumerate()
# using count()

# list containing some strings
my_list =["Geeks", "for", "Geeks"]

# count spits out integers for
# each value in my list

for i in zip(count(start=1, step=1), my_list):

    # prints tuple in an enumearted
    # format
    print(i)


stop = 1
for i in count(start=0, step=2):
    if stop < 10:
        print(i)
    else:
        break
    stop += 1

s = 1
for i in count(2.5, 0.5):
    if s < 10:
        print(i)
    else:
        break
    s += 1
