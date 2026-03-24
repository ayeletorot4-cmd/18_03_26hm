def nth_biggest_unique_number(list_num:list,n:int)->int:
    set_=set(list_num)
    print(set_)

    unique_numbers=list(set_)
    unique_numbers.sort(reverse=True)
    print(unique_numbers)
    return unique_numbers[n-1]
numbers_=[88, 100, 90, 95, 95, 97, 97, 99, 97, 99]
n = 4
print(nth_biggest_unique_number(numbers_,n))