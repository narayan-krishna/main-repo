

def word_to_pig(chosen_word):
    vowels = 'aeiou'
    consonants = 'qwrtypsdfghjklzxcvbnm'
    new_string = ""
    for characters in chosen_word.lower():
        if characters in consonants:
            new_string += chosen_word[1::] + characters + "ay"
            break
        if characters in vowels:
            new_string += chosen_word + "yay"
            break
    return new_string

print(word_to_pig("cole"))
print(word_to_pig("Cole"))
print(word_to_pig("Attack"))
