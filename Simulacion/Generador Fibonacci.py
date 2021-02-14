import itertools as it


def gen_fib(x_0, x_1, m):
    flag = False
    while True:
        x_next = (x_0 + x_1) % m
        x_0 = x_1
        x_1 = x_next
        flag = x_0 + x_1 == 1
        if flag:
            break
    return flag


data = list(it.combinations(range(0, 5), 2))
for k in range(1, 5):
    data.append((k, k))
print(data)
for j in range(len(data)):
    x_0 = data[j][0]
    x_1 = data[j][1]
    print(gen_fib(x_0, x_1, 5))
