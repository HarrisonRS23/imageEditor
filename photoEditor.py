from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'  # input image path for folder with images to be edited
pathOut = './editedImages'  # output image path for edited images
# factor = 1.0  # enhancer factor

# , , and higher values more
print("What do you want the enhancer factor to be? ")
print("Factor 1.0 always returns a copy of the original image"
      "lower factors mean less color (brightness, contrast, etc) "
      "and higher values more)")
print("Factor: ")
factor = float(input())
print("There will be a series of questions for how to edit your photos.")
print("Please press 0 for no and 1 for yes")


# Asking for black and white edit
blackAndWhite = int(input("Do you want the photo to be Black And White: "))

# Asking for contrast enhancement
contrast = int(input("Do you want to adjust the contrast? "))

# Asking for color vibrance enhancement
color = int(input("Do you want to adjust the color vibrance? "))

# Asking for brightness adjustment
brightness = int(input("Do you want to adjust the brightness? "))

# Asking for sharpness adjustment
sharpness = int(input("Do you want to adjust the sharpness? "))

# Access all images in file and edit all
print("Loading images: ")
for fileName in os.listdir(path):
    print("Processing image: " + fileName)
    editImage = Image.open(f'{path}/{fileName}')  # open image from path
    editImage = editImage.rotate(-90) # rotate up and down

    if blackAndWhite == 1:
        contrast_enhancer = ImageEnhance.Contrast(editImage)
        editImage = contrast_enhancer.enhance(factor)  # Black and white conversion
        print("Converting to black and white")

    if contrast == 1:
        contrast_enhancer = ImageEnhance.Contrast(editImage)
        editImage = contrast_enhancer.enhance(factor)
        print("Adjusting contrast")

    if color == 1:
        color_enhancer = ImageEnhance.Color(editImage)
        editImage = color_enhancer.enhance(factor)
        print("Adjusting color")

    if brightness == 1:
        brightness_enhancer = ImageEnhance.Brightness(editImage)
        editImage = brightness_enhancer.enhance(factor)
        print("Adjusting brightness")

    if sharpness == 1:
        sharpness_enhancer = ImageEnhance.Sharpness(editImage)
        editImage = sharpness_enhancer.enhance(factor)
        print("Adjusting sharpness")

    # Saving edited image
    print("Saving image: " + fileName)
    cleanName = os.path.splitext(fileName)[0]
    editImage.save(f'{pathOut}/{cleanName}_edited.jpg')
