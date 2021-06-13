import base64

def decode(input):
    decodedBytes = base64.b64decode(input)
    return str(decodedBytes, "utf-8")

def main():
    answer1 = input("How many prime numbers are there that are less than 174? ")
    answer2 = input("How many prime numbers are there that are less than 464? ")

    encodedStr = "0JAg0LPQtNC1LdGC0L4g0LvQvtC" + answer2 + "LTQvtC90YHQutC" + answer1 + \
        "Lkg0LTQvtC20LTRjCwK0JrQsNC6INCx0YPRgNGPINCyINGB0YLQsNC60LDQvdC1LgrQn9C+0LfQtNGA0LDQstC70Y/QtdC8INGC0LXQsdGPINC4INC" + \
                answer2 + "LAg0YHRgtCw0YDQvtC8INCx0LDRj9C" + answer2 + \
                    "LUK0JzRiyDRgdGL0LPRgNCw0LXQvCDRgtC10LHQtToKItChINC00L3RkdC8INGA0L7QttC00LXQvdC" + \
                        answer1 + "Y8sINCi0LDQvdGPISIg"

    decodedStr = decode(encodedStr)
    print()
    print(decodedStr)

if __name__ == "__main__":
    main()
