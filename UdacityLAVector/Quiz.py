from Vector import Vector

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

# dot_product_and_angle()
# parallel_and_orthogonal_vectors()
# projecting_vectors()
cross_products()