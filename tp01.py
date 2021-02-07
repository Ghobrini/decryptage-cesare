def decryptage (valeur):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    valeur.lower()
    #valeur.replace(" ","." )
    dict_alphabet={
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0
    }

    #number of repetion of every letter
    for item in valeur:
        for key,value in dict_alphabet.items():
            if key == item:                
                dict_alphabet[key]+= 1

    
    mx = None
    num = 0
    #the letter that is repeated the moste
    for key,value in dict_alphabet.items():
        if value > num:
            num = value
            mx = key

    num = 0
    #initialise the alphabet
    for key,value in dict_alphabet.items():
        dict_alphabet[key] = num
        num = num + 1
    
    #place of the moste repeated letter
    for key,value in dict_alphabet.items():
        if key == mx:
            num = value
    
    #value of the shift
    if num < 4:
        num = 4 - num        
    else :
        num =  num - 4
        num = 25 - num
    
    #decodage 
    lst=[]
    for item in valeur :
        increment = 0
        for itm in alphabet:             
            if itm == item :
                increment = (increment + num ) % 25 
                #item = alphabet[increment]
                lst.append(alphabet[increment])
                
                break
                #so it wouldn't loop again and toche another variable 
            elif item == ' ':
                lst.append(' ')
                break
            increment = increment +1
    #transforme it from a list to a string
    lst= ''.join(lst)
    return lst 

valeur = input("donne votre paragraphe chifré:")
print ("le paragraphe dechifré :")

print ( str(decryptage (valeur)) )

