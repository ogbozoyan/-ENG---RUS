import string
def switch_engrus(s1s2):
    masRUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    masENG = "f,dult`;pbqrkvyjghcnea[wxio]sm'"'.zF<DULT~:PBQRKVYJGHCNEA{WXIO}SM">Z'
    enc = s1s2.maketrans(masENG,masRUS)
    return s1s2.translate(enc)
def switch_ruseng(s1s2):
    masRUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    masENG = "f,dult`;pbqrkvyjghcnea[wxio]sm'"'.zF<DULT~:PBQRKVYJGHCNEA{WXIO}SM">Z'
    enc = s1s2.maketrans(masRUS,masENG)
    return s1s2.translate(enc)

print("Choose mode: \n"
      "1 - Eng to Rus \n"
      "2 - Rus to Eng \n")
mode1=input()
while 1:
    if mode1 == '1':
        print("1 - from keyboard \n"
              "2 - from file \n"
              "q - to quit")
        while 1:
            mode = input('Select your mode : ')
            if mode == '1':
                print('write text: ')
                text=input()
                for j in text:
                    res =  switch_engrus(text) 
                print(res,end='\n')
            elif mode == '2':
                with open("text.txt") as f:
                    text = f.read()
                for j in text:
                    res =  switch_engrus(text) 
                print(res,end='\n')
            elif mode == 'q':
                print("shutting down...")
                quit()
    elif mode1 =='2':
        print("1 - from keyboard \n"
              "2 - from file \n"
              "q - to quit")
        while 1:
            mode = input('Select your mode : ')
            if mode == '1':
                print('write text: ')
                text=input()
                for j in text:
                    res =  switch_ruseng(text) 
                print(res,end='\n')
            elif mode == '2':
                with open("text.txt") as f:
                    text = f.read()
                for j in text:
                    res =  switch_ruseng(text) 
                print(res,end='\n')
            elif mode == 'q':
                print("shutting down...")
                quit()
    else:
        print("Wrong operation")
