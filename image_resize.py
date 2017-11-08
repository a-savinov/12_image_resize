import argparse
import os

from PIL import Image


def calculate_new_image_size(image, scale=None, width=None,
                             height=None):
    image_width, image_height = image.size
    if scale:
        new_image_width = int(image_width * scale)
        new_image_height = int(image_height * scale)
    elif width and height:
        new_image_width = width
        new_image_height = height
    elif not scale and not width and not height:
        new_image_width = image_width
        new_image_height = image_height
    elif width:
        ratio = width / image_width
        new_image_width = width
        new_image_height = int(image_height * ratio)
    else:
        ratio = height / image_height
        new_image_width = int(image_width * ratio)
        new_image_height = height
    return new_image_width, new_image_height


def get_ratio_factor(orig_image, new_image, accuracy=2):
    orig_image_width, orig_image_height = orig_image.size
    new_image_width, new_image_height = new_image.size
    ratio_factor = bool(
        round(orig_image_width / orig_image_height, accuracy) ==
        round(new_image_width / new_image_height, accuracy))
    return ratio_factor


def resize_image(orig_image, new_width, new_height):
    output_image = orig_image.resize((new_width, new_height))
    return output_image


def get_input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Path to original image')
    parser.add_argument('-o', '--output_file', required=False,
                        help='Path to resized image')
    parser.add_argument('-s', '--scale', required=False,
                        help='Image scale factor', type=float)
    parser.add_argument('--width', required=False,
                        help='Output image width', type=int)
    parser.add_argument('--height', required=False,
                        help='Output image height', type=int)
    return parser.parse_args()


if __name__ == '__main__':
    args = get_input_argument_parser()
    orig_image = Image.open(args.input_file)
    new_image_width, new_image_height = calculate_new_image_size(
        orig_image, args.scale, args.width, args.height)
    new_image = resize_image(orig_image, new_image_width, new_image_height)
    if args.output_file:
        new_image.save(args.output_file)
    else:
        name, extension = os.path.splitext(args.input_file)
        new_image.save('{}__{}x{}{}'.format(name, new_image_width,
                                             new_image_height, extension))
    if not get_ratio_factor(orig_image, new_image):
        print('Aspect ratio was broken')
