"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = ((pixel.red-red)**2 + (pixel.green-green)**2 + (pixel.blue-blue)**2)**0.5
    return dist

    pass


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red_total = 0
    green_total = 0
    blue_total = 0
    count = 0
    for points in pixels:
        red_total += points.red
        blue_total += points.blue
        green_total += points.green
        count += 1
    ans = [red_total//count, green_total//count, blue_total//count]
    return ans

    pass


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    closest = [1000, 1000, 1000]
    ans = pixels[0]
    avg = get_average(pixels)
    for pixel in pixels:
        if abs(pixel.red - avg[0]) < closest[0]:
            closest[0] = abs(pixel.red - avg[0])
            ans.red = pixel.red
        if abs(pixel.green - avg[1]) < closest[1]:
            closest[1] = abs(pixel.green - avg[1])
            ans.green = pixel.green
        if abs(pixel.blue - avg[2]) < closest[2]:
            closest[2] = abs(pixel.blue - avg[2])
            # print('a:', closest[2])
            ans.blue = pixel.blue
    # print('ans', ans)
    return ans


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    """
    green_im = SimpleImage.blank(20, 20, 'green')
    green_pixel = green_im.get_pixel(0, 0)
    red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    print(best1.red, best1.green, best1.blue)
    pass
    """
    for i in range(width):
        for j in range(height):
            pixel_input = []
            for image in images:
                pixel_input.append(image.get_pixel(i, j))
            # print(get_best_pixel(pixel_input).red, get_best_pixel(pixel_input).green)
            ans = get_best_pixel(pixel_input)
            pixel = result.get_pixel(i, j)
            pixel.red = ans.red
            pixel.green = ans.green
            pixel.blue = ans.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
