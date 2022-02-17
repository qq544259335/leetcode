# Load libraries and convenience functions
import time
from IPython import display
import matplotlib.pyplot as plt
import numpy as np


def load_image(filename):
    img = np.load(filename)
    img = img.astype("float32") / 255.
    return img


def gray2rgb(image):
    print(image, np.shape(image))
    print(np.expand_dims(image, 2), np.shape(np.expand_dims(image, 2)))
    print(np.repeat(np.expand_dims(image, 2), 3, axis=2), np.shape(np.repeat(np.expand_dims(image, 2), 3, axis=2)))
    return np.repeat(np.expand_dims(image, 2), 3, axis=2)


def show_image(img):
    plt.imshow(img, interpolation='nearest')


start = time.time()
images = [load_image('red.npy'),
          load_image('green.npy'),
          load_image('blue.npy')]
np.set_printoptions(threshold=50)

show_image(gray2rgb(np.concatenate(images, axis=1)))
# Store the height and width of the images
height, width = images[0].shape
print(height, width)

# Pad each image with black by 30 pixels. You do not need to use this, but
# padding may make your implementation easier.
pad_size = 30
images_pad = [np.pad(x, pad_size, mode='constant') for x in images]
show_image(images[2])
np.set_printoptions(threshold=100)

# Store the height and width of the images
height, width = images[0].shape
print(height, width)

# Pad each image with black by 30 pixels. You do not need to use this, but
# padding may make your implementation easier.
pad_size = 30
images_pad = [np.pad(x, pad_size, mode='constant') for x in images]
show_image(images[2])


# Given two matrices, write a function that returns a number of how well they are aligned.
# The lower the number, the better they are aligned. There are a variety of scoring functions
# you can use. The simplest one is the Euclidean distance between the two matrices.
def score_function(im1, im2):
    # ======================
    # You code here
    return np.sum(np.square(im1 - im2)) ** 0.5
    # ======================


# Given two matrices chan1 and chan2, return a tuple of how to shift chan2 into chan1. This
# function should search over many different shifts, and find the best shift that minimizes
# the scoring function defined above.
def align_channels(chan1, chan2):
    best_offset = (0, 0)
    best_score = np.inf

    # ======================
    # You code here
    # Hint: you can first define a callable function to shift the images,
    # which will make your code clean in for-loops.
    shift_set = []
    for i in range(-30, 31):
        for j in range(-30, 31):
            shift_set.append((i, j))
    for dy, dx in shift_set:
        score = score_function(chan1, shift_image(chan2, dy, dx))
        # print(dy, dx, score)
        if score < best_score:
            best_score = score
            best_offset = (dx, dy)
        elif score == best_score:
            if dy ** 2 + dx ** 2 < best_offset[0] ** 2 + best_offset[1] ** 2:
                best_offset = (dx, dy)
    # ======================
    return best_offset


def shift_image(img, dy, dx):
    # print(dy, dx)
    # res = img[:][:]
    # if dy != 0:
    #     for i in range(len(res)):
    #         if dy > 0 and i + dy >= len(res):
    #             break
    #         elif dy < 0 and i + dy < 0:
    #             continue
    #         res[i + dy] = res[i]
    # if dx != 0:
    #     for j in range(len(res[0])):
    #         if dx > 0 and j + dx >= len(res[0]):
    #             break
    #         elif dx < 0 and j + dx < 0:
    #             continue
    #         for i in range(len(res)):
    #             res[i][j + dx] = res[i][j]
    # return res
    new_image = img[:][:]
    if dy != 0:
        if dy < 0:
            new_image = np.vstack([new_image[-dy:], new_image[:-dy]])
        else:
            height = len(new_image)
            new_image = np.vstack(
                [new_image[height - dy:], new_image[:height - dy]])
    if dx != 0:
        if dx < 0:
            new_image = np.hstack([new_image[:, -dx:], new_image[:, :-dx]])
        else:
            length = len(new_image[0])
            new_image = np.hstack(
                [new_image[:, length - dx:], new_image[:, :length - dx]])
    new_image = np.pad(new_image[30:-30, 30:-30], pad_size, mode='constant')

    return new_image


rg_dx, rg_dy = align_channels(images_pad[0], images_pad[1])
print("----------shift1 done----------------")
rb_dx, rb_dy = align_channels(images_pad[0], images_pad[2])
print("shift done")


# Use the best alignments to now combine the three images. You should use any of the variables
# above to return a tensor that is (Height)x(Width)x3, which is a color image that you can visualize.
def combine_images():
    # ======================
    # You code here
    im1 = images_pad[0]
    im2 = shift_image(images_pad[1], rg_dy, rg_dx)
    im3 = shift_image(images_pad[2], rb_dy, rb_dx)
    # ======================
    images = [im1, im2, im3]
    return np.stack(images, axis=-1)


print(rg_dx, rg_dy, rb_dx, rb_dy)
final_image = combine_images()
if final_image is not None:
    show_image(final_image)
end = time.time()
print(end - start)
