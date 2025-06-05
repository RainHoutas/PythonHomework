def sum_odd_even(s):
    oddsum = 0
    evensum = 0
    for char in s:
        num = int(char)
        if num % 2 == 0:
            evensum += num
        else:
            oddsum += num
    print(f"oddsum={oddsum},evensum={evensum}")
sum_odd_even("123456789")
