
def romanToInt(s: str):
    dict_of_value = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    list_of_char = list(s)
    total = 0
    for i in range(len(s)):
        total += dict_of_value[list_of_char[i]]
    return total

def main():
    print(romanToInt("MCMXCIV"))

main()
