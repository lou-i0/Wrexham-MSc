import re, string

word_list = []
word_dict = {}
key_list = []
count = 0
word = ""

# text from http://www.dummytextgenerator.com/#jump
in_text_string = open('exampletext.txt',"r").read().lower()

word_list = re.split(r'[^a-zA-z\_\-]+',in_text_string)

#print(word_list)

for word in word_list:
    count = count +1
    if word in word_dict:
        word_dict[word] = word_dict[word] + ',' + str(count)
    else:
        word_dict[word] = str(count)

key_list = list(word_dict)

print(key_list)

key_list.sort()

    
