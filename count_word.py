import jieba

do_uk=False 
excludes_china = [
]
includes_china=[
]
excludes_uk = []
includes_uk=[
]
excludes=excludes_china
if do_uk==True:
    excludes=excludes_uk
includes=includes_china
if do_uk==True:
    includes=includes_uk
stop_words = open("stopwords.txt", "r").readlines()
for word in stop_words:
    # print(word[:-1])
    excludes.append(word[:-1])
for item_group in includes:
    for item in item_group:
        jieba.add_word(item)
words_total=[]
file_count=4
if do_uk==True:
    file_count=4
for i in range(file_count): 
    if do_uk==True:
        file_name="uk_text"+str(i)+".txt"
    else:
        file_name="text"+str(i)+".txt"
    txt = open(file_name,"r").read()
    words = jieba.lcut(txt)
    for word in words:
        words_total.append(word.lower())
counts = {}
for word in words_total:
    if len(word) <= 1:
        continue
    else:
        rword = word
    if rword in counts:
        counts[rword] = counts[rword] + 1
    else:
        counts[rword] = 1
for word in excludes:
    if word in counts:
        del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
print("Include: ")
group_re={}
for word_group in includes:
    temp_count=0
    for word in word_group:
        if word in counts:
            temp_count=temp_count+counts[word]
    key_name=str(word_group)
    group_re[key_name]=temp_count
items = list(group_re.items())

items.sort(key=lambda x:x[1], reverse=True)
for i in range(len(items)):
    word, count=items[i]
    print(word,count)
print("=============")
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(len(items)):
    word, count=items[i]
    if count >=1:
        print(word,count)


