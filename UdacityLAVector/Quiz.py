from Vector import Vector
from Line import Line
from Plane import Plane
from LinearSystem import LinearSystem

# Quiz: Coding Magnitude & Direction
def magnitude_and_direction():
    v = Vector([-0.221, 7.437])
    print("magnitude is {0}".format(v.magnitude()))

    v = Vector([8.813, -1.331, -6.247])
    print("magnitude is {0}".format(v.magnitude()))

    v = Vector([5.581, -2.136])
    print("normilized vector is {0}".format(v.normalize()))

    v = Vector([1.996, 3.108, -4.554])
    print("normilized vector is {0}".format(v.normalize()))

# Quiz: Coding Dot Product & Angle
def dot_product_and_angle():
    v = Vector([7.887, 4.138])
    w = Vector([-8.802, 6.776])
    print("Dot product(Inner product) of v * w is {0}".format(v.dot_product(w)))

    v = Vector([-5.955, -4.904, -1.874])
    w = Vector([-4.496, -8.755, 7.103])
    print("Dot product(Inner product) of v * w is {0}".format(v.dot_product(w)))

    v = Vector([3.183, -7.627]);
    w = Vector([-2.668, 5.319]);
    print("Angel between v and w is {0} radians".format(v.angle_with(w)))

    v = Vector([7.35, 0.221, 5.188]);
    w = Vector([2.751, 8.259, 3.985]);
    print("Angel between v and w is {0} degrees".format(Vector.radian_to_degree(v.angle_with(w))))

# Quiz: Parallel and Orthogonal Vectors
def parallel_and_orthogonal_vectors():
    v = Vector(['-7.579', '-7.88'])
    w = Vector(['22.737', '23.64'])
    print("Vectors {0} and {1} is parallel. It is a {2} statement.\n".format(v, w, v.is_parallel_with(w)));
    print("Vectors {0} and {1} is orthogonal. It is a {2} statement.\n".format(v, w, v.is_orthogonal_with(w)));

    v = Vector(['-2.029', '9.97', '4.172'])
    w = Vector(['-9.231', '-6.639', '-7.245'])
    print("Vectors {0} and {1} is parallel. It is a {2} statement.\n".format(v, w, v.is_parallel_with(w)));
    print("Vectors {0} and {1} is orthogonal. It is a {2} statement.\n".format(v, w, v.is_orthogonal_with(w)));

    v = Vector(['-2.328', '-7.284', '-1.214'])
    w = Vector(['-1.821', '1.072', '-2.94'])
    print("Vectors {0} and {1} is parallel. It is a {2} statement.\n".format(v, w, v.is_parallel_with(w)));
    print("Vectors {0} and {1} is orthogonal. It is a {2} statement.\n".format(v, w, v.is_orthogonal_with(w)));

    v = Vector(['2.118', '4.827'])
    w = Vector(['0', '0'])
    print("Vectors {0} and {1} is parallel. It is a {2} statement.\n".format(v, w, v.is_parallel_with(w)));
    print("Vectors {0} and {1} is orthogonal. It is a {2} statement.\n".format(v, w, v.is_orthogonal_with(w)));

# Quiz: Projecting Vectors
def projecting_vectors():
    v = Vector(['3.039', '1.879'])
    b = Vector(['0.825', '2.036'])
    print("projection {0} onto {1} is {2}\n".format(v, b, v.component_parallel_to(b)))
    
    v = Vector(['-9.88', '-3.264', '-8.159'])
    b = Vector(['-2.155', '-9.353', '-9.473'])
    print("component of {0} orthogonal to {1} is {2}\n".format(v, b, v.component_orthogonal_to(b)))

    v = Vector(['3.009', '-6.172', '3.692', '-2.51'])
    b = Vector(['6.404', '-9.144', '2.759', '8.718'])
    print("{0} = {1} + {2}\n".format(v, v.component_parallel_to(b), v.component_orthogonal_to(b)))

# Quiz: Cross Products
def cross_products():
    v = Vector(['8.462', '7.893', '-8.187'])
    w = Vector(['6.984', '-5.975', '4.778'])
    print("{0} cross {1} is {2} \n".format(v, w, v.cross_product(w)))

    v = Vector(['-8.987', '-9.838', '5.031'])
    w = Vector(['-4.268', '-1.861', '-8.866'])
    print("area of parallelogram spanned by {0} and {1} is {2}\n".format(v, w, v.area_of_parallelogram_with(w)))
    
    v = Vector(['1.5', '9.547', '3.691'])
    w = Vector(['-6.007', '0.124', '5.772'])
    print("area of triangle spanned by {0} and {1} is {2}\n".format(v, w, v.area_of_triangle_with(w)))

# Quiz: Intersection of Lines in 2D
def intersection_of_lines_in_2D():
    l1 = Line(normal_vector = Vector(['4.046', '2.836']), constant_term = '1.21')
    l2 = Line(normal_vector = Vector(['10.115', '7.09']), constant_term = '3.025')
    print("{0} intersects with {1} in ".format(l1, l2) + str(l1.intersection_with(l2)))

    l1 = Line(Vector(['7.204', '3.182']), '8.68')
    l2 = Line(Vector(['8.172', '4.114']), '9.883')
    print("{0} intersects with {1} in ".format(l1, l2) + str(l1.intersection_with(l2)))

    l1 = Line(Vector(['1.182', '5.562']), '6.744')
    l2 = Line(Vector(['1.773', '8.343']), '9.525')
    print("{0} intersects with {1} in ".format(l1, l2) + str(l1.intersection_with(l2)))

# Quiz: Planes in 3 Dimensions
def planes_in_3D_print_outcomes(p1, p2):
    str = "{0} and {1} are ".format(p1, p2)
    if p1 == p2:
        str += "equal"
    elif p1.is_parallel_with(p2):
        str += "parallel but unequal"
    else:
        str += "not parallel"
    print(str)

def planes_in_3D():
    p1 = Plane(normal_vector = Vector(['-0.412', '3.806', '0.728']), constant_term = '-3.46')
    p2 = Plane(normal_vector = Vector(['1.03', '-9.515', '-1.82']), constant_term = '8.65')
    planes_in_3D_print_outcomes(p1, p2)

    p1 = Plane(normal_vector = Vector(['2.611', '5.528', '0.283']), constant_term = '4.6')
    p2 = Plane(normal_vector = Vector(['7.715', '8.306', '5.342']), constant_term = '3.76')
    planes_in_3D_print_outcomes(p1, p2)

    p1 = Plane(normal_vector = Vector(['-7.926', '8.625', '-7.212']), constant_term = '-7.952')
    p2 = Plane(normal_vector = Vector(['-2.642', '2.875', '-2.404']), constant_term = '-2.443')
    planes_in_3D_print_outcomes(p1, p2)

# Quiz: The Linear System : Coding Row Operations
def linear_system_coding_row_operations():
    p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
    p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
    p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

    s = LinearSystem([p0,p1,p2,p3])
    s.swap_rows(0,1)
    if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
        print('test case 1 failed')

    s.swap_rows(1,3)
    if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
        print('test case 2 failed')

    s.swap_rows(3,1)
    if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
        print('test case 3 failed')

    s.multiply_coefficient_and_row(1,0)
    if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
        print('test case 4 failed')

    s.multiply_coefficient_and_row(-1,2)
    if not (s[0] == p1 and
            s[1] == p0 and
            s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
            s[3] == p3):
        print('test case 5 failed')

    s.multiply_coefficient_and_row(10,1)
    if not (s[0] == p1 and
            s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
            s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
            s[3] == p3):
        print('test case 6 failed')

    s.add_multiple_times_row_to_row(0,0,1)
    if not (s[0] == p1 and
            s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
            s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
            s[3] == p3):
        print('test case 7 failed')

    s.add_multiple_times_row_to_row(1,0,1)
    if not (s[0] == p1 and
            s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
            s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
            s[3] == p3):
        print('test case 8 failed')

    s.add_multiple_times_row_to_row(-1,1,0)
    if not (s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
            s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
            s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
            s[3] == p3):
        print('test case 9 failed')


# dot_product_and_angle()
# parallel_and_orthogonal_vectors()
# projecting_vectors()
# cross_products()
# intersection_of_lines_in_2D()
# planes_in_3D()
linear_system_coding_row_operations()