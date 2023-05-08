# s language
# I HAVE LEARNT THIS LANGUAGE FROM SNEHA MUKHERJEE


blank = ""

def word_change():
    i_w = input("Enter a word which we are going to code in S language: ")
    if i_w == "":       #initial word
        return blank
    n_w = 's' + i_w[1:] + i_w[0:2]+ 'n'     #new word
    return n_w

def word_list(i_w):
    if i_w == "":       #initial word
        return blank    
    else: 
        n_w = 's' + i_w[1:] + i_w[0:2]+ 'n'     #new word
    return n_w

def in_list(list):
    length = len(list)
    for i in range (0,length):
        new_string = word_list(lst[i])      #taking each word from the list and converting
        print(new_string , end = " ")
        
while True:
    x = input("Enter 's' if you want to type sentence enter 'w' if you want to type a word , type 'x' if you want to cancel the program:  ")
    if x == 'x' :
        print("Good working with you !")
        break
    
    elif x  == 'w':
        print(word_change())
        ask = input("Do you want to convert more word (y or n)..")
        if ask == 'y':
            continue
        else:
            break
        
    elif x == 's':
        sen = input("Type a sentence: ")
        lst = sen.split(" ")
        in_list(lst)
        print()
        ask = input("Do you want to convert more sentences (y or n)..")
        if ask == 'y':
            continue
        else:
            break

    else:
        print("you are a idiot who dont read the instruction!")
        








