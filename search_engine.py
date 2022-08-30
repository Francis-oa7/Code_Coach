a = "Word found"
b = "Word not found"
def search(x,y):
    if str(x).count(y) == 0:
        return b
    else:
        return a    
text = input("text:") 
word = input("word:")
print(search(text,word))

 
 
