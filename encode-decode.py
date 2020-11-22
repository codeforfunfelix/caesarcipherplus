#This is my first full python program, and I'm very proud! Made on 11/21/2020

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.,(): /;[]{}|<>-_!@#$%^&*"
letters = list(letters)

def getFunc():
    print("What do you want to do?: (Answers: Encode, Decode)")
    func = input()
    if func == "Encode":
        print("Encoded Message: "+ encode())
    elif func == "Decode":
        print("Decoded Message: "+ decode())
    else:
        print("Please enter a valid answer.")
        getFunc()

def encode():
    print("What do you want to encode?")
    text = list(input())
    code = ""
    for i in range(len(text)):
        for j in range(len(letters)):
            if text[i] == letters[j]:
                code += letters[j + 1]
    return code

def decode():
    print("What do you want to decode?")
    code = list(input())
    text = ""
    for i in range(len(code)):
        for j in range(len(letters)):
            if code[i] == letters[j]:
                text += letters[j - 1]
    return text

getFunc()
