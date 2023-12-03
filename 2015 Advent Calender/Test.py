test_num = 0

def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# Example usage:
num = 8
result = find_divisors(num)

print(f"The divisors of {num} are: {result}")

for num in result:
    test_num += num * 10

print(test_num)