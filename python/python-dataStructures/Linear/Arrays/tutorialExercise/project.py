numOfDays = int(input("Enter number of days: "))
days = []
for i in range(0,numOfDays):
    day = int(input("Enter {}'s high temp: ".format(i+1)))
    days.append(day)

avg = round(sum(days)/len(days),2)
print("Average No of Days {}".format(avg))

print("There are {} days above average".format(sum([1 for i in days if i > avg])))
