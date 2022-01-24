import string 

book = open("files/book.txt","r", encoding="utf8")
words = book.read().lower()#.split()
fstop = open("files/stop_words_portuguese.txt","r",encoding="utf8")
stopwords = fstop.read().lower().split("\n")
for punc in string.punctuation:
    words = words.replace(punc,"")
words = words.split() 
words2 = []
for word in words:
    if word in stopwords:
        continue
    words2.append(word)


print(words2)