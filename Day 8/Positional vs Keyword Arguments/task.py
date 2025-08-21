# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
# greet_with(location='Daegue', name='Hwan')

def calculate_love_score(name1, name2):
    word_true = "true"
    word_love = "love"

    name1 = name1.lower()
    name2 = name2.lower()

    count_true = 0
    count_love = 0

    for letter in word_true:
        count_true = count_true + name1.count(letter) + name2.count(letter)

    for letter in word_love:
        count_love = count_love + name1.count(letter) + name2.count(letter)

    print(f"{count_true}{count_love}")


calculate_love_score("Kanye West", "Kim Kardashian")