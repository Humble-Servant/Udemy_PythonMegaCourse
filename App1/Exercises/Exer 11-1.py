def get_max_min():
    grades = [9.6, 9.2, 9.7]
    max_min = {'Max':max(grades), 'Min':min(grades)}
    return max_min


maxmin = get_max_min()
print(f"Max: {maxmin['Max']}  Min: {maxmin['Min']}")