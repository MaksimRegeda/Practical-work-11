# Задача 11.1.
import time

n = 1000000

my_list = list(range(n))
my_set = set(range(n))

target = 999999
count = 100

start = time.perf_counter()

for i in range(count):
    target in my_list

list_time = time.perf_counter() - start

start = time.perf_counter()

for i in range(count):
    target in my_set

set_time = time.perf_counter() - start

print("Пошук у List:", round(list_time, 6), "секунд")
print("Пошук у Set:", round(set_time, 6), "секунд")

print("Прискорення:",
      round(list_time / set_time, 2), "разів")

# Задача 11.2.

import time

def intersection_slow(a, b):
    result = []

    for x in a:
        if x in b and x not in result:
            result.append(x)

    return result


def intersection_fast(a, b):
    set_b = set(b)
    result = []
    seen = set()

    for x in a:
        if x in set_b and x not in seen:
            result.append(x)
            seen.add(x)

    return result

a = list(range(10000))
b = list(range(5000, 15000))

start = time.perf_counter()
result1 = intersection_slow(a, b)
time1 = time.perf_counter() - start

start = time.perf_counter()
result2 = intersection_fast(a, b)
time2 = time.perf_counter() - start

print("Перший алгоритм O(N*M):")
print("Час виконання:", round(time1, 6), "секунд")

print("\nДругий алгоритм O(N+M):")
print("Час виконання:", round(time2, 6), "секунд")

print("\nПеретин масивів:")
print(result2)

print("\nКількість спільних елементів:", len(result2))
print("Результати однакові:", result1 == result2)

print("\nПрискорення:",
      round(time1 / time2, 2), "разів")
