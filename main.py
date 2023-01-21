from functools import wraps

# def upper_text(func):
#     @wraps(func)
#     def wrapper():
#         result = func()

#         return result.upper()
        
#     return wrapper 

# @upper_text
# def say_hi():
#     return 'всем привет'


# print(say_hi())        





# def change_phone_number(phone_number):
#     number = list(phone_number)
#     for i in range(len(number)-2):
#         number[i] = '#'

#     return number

# my_number = '+996700123456'

# number = change_phone_number(my_number)

# for n in range(len(number)):
#     print(f'{number[n]}', end='')



# print()


# my_number = '+996700123456'
# def change_number_to_sharp(my_number):
#     result = ''

#     for i in my_number[:-2]:
#         result += '#'

#     result += my_number[-2:]   

#     return result 

# print(change_number_to_sharp(my_number))


def change_phone_number(func):
    @wraps(func)
    def wrapper():
        number = func()
        result = ''
        for i in range(len(number)-2):

            result += '#'

        result += number[-2:] 

        return result
    return wrapper    


@change_phone_number
def get_number():
    phone_number = '+996700123456'
    return phone_number

print(get_number())
 
