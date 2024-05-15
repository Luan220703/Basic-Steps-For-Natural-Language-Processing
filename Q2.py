import re

from nltk.tokenize import wordpunct_tokenize
def text_split(text: str) -> list:
    list_word =  wordpunct_tokenize(text)
    return list_word

if __name__ == "__main__":
    
    text = "She received the news of the discovery with equanimity"
    list_word = text_split(text)
    slice = []
    slice.append(list_word[-2])
    slice.append(list_word[-1])
    print(slice)
