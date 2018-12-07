import random

def shuffle_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def mobileNoGenerator():
    mobileInitials = ['99', '98', '97', '86']
    mobileEnd = '1234567890'
    print(mobileInitials[random.randint(0, len(mobileInitials) - 1)] + mobileInitials[random.randint(0, len(mobileInitials) - 1)] + shuffle_word(mobileEnd)[:6])

def nameGenerator():
    charSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(shuffle_word(charSet)[:5] + ' ' + shuffle_word(charSet)[:6])




nameGenerator()
mobileNoGenerator()
