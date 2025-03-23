############# DO NOT DELETE THESE LINES OF CODE ######################
KEYPAD = {'0':'', '1':'', '2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', 
          '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}

##################   WRITE YOUR CODE HERE  ########################### 
def  getWords(keysPressed, current, words):
    if keysPressed=='':
        words.add(current)
        return words 
    letters = KEYPAD[keysPressed[0]]
    keysPressed = keysPressed.replace(keysPressed[0], '')
    if letters == '':
        getWords(keysPressed, current, words)
    else:
        for i in range (len(letters)):
            #current = current + letters[i]
            getWords(keysPressed, current+letters[i], words)

def  t9Words(keysPressed):
    words = set()
    current = ''
    getWords(keysPressed, current, words)
    return words