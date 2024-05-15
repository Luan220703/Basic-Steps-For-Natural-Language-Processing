import nltk
# Print all words beginning with pe

# Print all words less than eight characters
def find_eight_letter_words(text):
    eight_letter_words = [word.lower() for word in text if len(word) < 8 and word.isalpha()]
    return eight_letter_words

if __name__ == "__main__":
    flowers = ['carnation','pendulum','pentunias','begonia','receptacle','hostas','pelorism','paperwhite']
    eight_letter_words = find_eight_letter_words(flowers)
    result = []
    for word in eight_letter_words:
        result.append(word)
    print(result)
      
