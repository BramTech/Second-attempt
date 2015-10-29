#A bug collector collects bugs every day for five days.
#Write a program that keeps a running total of the number of bugs
#collected during the five days. The loop should ask for the number
#of bugs collected for each day, and when the loop is finished,
#the program should display the total number of bugs collected.
 

# 5 days of bug collection
TOTAL = 0
count = 5
#    input bugs collected
#    add bugs collected to total
for day in range (1,8):
    print ("Enter bugs collected on day:", day)
    bugs = int(input())
    TOTAL = (TOTAL + bugs)
#display the total bugs
print ("you collected a total of", TOTAL, "bugs.")

#ask user for five numbers

#initialize total and count variable
#total = 0
#count = 1
#prime read


#while count <=5:
#    number = int(input("Enter a number: "))
#    total += number
#    count += 1   
#print ("Total: ", total)

