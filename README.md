# Image Resizer

Tools for scale and resize image


### How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

### How to use
```bash

$ python image_resize.py -h
usage: image_resize.py [-h] [-o OUTPUT_FILE] [-s SCALE] [--width WIDTH]
                       [--height HEIGHT]
                       input_file

positional arguments:
  input_file            Path to original image

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Path to resized image
  -s SCALE, --scale SCALE
                        Image scale factor
  --width WIDTH         Output image width
  --height HEIGHT       Output image height

```

### Sample output
```bash
$ python python image_resize.py e:/test.png -s 0.5
Process finished with exit code 0
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
