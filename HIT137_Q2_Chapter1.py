from PIL import Image
import time

mainImage_directory = "chapter1.jpg"
mainImage = Image.open(mainImage_directory)

current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10
    
new_image = Image.new('RGB', mainImage.size)
for y in range(mainImage.height):
    for x in range(mainImage.width):
        r, g, b = mainImage.getpixel((x, y))
        generated_r = min(255, r + generated_number)
        generated_g = min(255, g + generated_number)
        generated_b = min(255, b + generated_number)
        new_image.putpixel((x, y), (generated_r, generated_g, generated_b))

outputImage_directory = "chapter1out.png"
new_image.save(outputImage_directory)

sumofRedPixel = sum([new_image.getpixel((x, y))[0]

  for y in range(new_image.height)
  for x in range(new_image.width)])

print("Total Number of Red Pixel:", sumofRedPixel)
