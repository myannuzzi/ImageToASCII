# ImageToASCII
# Converts image to ascii text

# Import Python Image Library
from PIL import Image

def image2ASCII(image, fType, saveas, scale):
    # Load image in
    im = Image.open(image)
    scale = int(scale)

    # Get image info
    print(im.format, im.size, im.mode)
    w,h = im.size

    # resize image
    im.resize((w//scale, h//scale)).save("resized.%s" % fType)
    w, h = im.size

    # Create text file for image conversion
    convFile = open(saveas, "w")

    # Matrix for characters
    grid = []
    # Read through image pixel by pixel
    for i in range(h):
        grid.append(["X"] * w)

    pixel = im.load()
    print(im.size)

    for y in range(h):
        for x in range(w):
            if sum(pixel[x,y]) == 0:
                grid[y][x] = "#"
            elif sum(pixel[x,y]) in range(1,100):
                grid[y][x] = "X"
            elif sum(pixel[x,y]) in range(100,200):
                grid[y][x] = "%"
            elif sum(pixel[x,y]) in range(200,300):
                grid[y][x] = "&"
            elif sum(pixel[x,y]) in range(300,400):
                grid[y][x] = "*"
            elif sum(pixel[x,y]) in range(400,500):
                grid[y][x] = "+"
            elif sum(pixel[x,y]) in range(500,600):
                grid[y][x] = "/"
            elif sum(pixel[x,y]) in range(600,700):
                grid[y][x] = "("
            elif sum(pixel[x,y]) in range(700,800):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "

    # print(grid)
    for row in grid:
        convFile.write("".join(row)+"\n")
    # Close file
    convFile.close()

if __name__ == '__main__':
    image2ASCII("haro.jpg", "jpg", "haroConv.txt", "5")