# TESTING

# f=1,1,2,3,5
# t=1,2,3,5,8
# l=1,2,3,5,8


is_finished = False
first = 0
temp = 0
last = 1

number = int(input("Enter a number: "))
while not is_finished:
    if not (number > first):
        if first == number:
            print("It is a number of fibonnacci")
            
        else:
            print("It is not number of fibonnacci")

        is_finished = True
    
    temp = first + last
    first = last
    last = temp

