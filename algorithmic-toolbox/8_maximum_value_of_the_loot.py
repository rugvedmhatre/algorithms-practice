import sys

def get_optimal_value(capacity, weights, values):
    items = []
    for i in range(len(weights)):
        item = [values[i], weights[i]]
        items.append(item)
    items.sort(key = lambda x : x[0]/x[1], reverse=True)
    final_value = 0
    for value, weight in items:
        if capacity == 0 :
            return final_value
        else:
            amount = min(weight, capacity)
            final_value += amount * value/weight
            capacity -= amount
    return final_value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
