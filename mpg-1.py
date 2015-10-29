#define speed travelled

speed = int(input("What is your speed "))

# define hours travelled
hours = int(input("How long did you drive?"))
#show distance travelled each hour
for hours in range (1, hours+1):
    mph = (hours*speed)
    print ("In hour", hours, "your miles travelled were:", mph)
