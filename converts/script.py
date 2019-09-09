from PIL import Image
import os


def convert(infile):
    f, e = os.path.splitext(infile)
    outfile = f + '.jpeg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('Cannot convert', infile)
