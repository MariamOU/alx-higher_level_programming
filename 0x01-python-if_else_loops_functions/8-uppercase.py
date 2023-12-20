#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if 'a' <= character <= 'z':
            return chr(ord(character) - 32)
        else:
            return character
