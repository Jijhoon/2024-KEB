import random
numbers = list
# for i in range(5):
#     numbers.append(random.randint(1, 100))
class OopsException(Exception):
    pass
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)
try:
    pick = int(input(f"Input idex (0 ~ {len(numbers)-1}): "))
    print(numbers[pick])
    # print((5/0))
    raise OopsException("Oops~~~~") # 객체를 강제로 던져버림. 밑에서 누군가 받아야하는데 그때 받는 것이 else다.
except IndexError as err:
    print(f"Wrong index number\n{err}")
except ValueError as rre:
    print(f"Write the number\n{rre}")
except ZeroDivisionError as zero:
    print(f"Zero can't be division{zero}")
except OopsException as eee:
    print(f"No way! {eee}")
except Exception as new:
    print(f"You find the new Error!\n{new}")
else:
    print("Program terminate")