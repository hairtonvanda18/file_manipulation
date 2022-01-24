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

pares ={}
for word in words2:
    if word not in pares:
        pares[word] = 1
    else:
        pares[word] += 1
#aux=pares.items()
#for item in aux:
paresdecres =sorted(pares.items(),key=lambda item: item[1],reverse=True) 
paresdecres = paresdecres[3:]
b= open("resultado.csv","w",encoding="utf8")
for h,v in paresdecres:
    b.write(f'"{v}";"{h}";"";""\n')
b.close()