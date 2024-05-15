import re
import nltk

def write_a_expressions(text: str):
    email_word = re.findall(r'\b\w*@fpt.edu.vn\b', text)
    return email_word

if __name__ == "__main__":
    text = 'Please contact us at contact@fpt.edu.vn for further information. You can also give feedback at feedback@fpt.edu.vn'
    answers =  write_a_expressions(text)
    print(answers)