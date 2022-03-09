import os
from ast import For
from multiprocessing.dummy import Array
from PIL import Image

skintoneAttributes = ["shirt", "mouth", "accessory", "eyebrows", "eyes" ]
skintoneNames = ["skin-tone-1"]

attributes = ["background", "skin-tone-1", "eyewear", "hair-hat"]
attributesCount = len(attributes)

image = Image.new('RGB', (1200, 1200))
image.save('combo.png', "PNG")

def process_folder(directory, prevImage):
    print('Getting items in ' + directory)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.png'):
                # For now, we'll just go 1 level deep
                print(os.getcwd())
                newImage = Image.open('./' + directory + '/' + file)
                prevImage.paste(newImage, (0,0), newImage)
                prevImage.save('combo.png', "PNG")
                break

for folder in attributes:
    directory = 'images/' + folder
    if folder in skintoneNames:
        for skintoneFolder in skintoneAttributes:
            process_folder(directory + '/' + skintoneFolder, image)
    else:
        process_folder(directory, image)
    
    

