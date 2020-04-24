'''
Years after the Ishval Civil War, the Ishvalan refugees have now found a safe place for themselves which is a
rectangular piece of land, surrounded by fences.

The land can be thought of as a 2d grid which extends N units vertically and M units horizontally. It is
divided into N horizontal rows, which are numbered from 1 to N, as you move from top to bottom and into
M vertical columns numbered from 1 to M, from left to right.

There are X rivers flowing in a horizontal direction, each flowing in a different row and covering the
entire row. Similarly, there are Y rivers flowing in a vertical direction, each flowing in a different
column and covering the entire column.

The people want to build houses of dimensions S×S on the remaining land.

What is the maximum number of houses of the given dimensions that could be built on the remaining land,
such that no part of any house is in a river and no two houses overlap?
'''

'''
solve_map(8, 7, [5], [4, 8], 2, 2)

OOO R OOO R
OOO R OOO R
OOO R OOO R
OOO R OOO R

RRR R RRR R

OOO R OOO R
OOO R OOO R
'''
import itertools
from math import floor

def solve_map(x_input, y_input, h_rivers, v_rivers, house_w, house_h):
    # get a width and height for all non-river areas in the map.
    areas = get_areas_and_dimensions(x_input, y_input, h_rivers, v_rivers)
    print(areas)
    num_houses = 0

    # loop through each area and get the number of houses that will fit
    for area in areas:
        num_houses += get_houses_in_area(area, house_w, house_h)

    return num_houses

def get_houses_in_area(area, house_w, house_h):
    # for each area find the number of houses that will fill the width and height
    # example if a house is 2 units wide and the area is 4 units - 4/2 = 2 house widths will fit
    houses_in_width = floor(area[0] / house_w)
    houses_in_height = floor(area[1] / house_h)

    # return the number of houses that fit in width and height
    # example 2 house widths fit, and 1 house heights fit - 2 * 1 = 2 houses total
    return houses_in_width * houses_in_height


def get_areas_and_dimensions(x_input, y_input, h_rivers, v_rivers):
    # get a list of widths and heights that do not have rivers
    horizontal_widths = get_dimenstions(x_input, v_rivers)
    vertical_heights = get_dimenstions(y_input, h_rivers)

    # create an array of tuples with the width and height of each area
    areas = list(itertools.product(horizontal_widths, vertical_heights))

    return areas


def get_dimenstions(dim, rivers):
    # gives the dimensions of a non-river area. e.g.
    # dimension size is given by a border and a river or two rivers
    # I just take the difference of the borders
    dimensions = []

    # first dimension is from 1 to the first river
    dimensions = append_non_zero(dimensions, rivers[0] - 1)

    # each remaining dimension is the difference between each river
    for river_initial, river_final in zip(rivers[0::], rivers[1::]):
        # we could still append 0 dimension areas to the array I just don't want to.
        dimensions = append_non_zero(dimensions, river_final - river_initial - 1)

    # get last dimension which is between the end
    dimensions = append_non_zero(dimensions, dim - rivers[-1])

    return dimensions


def append_non_zero(arr, to_append):
    if to_append != 0:
        arr.append(to_append)

    return arr


print(solve_map(8, 7, [5], [4, 8], 2, 2))
print(solve_map(8, 8, [2], [5], 2, 2))