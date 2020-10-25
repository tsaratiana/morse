# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 18:04:14 2020

@author: Tsara
"""

import tkinter as tk
import time
import sys

# Dictionaries

morse_dict = { 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 
              'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 
              'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 
              'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', 
              
              'é':'..-..', 'è':'.-..-', 'à':'.--.-', 'ç':'-.-..',
              
              '!':'-.-.--', '?':'..--..', ',':'--..--', "'":'.----.', '.':'.-.-.-',
              '(':'-.--.', ')':'-.--.-', '=':'-...-', '-':'-....-', '_':'..--.-',
              '@':'.--.-.', ':':'---...', ';':'-.-.-.', '+':'.-.-.', '/':'-..-.', 
              '&':'.-...', '$':'...-..-', '"':'.-..-.', 
              
              '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
              '6':'-....', '7':'--...', '8':'---..', '9':'----.', 
               }

morse_code = {'wait':'.-...', 'understood':'...-.', 'end':'...-.-', 'error':'........', 'starting signal':'-.-.-' }

morse_dict_words = {'a':'allo', 'b':'bonaparte', 'c':'coca cola', 'd':'dos dane', 'e':'eh', 'f':'farandole', 'g':'goldorak', 
              'h':'himalaya', 'i':'ici', 'j':'jai gros bobo', 'k':'korridor', 'l':'limonade', 'm':'moto', 'n':'noel', 
              'o':'ostrogoth', 'p':'philosophe', 'q':'quococorico', 'r':'revolver', 's':'sardine', 't':'thon', 'u':'union', 
              'v':'vegetation', 'w':'wagon post', 'x':'xtrocadero', 'y':'yoshimoto', 'z':'zorro est la'
              }

morse_dict_alpha = { 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 
              'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 
              'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 
              'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..'
              }

# Definitions

def decoration():
    print("\n**********************************************************")
    print("\tWelcome to my morse code decrytor/encryptor!")
    print("\t(Supports English and most latin languages")
    print("**********************************************************\n")
    
    print('Note: "ï" and "œ" cannot be encrypted or decrypted.\n\n')
    
def put_message():
    print(list(morse_code.keys())[list(morse_code.values()).index('-.-.-')].capitalize(),"...")
    message = input("*Enter your message: ")
    return(message) 
    
    
def encrypt(message):  
    print(list(morse_code.keys())[list(morse_code.values()).index('...-.')].capitalize())
    print(list(morse_code.keys())[list(morse_code.values()).index('.-...')].capitalize(),"...")
    
    output_enc = '' # empty output
    message = message.lower() # message forced in lower case
    
    for letter in message:
        if letter != ' ':
            output_enc += morse_dict[letter]+' '
        else:
            output_enc += '/ ' # word separation

    return(output_enc)
    
    
def decrypt(message):
    print(list(morse_code.keys())[list(morse_code.values()).index('...-.')].capitalize())
    print(list(morse_code.keys())[list(morse_code.values()).index('.-...')].capitalize(),"...")
    
    output_dec = '' # empty output
    text = ''
    message += ' ' # to decrypt the last letter/symbol
    
    for letter in message:
        if letter != ' ':
            i = 0
            text += letter # store letter
        
        else:
            i += 1 # new letter/symbol
            
            if i == 2 : # meaning new word = space instead of /
                output_dec += ' '
            else:
                output_dec += list(morse_dict.keys())[list(morse_dict.values()).index(text)]
                text = '' # reinitialisation to decrypt the next letter/symbol
    
    return(output_dec)
    
def tab_AW():
    print("\n\n********************************************************************")
    print("\t\t\tTo go further...")
    print("********************************************************************\n")
    print('To learn morse code, it is easier to use associated words. "a", "e", "i" are "." and "o" is "-".')
    print('Note: "u" is "." only for the letter U. If two vowels follow each other, we code only the second vowel.')
    print('\n\t\t-------------------------------------------------\n\t\t|\tLetter','\t\t|\tWord associated |\n\t\t-------------------------------------------------')
    
    for key, value in morse_dict_words.items():
        maxLength = 0
        maxLength = max(len(value), maxLength)
    
    for key, value in morse_dict_alpha.items(): # a voir
        maxLength2 = 0
        maxLength2 = max(len(value), maxLength2)
        
    for key, value in morse_dict_words.items():
        print("\t\t|\t",key.capitalize().ljust(maxLength),"\t|\t",value.capitalize().ljust(maxLength),"\t|")

    print("\t\t-------------------------------------------------\n")


def ex():
    answer = input("Do you want to exercise? (Y/N) ").upper()
    
    if answer == 'Y':
        print('Try to encrypt "Hello"!')
        time.sleep(10)
    
        print('The answer was: .... . .-.. .-.. ---')
    
        print('\nTry to decrypt "-... -.-- ."!')
        time.sleep(10)
        print('The answer was: Bye')
    elif answer == 'N':
        print("\n********************************")
        print("\t", morse_code.get('end'),"/",list(morse_code.keys())[list(morse_code.values()).index('...-.-')].capitalize())
        print("\tThank you!")
        print("*********************************\n")
    else:
        print('\n',morse_code.get('error'),"/",list(morse_code.keys())[list(morse_code.values()).index('........')].capitalize(),
                  ': Please type "Y" or "N" (lower or upper case)\n')
        sys.exit()
    
    
def main():
    decoration()
    
    again = True
    
    while again == True:
        answer = input("Do you want to decrypt or to encrypt something? (D/E): ").upper()
    
        if answer == 'E':
            message = put_message()
            output_enc = encrypt(message)
            print("\n*Message encrypted:", output_enc)
    
        elif answer == 'D':
            message = put_message()
            output_dec = decrypt(message)
            print("\n*Message decrypted:", output_dec.capitalize()) # With a capital at the beginning
        
        else:
            print('\n',morse_code.get('error'),"/",list(morse_code.keys())[list(morse_code.values()).index('........')].capitalize(),
                  ': Please type "D" or "E" (lower or upper case)')
           
            
        repeat = input("Again? (Y/N): ").upper()
        
        if repeat == "N":            
            tab_AW()
            ex()
            break
        
        elif repeat == "Y":
            continue
        else:
            print('\n',morse_code.get('error'),"/",list(morse_code.keys())[list(morse_code.values()).index('........')].capitalize(),
                  ': Please type "Y" or "N" (lower or upper case)')
            break
            
        
def test(): # a voir
    a=dict()
    for key2, value2 in morse_dict_alpha.items():
        a=value2
    a=(morse_dict_alpha.get('a'),morse_dict_alpha.get('b'),morse_dict_alpha.get('c'))   
        
    print(a)


# main
    
if __name__ == '__main__':
    main()