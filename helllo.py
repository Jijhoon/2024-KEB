#rjust(20) 오른쪽으로 20만큼 정렬 / ljust(20) 왼쪽으로 20만큼 정렬
subject = {
    'python': 'kim',
    'c++': 'sung',
    'data structure': ['kim2', 'kim3'],
    'database': 'kang'
    }
print("{0[python]} {0[data structure]}".format(subject))