# -*- coding: utf-8 -*-

#Checking which moves are possible to generate child nodes
def check_move_up(mat_input, MATRIX_SIZE):
   return True if mat_input.index(0) >= MATRIX_SIZE else False


def check_move_down(mat_input, MATRIX_SIZE, N_Board):
    return True if mat_input.index(0) < N_Board + 1 - MATRIX_SIZE else False


def check_move_left(mat_input, MATRIX_SIZE):
    return False if mat_input.index(0) % MATRIX_SIZE == 0 else True

def check_move_right(mat_input, MATRIX_SIZE):
    return False if mat_input.index(0) % MATRIX_SIZE == MATRIX_SIZE - 1 else True

#Move the blank tile upwards
def blank_tile_up(mat_input, MATRIX_SIZE):
    if check_move_up(mat_input, MATRIX_SIZE):
        index = mat_input.index(0)
        mat_input[index -  MATRIX_SIZE], mat_input[index] = mat_input[index], mat_input[index -  MATRIX_SIZE]
        return mat_input
    return None

#Move the blank tile downwards
def blank_tile_down(mat_input, MATRIX_SIZE, N_Board):
    if check_move_down(mat_input, MATRIX_SIZE, N_Board):
            index = mat_input.index(0)
            mat_input[index + MATRIX_SIZE], mat_input[index] = mat_input[index], mat_input[index + MATRIX_SIZE]
            return mat_input
    return None

#Move the blank tile towards left
def blank_tile_left(mat_input, MATRIX_SIZE):
    if check_move_left(mat_input, MATRIX_SIZE):
            index = mat_input.index(0)
            mat_input[index - 1], mat_input[index] = mat_input[index], mat_input[index - 1]
            return mat_input
    return None

#Move the blank tile towards right
def blank_tile_right(mat_input, MATRIX_SIZE):
    if check_move_right(mat_input, MATRIX_SIZE):
            index = mat_input.index(0)
            mat_input[index + 1], mat_input[index] = mat_input[index], mat_input[index + 1]
            return mat_input
    return None

