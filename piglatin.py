userInput = input("Enter word: ")

vowels = ['a','e','i','o','u']
def translate(userInput): 
    first = userInput[0]

    if first in vowels: 
         userInput = userInput.lower()
         userInput += "way" 
         return userInput
    else: 
        userInput = userInput.lower()

        for letter in userInput:
            if letter in vowels:
                index_value = userInput.index(letter)
                break

        userInput = userInput[index_value:] +userInput[:index_value]+ "ay" 
        return userInput 

print(translate(userInput))
