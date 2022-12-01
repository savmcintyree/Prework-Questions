question 1
def hello_name(user_name):
    print("Hello, " + user_name.title() + "!")

hello_name('savanna')

question 2
def first_odds(odd_numbers):
    i = 1
    while i < 100
        print(i)
        i += 2
    return

print(odd_numbers())

question 3
def max_num_in_list(a_list):
        return max([item for item in a_list])

print(max_num_in_list(([1,66,7,12])))

question 4
def is_leap_year(a_year):
    not_a_leap_year = False
       
        if (a_year % 400 == 0) and (a_year % 4 == 0) or (a_year % 100 != 0):
                print("Is a leap year")
        
        else:
                not_a_leap_year = True
                print("Is not a leap year")

a_year = int(input("What is the year: "))

is_leap_year(a_year)

question 5
def is_consecutive(a_list):
if sorted(a_list) == list(range(min(a_list),max(a_list)+1)):
        return True
    else:
        return False
        
print(is_consecutive([12,16,14]))