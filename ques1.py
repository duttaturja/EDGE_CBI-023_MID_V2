given_list = []
def finding_second_largest_number_without_sorting(list):
    largest_number = max(list) #finds the max element in list
    list.remove(largest_number) #deleting the max element from the list
    second_largest_number = max(list) #again finding the max element which is the second largest now
    return second_largest_number #returns the second largest number


n = input("Enter your list size: ")
n = int(n)
for i in range(0,n): #loop to get elements of the list
    x = input(f"{i+1}th element: ") #getting user input
    x=int(x) #datatype declaration
    given_list.append(x) #entering all the elements into the list

answer = finding_second_largest_number_without_sorting(given_list)
print(f"The second largest number is: {answer}")