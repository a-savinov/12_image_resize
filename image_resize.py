import argparse
import os

from PIL import Image


def calculate_new_image_size(image_width, image_height, scale, width, height):
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


def resize_image(path_to_original, path_to_output, **kwargs):
    input_image = Image.open(path_to_original)
    input_image_width, input_image_height = input_image.size
    new_image_width, new_image_height = calculate_new_image_size(
        input_image_width, input_image_height, kwargs.get('scale'),
        kwargs.get('width'), kwargs.get('height'))
    rounding_accuracy = 2
    ratio_factor = True if round(input_image_width / input_image_height,
                                 rounding_accuracy) == \
                           round(new_image_width / new_image_height,
                                 rounding_accuracy) else False
    output_image = input_image.resize((new_image_width, new_image_height))
    if path_to_output:
        output_image.save(path_to_output)
    else:
        input_file_path = os.path.dirname(path_to_original)
        output_file_name = os.path.basename(path_to_original).split('.')
        output_image.save('{}{}__{}x{}.{}'.format(input_file_path,
                                                  output_file_name[0],
                                                  new_image_width,
                                                  new_image_height,
                                                  output_file_name[1]))
    return ratio_factor


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
    if not resize_image(args.input_file, args.output_file, scale=args.scale,
                        width=args.width, height=args.height):
        print('Aspect ratio was broken')
