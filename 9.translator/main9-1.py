# import googletrans 

# translator = googletrans.Translator() 

# str1 = "행복하세요" 
# result1 = translator.translate(str1, dest='en', src='auto') 
# print(f"행복하세요 => {result1.text}") 

# str2 = "I am happy" 
# result2 = translator.translate(str2, dest='ko', src='en') 
# print(f"I am happy => {result2.text}")

import googletrans

translator = googletrans.Translator()

str1 = "This is some text to translate"

try:
    result1 = translator.translate(str1, dest='en', src='auto')
    print(f"{str1} => {result1.text}")
except AttributeError:
    print("Error: Translation failed. Please try again later.")