from display import *
from draw import *
from math import pi

screen = new_screen()
color = [ 250, 100, 0 ]



edge = [[],
        [],
        [],
        []]
x = XRES/2
y = YRES/2
r = 100

matrix = [[],[], [],[]]
add_edge(matrix, 20, 20, 1, 20, 50, 1)
add_edge(matrix, 20, 50, 1, 50, 50, 1)
add_edge(matrix, 50, 50, 1, 50, 20, 1)
add_edge(matrix, 50, 20, 1, 20, 20, 1)

add_edge(matrix, 200, 200, 1, 200, 250, 1)
add_edge(matrix, 200, 250, 1, 250, 250, 1)
add_edge(matrix, 250, 250, 1, 250, 200, 1)
add_edge(matrix, 250, 200, 1, 200, 200, 1)

add_edge(matrix, 100, 100, 1, 100, 250, 1)
add_edge(matrix, 100, 250, 1, 250, 250, 1)
add_edge(matrix, 250, 250, 1, 250, 100, 1)
add_edge(matrix, 250, 100, 1, 100, 100, 1)

edge[0].extend(matrix[0])
edge[1].extend(matrix[1])
edge[2].extend(matrix[2])
edge[3].extend(matrix[3])

    
for n in xrange(50):
    trans_matrix = matrix_mult(
        matrix_mult(make_translate(x,y,0), make_rotZ(pi/4)),
        make_translate(-x,-y,0))
    edge = matrix_mult(trans_matrix, edge)
    draw_lines(edge, screen, color)
    
    
display(screen)
