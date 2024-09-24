from textblob import TextBlob,Word
wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print("Tags",wiki.tags)
print("Words",wiki.words)
print("Correct Words",  wiki.correct())



print("###########################")
print()

#word=Word("WAN")
#print("Defination",word.definitions)

print("###########################")


text = ''
blob = TextBlob(text)
sentiment=blob.sentiment
print(sentiment.polarity)







