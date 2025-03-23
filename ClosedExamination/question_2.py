import math

def collide(objectA, objectB):
    lenA = len(objectA)
    lenB = len(objectB)
    A_list = list(objectA)
    B_list = list(objectB)
    for i in range (lenA):
        if len(A_list[i])!=4:
            raise ValueError ('The tuple for object A or object B does not have the correct number of elements.')
        elif (A_list[i][3]<=0):
            raise ValueError('The radius of object A or object B is 0 and therefore invalid.')
        for j in range (lenB):
            if len(B_list[j])!=4:
                raise ValueError ('The tuple for object A or object B does not have the correct number of elements.')
            elif (B_list[j][3]<=0):
                raise ValueError('The radius of object A or object B is 0 and therefore invalid.')
            else: 
                total_radius = A_list[i][3]+B_list[j][3]
                distance = math.sqrt(pow(A_list[i][0]-B_list[j][0], 2)+pow(A_list[i][1]-B_list[j][1], 2)+pow(A_list[i][2]-B_list[j][2], 2))
                if (total_radius>distance):
                    return True
    return False


