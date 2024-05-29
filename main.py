def common_elements():
    first_numbers = [number for number in range(100) if number % 3 == 0]
    second_numbers = [number for number in range(100) if number % 5 == 0]
    return set(first_numbers).intersection(set(second_numbers))



assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("ok")
#print(common_elements())
