# 
import string
a_ru = ord('а')
alfabet_ru = ''.join([chr(i) for i in range(a_ru,a_ru+32)])
alfabet_ua = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
alfabet_en = string.ascii_lowercase

def alfabetPrint(RepeatLetter, alfabetType):
    returnString = ''
    lenAlfabet = len(alfabetType)
    returnString = ', '.join([RepeatLetter * (i.upper()+i) for i in alfabetType]) #RepeatLetter * i.upper() + " " + RepeatLetter * i + " " + 
    print(returnString)

# print(string.ascii_letters)
# print(alfabet_ru)
# print(alfabet_ua)
print(string.digits)
print(" - RU - ")

alfabetPrint(2, alfabet_ru)
print(" - UA - ")
alfabetPrint(5, alfabet_ua)
print(" - EN - ")
alfabetPrint(4, alfabet_en)
