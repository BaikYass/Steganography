import sys
sys.path.append('png')
import png
import argparse



def read_png_file(filepath):
    '''
    :param filepath: l'image PNG
    :return: width, height, rows, rgbA
    width: Width of PNG image in pixels
    height: Height of PNG image in pixes
    rows: A sequence or iterator for the row data
    RGBA 
    '''
    data = png.Reader(filename=filepath).asRGBA8()
    width = data[0]
    height = data[1]
    rows = list(data[2])
    list1 = []
    list1 = rows
    rgbA = []
    for i in list1:
        for j in range(0, len(i)):
            rgbA.append(i[j])
    return rows, width, height, rgbA





def Insert_to_lowest_weight(rgbA):
    '''
    :param rgbA:
    :return: rgbA
    rgbA : represents rounding down to an even number less than or equal
    '''

    Modulo=0
    for i in range(len(rgbA)):
        Modulo = rgbA[i] % 2
        if Modulo != 0:
            rgbA[i] = rgbA[i] - 1
    return rgbA




def convertTOBunery(text):
    '''
    :param text:
    :return: !binnary
    using join() + ord() + format()
    Converting String to binary
    binnary : return the binary value
    '''
    binnary = ''.join(format(ord(i), 'b').rjust(8,"0") for i in text)
    return binnary




def encode(rgbA,binnary):
    '''
    :param rgbA:
    :param binnary:
    :return:
    '''

    rgba_New =[]
    rgba_New = rgbA

    for i in range(0,len(binnary)):
        rgba_New[i] = rgba_New[i] + int(binnary[i])
    return rgba_New




def RGBAdapter(RGBrows, width):
    '''
    Adapt RGB ROWS format
    :param RGBrows:
    :return: Pixelslist
    '''
    PixelsList = []
    Liste =[]
    for i in range(0, len(RGBrows)):
        PixelsList.append(RGBrows[i])
        if(len(PixelsList) == width*4 and i != 0):
            Liste.append(tuple(PixelsList))
            PixelsList.clear()
    return Liste


def WiriteToPNGFile(width, height, rowsFinal, pngFile):
    '''
    :param width:
    :param height:
    :param rowsFinal:
    :return: The new image png with text binary
    '''
    w = png.Writer(width, height, greyscale=False, alpha=True)
    file = open(pngFile, 'wb')
    w.write(file, rowsFinal)
    file.close()



def decode(path):
    '''
     Decode text hidden in the image, to find the end of the text you have to find block of 8 values of even
    :param path: the new png image
    :return: The Plain text
    '''
    i = 0
    NewList = []
    rows, width, height, rgbA = read_png_file(path)

    while i < len(rgbA):
        NewList.append(rgbA[i:i + 8])
        i += 8
    values = []
    for e in NewList:
        if (any(n % 2 == 1 for n in e)):
            values.append(e)
        else:
            break
    Binnary = ''
    Text = ''
    for x in values:
        Binnary = Binnary + ''.join(map(str, [item % 2 for item in x]))

    Text = ''.join(chr(int(Binnary[i * 8:i * 8 + 8], 2)) for i in range(len(Binnary) // 8))
    return Text



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-w", '--write', action='store_true')
    parser.add_argument("-f", '--file')
    parser.add_argument("-t", '--text')
    parser.add_argument('output')
    args = parser.parse_args()

    if args.write:

        if args.file and args.text:
            image_file = args.file
            text = args.text
        elif args.file:
            image_file = args.file
            text = "Hello !!"
        else:
            image_file = input("Please enter your Image path !: ")
            text = input("Please enter your Text !: ")

        rows, width, height, rgbA = read_png_file(image_file)

        BinaryText = convertTOBunery(text)
        lowest_weight_RGBA= []
        lowest_weight_RGBA = Insert_to_lowest_weight(rgbA)
        New_RGBA = encode(lowest_weight_RGBA, BinaryText)

        rowsFinal = RGBAdapter(New_RGBA, width)
        WiriteToPNGFile(width, height, rowsFinal, args.output)

    if not args.write:
        print(decode(args.output))