import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def find_the_word(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        choose=input("Did you mean %s instead of %s?If yes enter Y, else enter N for No"%(get_close_matches(word,data.keys())[0],word))
        if choose.lower()=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif choose.lower()=="n":
            return "Word doesn't exist. Please check it..."
        else:
            return "Invalid entry..."
    else:
        return "Word doesn't exist. Please check it..."

word=input("Enter the word: ")
word_list=find_the_word(word)
if type(word_list)==list:
    count=1
    for i in word_list:
        print(str(count)+"."+i)
        count+=1
else:
    print(word_list)
