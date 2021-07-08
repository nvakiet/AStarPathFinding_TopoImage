from PIL import Image, ImageDraw, ImageChops
import numpy as np

def getGrayscale(rgbPixel: tuple):
    return int(0.2989 * rgbPixel[0] + 0.5870 * rgbPixel[1] + 0.1140 * rgbPixel[2])

def main():
    inPath = "input/map.bmp"
    outPath = "output/test.bmp"
    im = Image.open(inPath).convert("L")
    im2 = Image.open(inPath).convert("RGB")
    imDraw = ImageDraw.Draw(im2, "RGB")
    for y in range(im.size[0]):
        for x in range(im.size[1]):
            if im.getpixel((x,y)) < 50:
                imDraw.point((x, y), (255,0,0))
    im2.save(outPath)

if __name__ == "__main__":
    main()