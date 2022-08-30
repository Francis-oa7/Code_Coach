'''This program encodes your message.It replaces each alphabeth in your message with-'
it's opposite position alphabeth in order'''
alpha = {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n'}
rev = list(alpha.values())
rev1 = list(alpha.keys())
te_t = input("Message:").lower()
text = ''.join((i for i in te_t if(i.isalpha() or i.isspace())))
print('\nEncrypted message:')
 
def sec():
 s_message = ''
 for c in text:
     if c != ' ':
      if c in alpha:
        s_message+=alpha[c]
      else:
       s_message+=rev1[rev.index(c)] 
     else:
      if c == " ":
       s_message+=' '
 return s_message      

print(sec())
    # Works