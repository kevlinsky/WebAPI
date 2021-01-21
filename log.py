import math

p = [0.37, 0.2, 0.15, 0.1, 0.05, 0.05, 0.04, 0.03, 0.02]

print("Введите основание:")
s = int(input())

iterator = 1
for pi in p:
    print(f"l{iterator} = {round(math.log(1 / pi, s))}")
    iterator += 1
