# Write your code here.
# First task - hello

def hello():
    return "Hello!"

# Second task - greet with formatted string
def greet(name):
    return f"Hello, {name}!"

# Third task - python calculator
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
# fourth task - data type conversion
def data_type_conversion(value, type):
    try:
        if type == "float":
            return float(value)
        elif type == "str":
            return str(value)
        elif type == "int":
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
    
    # Fifth task - grading system using *args
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except:
        return "Invalid data was provided."
    
# Sixth task - repeat using a for loop with range
def repeat(string, count):
    result = ""

    for i in range(count):
        result += string

    return result

# Seventh task - student scores using kwargs
def student_scores(mode, **kwargs):
    if mode == "mean":
        total = sum(kwargs.values())
        count = len(kwargs)
        return total / count

    elif mode == "best":
        best_student = ""
        best_score = -1

        for student, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_student = student

        return best_student
    
# Eighth task - titleize
def titleize(title):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = title.split()
    titleized_words = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            titleized_words.append(word.capitalize())
        elif word in little_words:
            titleized_words.append(word)
        else:
            titleized_words.append(word.capitalize())

    return " ".join(titleized_words)

# Ninth task - hangman
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

# Tenth task - pig latin
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    translated_words = []

    for word in words:
        if word[0] in vowels:
            translated_words.append(word + "ay")
        else:
            consonants = ""
            rest_of_word = word

            while len(rest_of_word) > 0 and rest_of_word[0] not in vowels:
                if rest_of_word.startswith("qu"):
                    consonants += "qu"
                    rest_of_word = rest_of_word[2:]
                else:
                    consonants += rest_of_word[0]
                    rest_of_word = rest_of_word[1:]

            translated_words.append(rest_of_word + consonants + "ay")

    return " ".join(translated_words)