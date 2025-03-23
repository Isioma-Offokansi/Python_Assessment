import math

def  centreOfMass(spheres):
    """
    Function to find the centre of mass of a set of spheres.

    Args:
        spheres (set): the set of tuples containing the x coordinate, y coordinate, z coordinate, radius, and unit mass of a sphere.

    Raises:
        ValueError: the sphere set is empty
        ValueError: the radius of a sphere is less than or equal to zero
        ValueError: the unit mass of a sphere is less than or equal to zero

    Returns:
        tuple: the a tuple of the centre of mass of the spheres
    """
    PI = 3.14159
    if len(spheres)==0:
        raise ValueError ('The sphere set is empty.')
    cX = 0
    cY = 0
    cZ = 0
    total_mass = 0
    sphere_list = list(spheres)
    for i in range (len(spheres)):
        if sphere_list[i][3]<=0:
            raise ValueError ('Radius of a sphere is less than or equal to 0 and therefor invalid.')
        elif sphere_list[i][4]<=0:
            raise ValueError ('Unit mass of a sphere is less than or equal to 0 and therefor invalid.')
        else:
            mass = (4/3)*sphere_list[i][4]*math.pi*(sphere_list[i][3]**3)
            cX += sphere_list[i][0]*mass
            cY += sphere_list[i][1]*mass
            cZ += sphere_list[i][2]*mass
            total_mass += mass
    cX = cX/total_mass
    cY = cY/total_mass
    cZ = cZ/total_mass
    cen_mass = (cX, cY, cZ)
    return cen_mass
