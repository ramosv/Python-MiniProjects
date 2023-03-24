

test_cases_true = [("house","esuoh"), ("tar","rat"), ("stressed","desserts"), ("cat", "act"), ("save", "vase"), ("salvages", "lasvegas"), ("state","taste"), ("python","nythop")]
test_cases_false = [("house","mouse"), ("tree","three"), ("desserts","reindeers"), ("test","set"), ("python","java")]

anagrams = lambda x,y: str(sorted(x.lower())) == str(sorted(y.lower()))

for test in test_cases_true:
    print(anagrams(test[0],test[1]))

for test in test_cases_false:
    print(anagrams(test[0],test[1]))