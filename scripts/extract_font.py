import sys
import time
from PIL import Image


def main(path, output):
    original = Image.open(path)
    # original.show()
    for i in range(original.width // 8):
        for j in range(original.height // 8):
            rect = (14+8*i, 14+8*j, 14+8*(i+1), 14+8*(j+1))
            tile = original.crop(rect)
            # time.sleep(0.5)
            tile.save("{}/{}_{}.png".format(output, i, j))


if __name__ == '__main__':
    main(*sys.argv[1:])
