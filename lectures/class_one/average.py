def average(list_of_numbers):
    running_sum = 0
    for i in list_of_numbers:
        running_sum += i
    return running_sum/float(len(list_of_numbers))

print("average of 1st hundred contigious numbers",average(list(range(100))))

