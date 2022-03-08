import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageColor

white = ImageColor.getcolor('#ffce9e', "RGB")
black = ImageColor.getcolor('#d18b47', "RGB")

replacements = {0: white, 1: black}

def checkerboard(size):
    return np.indices(size).sum(axis=0) % 2

def chess_board_background(checkerboard, res):
    chess_board = np.zeros((*checkerboard.shape, 3), dtype=np.uint8)

    for val, color in replacements.items():
        chess_board[checkerboard == val] = color

    return Image.fromarray(chess_board).resize(res * np.array(checkerboard.shape)[::-1], resample=Image.NEAREST)

# image source https://en.wikipedia.org/wiki/File:Chess_qlt45.svg
queen = Image.open('./queen.png').convert('RGBA')

def place_queens(background, queens):
    """Modifies the background and places queen images to ones in the matrix
    
    background -- the output image from chess_board_background
    queens -- a matrix representing the positions of queens with ones
    """
    resized = np.array(background.size) / np.array(queens.shape)[::-1]
    scaled_queen = queen.resize(np.uint8(resized))
    for x, y in zip(*np.where(queens == 1)):
        background.paste(scaled_queen, (int(resized[0] * y), int(resized[1] * x)), scaled_queen)

def plot_grid(padx, pady, images, titles, numx, scale):
    fig, ax = plt.subplots(1, 1, figsize=(1, 1))
    ax.set_axis_off()

    for i, image in enumerate(images):
        x, y = padx * (i % numx), pady * (i // numx)
        w, h = np.array(fig.get_size_inches()) / scale
        imw, imh = image.size

        ax = fig.add_axes([x / fig.dpi / w, 1 - (y + imw) / fig.dpi / h, imw / fig.dpi / w, imh / fig.dpi / h])

        title = titles[i] if i < len(titles) else ""
        ax.set_title(title)
        ax.set_axis_off()
        ax.imshow(image)

# M is the matrix to visualize, dpi stands for dots per inch in the plot,
# pixels defines the side length of each square (like resolution)
def vis(boards, titles = [], numx = 2, res = 120, scale = 1):
    """Visualize chessboards with optional titles in a numx wide grid
    
    boards -- chess board state(s)
    titles -- array of titles to show over the chessboards
    numx -- number of boards per row
    res -- resolution of one tile in the chessboard
    scale -- visualization scale (does not affect text size)
    """
    if not isinstance(boards, list): boards = [boards]

    background = chess_board_background(checkerboard(boards[0].shape), res)

    images = [background.copy() for _ in boards]
    for i, image in enumerate(images):
        place_queens(image, boards[i])

    padx = 5
    pady = 25 if len(titles) else 5
    plot_grid(background.size[0] + padx / scale, background.size[1] + pady / scale, images, titles, numx, scale)

    plt.show(block=True)