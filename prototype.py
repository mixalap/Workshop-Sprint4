for num in range(1, 101):
    val = ''
    # if num == 15:
    #     breakpoint()
    if num % 3 == 0:
        val += 'Fizz'
    if num % 5 == 0:
        val += 'Buzz'
    if not val:
        val = str(num)
    print(val)

# for num in range(1, 101):
#     print(f"n: {num} n%3: {num%3} n%5: {num%5}")
  