############# DO NOT DELETE THIS LINE OF CODE ######################
from invalidfileformatexception import InvalidFileFormatException

##################  WRITE YOUR CODE HERE ###########################
def readAdjacency(file_name):
    try:
        with open(file_name, 'r') as file: 
            text = file.read()
    except:
        raise FileNotFoundError ('The file does not exist')
    else:
        matrix= []
        string = ''
        row = []
        valid = ['0', '1', ' ', ',', '\n']
        for i in range (len(text)):
            if text[i] not in valid:
                raise InvalidFileFormatException ('The file contains invalid values')
            if text[i] != '\n':
                string += text[i]
            else:
                row = string.split(',')
                try:
                    matrix.append(list(map(int, row)))
                except:
                    raise InvalidFileFormatException ('The file has invalid formating')
                if len(matrix)>2 and len(matrix[len(matrix)-2])!=len(matrix[len(matrix)-1]):
                    raise InvalidFileFormatException ('The file has invalid formating')
                string = ''
        if len(string)>0:
            row = string.split(',')
            matrix.append(list(map(int, row)))
            string = ''
        if len(matrix) != len(matrix[0]):
            raise InvalidFileFormatException ('The file has invalid formating')
        else:
            return matrix
#print(readAdjacency('./data/missingvalue.csv'))
