def max_value_after_operations(n, queries):
    arr = [0] * (n + 1)

    for query in queries:
        a, b, k = query
        arr[a] += k
        if b + 1 <= n:
            arr[b + 1] -= k

    max_value = 0
    current_value = 0

    for value in arr:
        current_value += value
        max_value = max(max_value, current_value)

    return max_value

# Ejemplo
n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
result = max_value_after_operations(n, queries)
print(result)  # Salida esperada: 10