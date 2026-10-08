def half_adder(a, b):
    sum_bit = a ^ b
    carry = a & b

    return sum_bit, carry


print("Half Adder")
print("----------")

a = int(input("Enter A (0 or 1): "))
b = int(input("Enter B (0 or 1): "))

if a in [0, 1] and b in [0, 1]:

    sum_bit, carry = half_adder(a, b)

    print("\nResults:")
    print(f"A     = {a}")
    print(f"B     = {b}")
    print(f"Sum   = {sum_bit}")
    print(f"Carry = {carry}")

else:
    print("Invalid input! Please enter only 0 or 1.")
