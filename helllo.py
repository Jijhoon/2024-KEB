import random
numbers = list
# for i in range(5):
#     numbers.append(random.randint(1, 100))

numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)
try:
    pick = int(input(f"Input idex (0 ~ {len(numbers)-1}): "))
    print(numbers[pick])
    print((5/0))
except IndexError as err:
    print(f"Wrong index number\n{err}")
except ValueError as rre:
    print(f"Write the number\n{rre}")
except ZeroDivisionError as zero:
    print(f"Zero can't be division{zero}")
except Exception as new:
    print(f"You find the new Error!\n{new}")