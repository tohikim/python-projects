print('Project -  Crypto')

def enigma_light():
    keys = "abcdefghijklmnopqrstuvwxyz !"
    values = keys[-1]+keys[0:-1]

    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))

    msg = input('Enter your secret message: ')
    mode = input("Crypto mode: encode (e) OR decrypt as default: ")
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
    
    return new_msg.capitalize()
print(enigma_light())