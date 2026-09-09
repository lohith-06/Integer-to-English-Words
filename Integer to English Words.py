def number_to_words(num):
    ones = [
        "Zero", "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
        "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]
    tens = [
        "", "", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    ]

    def convert(n):
        if n < 20:
            return ones[n]

        if n < 100:
            if n % 10 == 0:
                return tens[n // 10]
            return tens[n // 10] + " " + ones[n % 10]

        if n < 1000:
            if n % 100 == 0:
                return ones[n // 100] + " Hundred"
            return ones[n // 100] + " Hundred " + convert(n % 100)

        if n < 1000000:
            if n % 1000 == 0:
                return convert(n // 1000) + " Thousand"
            return convert(n // 1000) + " Thousand " + convert(n % 1000)

        if n < 1000000000:
            if n % 1000000 == 0:
                return convert(n // 1000000) + " Million"
            return convert(n // 1000000) + " Million " + convert(n % 1000000)

        if n % 1000000000 == 0:
            return convert(n // 1000000000) + " Billion"
        return convert(n // 1000000000) + " Billion " + convert(n % 1000000000)

    if num == 0:
        return "Zero"

    if num < 0:
        return "Negative " + convert(abs(num))

    return convert(num)


num = int(input("Enter a number: "))
print(number_to_words(num))