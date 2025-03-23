from typing import Counter


class Encoding:
    def __init__(self, binary_tree):
        self._encoding = binary_tree.copy()
    
    def decodeText(self, binary_code):
        length = len(binary_code)
        word = ''
        current = 0
        node_count = 0
        for i in range (length):
            if binary_code[i] != '1' and binary_code[i] != '0':
                raise ValueError ('Invalid symbol in binary code.')
            else:
                if int(binary_code[i]) == 0:
                    current = self._encoding[2*(node_count)+1]
                else:
                    current = self._encoding[2*(node_count)+2]
                if current == '':
                    node_count+=2
                elif current != None:
                    if self._encoding[2*(node_count+1)+1] == None and self._encoding[2*(node_count+1)+2] == None:
                        word += current
                        node_count = 0
                    else: 
                        raise ValueError ('Word did not finish of leaf of a binary tree.')
        if current == '':
            raise ValueError ('Missing bit.')
        return word
    
    def encodeText(self, plain_text):
        cipher = {}
        cipher_string = ''

        for i in self._encoding:
            if i != '' and i != None:
                num = self._encoding.index(i)
                b_code = ''
                while num>0:
                    if num%2 == 1:
                        b_code = '0' + b_code
                        num = (num-1)/2
                    else:
                        b_code = '1' + b_code
                        num = (num-2)/2
                cipher[i] = b_code
        for i in range (len(plain_text)):
            if plain_text[i] not in cipher:
                raise ValueError ('Symbol from tree not in dictionary.')
            else:
                cipher_string += cipher[plain_text[i]]
        return cipher_string
                
e = Encoding([  '', 
                '', '',
                'D', 'Y','A', 'B', 
                None, None, None, None, None, None, None, None])

print(e.encodeText('BAD'))