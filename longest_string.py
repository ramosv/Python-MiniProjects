
def longest(listA):

    longest = ""
    for x in listA:
        if len(x) > len(longest):
            longest = x
    return longest

if __name__ == "__main__":
    test_cases = ("first second third", "ab abcd abc acbdefg a abcd aa", "orange apple milkshake banana pear", "sheila sells seashells on the seashore")
    print(longest(test_cases))