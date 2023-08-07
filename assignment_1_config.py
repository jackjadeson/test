
#-----Module Description - Drawing Canvas Configuration--------------#
#
#  This module contains functions needed for Assignment 1 in
#  QUT's teaching unit IFB104 "Building IT Systems".  You should put
#  a copy of this file in the same folder as your solution to the
#  assignment.  The necessary elements will then be imported
#  into your program automatically.
#
#  NB: Do NOT submit this file with your solution.  Changes made to
#  this module will have no effect when your assignment is graded
#  because the markers will use their own copy of the file.  If your
#  solution relies on changes made to this file it will fail to work
#  when assessed.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section defines constants and imports necessary functions
# used for creating the drawing canvas.
#

# Import standard Python functions needed to support this module.
from turtle import *

# Define the length of the sides of the cells. All other dimensions
# for the drawing canvas are calculated relative to this value.
cell_size = 80 # pixels
assert cell_size >= 60, 'Cells must be at least 60x60 pixels'

# Define the width and height of the grid.
grid_width = 10 # cells
grid_height = 7 # cells
assert grid_width % 2 == 0, 'Grid width must be even'
assert grid_height % 2 != 0, 'Grid height must be odd'

# Define values that determine the size of the
# drawing canvas, proprtional to the given cell size.
x_margin = cell_size * 3 # pixels, left/right margin
y_margin = cell_size * 1 # pixels, top/bottom margin
canvas_height = grid_height * cell_size + y_margin * 2
canvas_width = grid_width * cell_size + x_margin * 2

#
#--------------------------------------------------------------------#



#-----Functions for Maintaining the Drawing Canvas-------------------#
#
# The functions in this section are called by the assignment template
# to manage the drawing canvas used by your program.  Your code must
# not call these functions and your code must not create its own
# drawing canvas.
#

# Set up the canvas and draw the background for the overall image
#
def create_drawing_canvas(canvas_title = "Put your solution's title here",
                          background_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          write_instructions = True):

    # Set up the drawing canvas with enough space for the grid and
    # surrounding margins
    setup(canvas_width, canvas_height)
    bgcolor(background_colour)

    # Put a title on the canvas
    title(canvas_title)

    # Draw the grid as quickly as possible
    tracer(False)

    # Get the pen ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Choose a font for the text around the grid
    grid_font = ('Arial', cell_size // 4, 'normal')

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Write each of the labels on the x axis
        penup()
        y_offset = cell_size // 2 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2),
                 bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = grid_font)

        # Write each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 5, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset,
                 bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = grid_font)

        # Mark the two special cells (assuming the grid's
        # width is even)
        goto(-1.5 * cell_size, 0)
        dot(cell_size // 6)
        goto(1.5 * cell_size, 0)
        dot(cell_size // 6)

        # Highlight the centre line (assuming the grid's
        # height is odd)
        goto(0, cell_size * (grid_height / 2)) # top centre
        setheading(270) # south
        width(6)
        pendown()
        forward(cell_size * grid_height)
        penup()

    # Optionally write instructions to the programmer
    if write_instructions:
        # Left
        goto(-(grid_width // 2 + 1.5) * cell_size, -cell_size)
        write("Draw and\ndescribe\nthe first\ncompetitor\nhere",
              align = 'center', font = grid_font)    
        # Right
        goto((grid_width // 2 + 1.5) * cell_size, -cell_size)
        write("Draw and\ndescribe\nthe second\ncompetitor\nhere",
              align = 'center', font = grid_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)
        


# End the program and release the drawing canvas back to the
# host operating system
#
def release_drawing_canvas(signature,
                           text_colour = 'slate grey'):
    
    # Ensure any student drawing still in progress is displayed
    # completely
    tracer(True)
        
    # Sign the canvas with the student's name
    signature_font = ('Comic Sans MS', cell_size // 4, 'bold')
    color(text_colour)
    penup()
    goto((cell_size * grid_width) // 2,
         (cell_size * (grid_height + 0.1)) // 2)
    write('Visualisation by ' + signature + ' ',
          align = 'right', font = signature_font)    
    
    # Hide the cursor and release the window to the host
    # operating system
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#
