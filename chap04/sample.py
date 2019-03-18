
number_list = list(range(1,6))
print(number_list)

number_list2 = [ number for number in range(1,6) ]
print(number_list2)

number_list3 = [ number-1 for number in range(1,6) ]
print(number_list3)

number_list4 = [ number for number in range(1,6) if number % 2 == 1 ]
print(number_list4)
