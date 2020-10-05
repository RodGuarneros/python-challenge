
print("""
------------------------------------------------------------------------------------------
                            Text analysis code
                                Starting...
------------------------------------------------------------------------------------------
""")

import os
import csv
import re # it is a hint re.split("(?<=[.!?]) +", paragraph) it is a regular expression operations 

letters_word = []
words_sentence = []
#Open the door

text = os.path.join("..","raw_data","paragraph_1.txt")

with open(text, "r", newline="") as filetext:
    textreader = filetext.readline()
    
    word_count = re.split(" ", textreader)
    word_count1 = len(word_count) + 1
    print(f"The number of words are: {word_count1}")
    
    sentence_count = re.split("(?<=[.!?]) +", textreader)
    print(f"The number of sentences are: {len(sentence_count)}")
    
    for word in word_count:
        letters_word.append(len(word))

print(f"The letter account for each word is: {letters_word}")
print(f"The words account for each sentence is: {words_sentence}")
    # for wds in textreader:
    #     #as we can see in the paragraph 
    #     criteria1 = textreader.split(" ")
               
        
        
        


        

#first of all, what is a word? we define it as following

    
    
    