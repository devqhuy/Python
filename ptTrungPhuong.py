def evenNum(res):
    even_numbers = []
    for number in res:
        if number % 2 == 0:
            even_numbers.append(number)
    print(even_numbers)
if __name__ == '__main__':

# Initial list
        res = []

        # Input lengths
        lengths = int(input())

        # Add element
        for i in range(lengths):
            # Input elements
            n = int(input())
            res.append(n)

        evenNum(res)