from itertools import product



def maximize_expression(K, M, lists):
    # twoj kod tutaj
    combinations = product(*lists)
    max_value = 0

    for combination in combinations:
        current_sum = sum(x**2 for x in combination)

        current_mod_value = current_sum % M

        if current_mod_value > max_value:
            max_value = current_mod_value

    return max_value

if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
