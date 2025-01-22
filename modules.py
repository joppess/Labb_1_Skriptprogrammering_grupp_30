def show_divided_numbers(num1, num2):
    results = []
    for i in range(1,1401):
        if i % num1 == 0 and i % num2 == 0:
            results.append(i)

    return results

