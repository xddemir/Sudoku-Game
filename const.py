import pygame as pg

board: list = [
    ["X7", "X8", "0", "X4", "0", "0", "X1", "X2", "0"],
    ["X6", "0", "0", "0", "X7", "X5", "0", "0", "X9"],
    ["0", "0", "0", "6", "0", "X1", "0", "X7", "X8"],
    ["0", "0", "X7", "0", "X4", "0", "X2", "X6", "0"],
    ["0", "0", "X1", "0","X5", "0", "X9", "X3", "0"],
    ["9", "0", "X4", "0", "X6", "0", "0", "0", "X5"],
    ["0", "X7", "0", "X3", "0", "0", "0", "X1", "X2"],
    ["X1", "X2", "0", "0", "0", "X7", "X4", "0", "0"],
    ["0", "X4", "X9", "X2", "0","X6", "0", "0", "X7"]]

    
WIDTH, HEIGHT = 720, 720
SQ_SIZE = 720 // 12

GRID_COLOR = (200, 200, 200)
PICK_COLOR = (91, 209, 215)
VALID_COLOR = (230, 239, 240)
INVALID_COLOR = (214, 116, 137)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

KEYS: dict = {pg.K_1 : "1", pg.K_2 : "2", pg.K_3 : "3", 
              pg.K_4 : "4", pg.K_5 : "5", pg.K_6 : "6", 
              pg.K_7 : "7", pg.K_8 : "8", pg.K_9 : "9"}
