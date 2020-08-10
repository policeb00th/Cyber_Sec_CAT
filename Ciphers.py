from pycipher import Vigenere
def Caesar(text,s):
    result = ""
   # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      return result
def vigenere(Key,String):
    vig=Vigenere(Key)
    encode=vig.encipher(String)
    return encode

def Row_transpose(key,text):
    key=list(key)
    ordered=[i for i in key]
    matrix=[]
    for i in range(len(key)):
        key[i]=int(key[i])
    for i in range(0,len(text),len(key)):
        matrix.append(list(text[i:i+len(key)]))
    print(matrix)
    for i in range(len(key)):
        temp=""
        for j in matrix:
            temp+=j[i]
        ordered[key[i]-1]=temp
    final=""
    for j in ordered:
        final+=j
    print(ordered)
