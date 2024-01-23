#print the current and previous number in a range 1-10
print("Printing current and previous number and their sum in a range(10)")
#modify the previous number as 0
previous_number = 0
#loop from 1 to 10
for i in range(1, 10):
    sum = previous_number + i
    #print the current number, previous number, and the sum
    print("Current Number:", i, "Previous Number: ", previous_number, " Sum: ", sum)
#modify previous number
#set it to i