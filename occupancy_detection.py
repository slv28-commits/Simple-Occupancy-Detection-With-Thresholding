import cv2 as cv
import numpy as np

img = cv.imread(r'your_own_image.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

display = cv.resize(gray, (512, 512), interpolation=cv.INTER_CUBIC)
cv.imshow("Chessboard", display)

# assigning chessboard squares
chessboard_squares = [
    ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"],
    ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
    ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
    ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
    ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
    ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
    ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
    ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"],
]

i = 0
j = 0

def find_occupancy(chessboard_squares, display, i, j):
    start_x = j * 64
    end_x = (j + 1) * 64
    start_y = i * 64
    end_y = (i + 1) * 64
    square = display[start_x:end_x, start_y:end_y]
    if (i % 2 != 0 and j % 2 != 0) or (i % 2 == 0 and j % 2 == 0):
        ret, thresh_square = cv.threshold(square, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        num_black_square = np.sum(thresh_square == 0)

        if num_black_square >= (64 * 64) * 0.45:
            print(f'Square {chessboard_squares[j][i]} is occupied')
    else:
        ret, thresh_square = cv.threshold(square, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        num_black_square = np.sum(thresh_square == 0)
        num_white_square = np.sum(thresh_square == 255)

        if (num_black_square < ((64 * 64) * 0.85) and num_black_square >= ((64 * 64) * 0.10)) or (num_white_square < ((65 * 65) * 0.85) and num_white_square >= ((64 * 64) * 0.10)):
            print(f'Square {chessboard_squares[j][i]} is occupied.')

# main occupancy loop
while i < 8:
    j = 0
    while j < 8:
        find_occupancy(chessboard_squares, display, i, j)
        j += 1
    i += 1

cv.waitKey(0)
