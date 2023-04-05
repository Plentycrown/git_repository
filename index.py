print("hello from the index file")


def average_mean(x):
    count = 0 
    total = 0
    for i in x:
       count = count + 1
       avg = total + i
    return (avg/count))

y = (1,2,3,4,5)
print(average_mean(y))
