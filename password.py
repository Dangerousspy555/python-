# import random
# upper=("A,S,D,F,F,G,R,T,")
# lower=("a,s,d,f,g,g,h,")
# number=("1,2,3,4,5")
# symbols=("@,#,$,^")
# string=upper+lower+number+symbols
# lenght=10
# password="".join(random.sample(string,lenght))
# print(password)
def filter_even_elements(input_list):
    # Use list comprehension to filter out even elements
    even_elements = [num for num in input_list if num % 2 == 0]
    return even_elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_elements(numbers)
print("Even elements:", even_numbers)