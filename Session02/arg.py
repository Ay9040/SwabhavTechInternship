def calculate_product(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

print(calculate_product(10,20,30))
print(calculate_product(*range(1,6,2)))