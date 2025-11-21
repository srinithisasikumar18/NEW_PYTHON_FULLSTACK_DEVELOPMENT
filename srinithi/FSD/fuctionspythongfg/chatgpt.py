# # a=22
# # b=5
# # print(a%b)

# def get_remainder_without_modulo(dividend, divisor):
#     """
#     Calculates the remainder of a division without using the modulo operator (%).

#     Args:
#         dividend (int): The number to be divided.
#         divisor (int): The number by which the dividend is divided.

#     Returns:
#         int: The remainder of the division.

#     Raises:
#         ValueError: If the divisor is zero.
#     """
#     if divisor == 0:
# num4 = 3
# result2 = get_remainder_without_modulo(num3, num4)
# print(f"The remainder of {num3} divided by {num4} is: {result2}")

# # Handling negative numbers (optional, depending on desired behavior)
# num5 = -17
# num6 = 5
# result3 = get_remainder_without_modulo(num5, num6)
# print(f"The remainder of {num5} divided by {num6} is: {result3}")
        raise ValueError("Divisor cannot be zero.")

#     # Calculate the quotient using integer division (//)
#     quotient = dividend // divisor

#     # Calculate the remainder
#     remainder = dividend - (divisor * quotient)

#     return remainder

# # Example usage:
# num1 = 17
# num2 = 5
# result = get_remainder_without_modulo(num1, num2)
# print(f"The remainder of {num1} divided by {num2} is: {result}")

# num3 = 10
# 
# # Handling zero divisor
# try:
#     get_remainder_without_modulo(10, 0)
# except ValueError as e:
#     print(f"Error: {e}")

a=17
b=5
quo=a//b
print(quo)
rem=a-(b*quo)
print("modulus of",a, "and" ,b ,"is:",rem)