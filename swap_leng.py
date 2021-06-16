import string
def switch(s1s2):
    masRUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    masENG = "f,dult`;pbqrkvyjghcnea[wxio]sm'"'.zF<DULT~:PBQRKVYJGHCNEA{WXIO}SM">Z'
    enc = s1s2.maketrans(masENG,masRUS)
    s3 = s1s2.translate(enc)
    return s3
print("1 - from keyboard \n"
      "2 - from file")
mode = input('Select your mode : ')
if mode == '1':
    print('write text: ')
    text=input()
    for j in text:
        res =  switch(text) 
    print(res,end='')
elif mode == '2':
    with open("text.txt") as f:
        text = f.read()
    for j in text:
        res =  switch(text) 
    print(res,end='')
