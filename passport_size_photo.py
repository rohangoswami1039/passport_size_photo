#importing modules 
from PIL import Image
import os 


#functions and classes 
def image_details(image):
    print("Image details")
    print()
    print(image.format)
    print(image.mode)
    print(image.size)
    print(image.palette)

class image_size:
    def image_size1(image):
        # for image of the size 5.08 x 5.08
        img_size=(600,600)
        new_image = image.resize(img_size)
        new_image.save('edit/1.jpg')
        print("image resized")
        print()
    def image_size2(image):
        # for image of the size 3.81 x 3.81
        img_size=(450,450)
        new_image = image.resize(img_size)
        new_image.save('edit/2.jpg')
        print("image resized")
        print()
    def image_size3(image):
        # for image of the size 3.5 x 4.5 
        img_size=(413,531)
        new_image = image.resize(img_size)
        new_image.save('edit/3.jpg')
        print("image resized")
        print()
    def image_size4(image):
        # for image of the size 3.5 x 3.5
        img_size=(413,413)
        new_image = image.resize(img_size)
        new_image.save('edit/4.jpg')
        print("image resized")
        print()
    def image_size5(image):
        # for image of the size 3 x 4
        img_size=(354,472)
        new_image = image.resize(img_size)
        new_image.save('edit/5.jpg')
        print("image resized")
        print()
    def image_size6(image):
        # for image of the size 5 x 7
        img_size=(591,827)
        new_image = image.resize(img_size)
        new_image.save('edit/6.jpg')
        print("image resized")
        print()
    def image_size7(image):
        # for image of the size 3.3 x 4.8
        img_size=(390,567)
        new_image = image.resize(img_size)
        new_image.save('edit/7.jpg')
        print("image resized")
        print()



#main loop
for f in os.listdir("."):
    if f.endswith('.jpg'):
        image=Image.open(f)
        print('image is: ',f)
        print()
while True :
        print("Image Editing ")
        print("1. image details ")
        print("2. image resize ")
        ch=int(input("Enter your choice: "))
        if ch==1:
            image_details(image)
            print("")
            
        elif ch==2:
            print("")
            print("1. 5.08 x 5.08 cm")
            print("2. 3.81x3.81 cm")
            print("3. 3.5x4.5 cm  India ")
            print("4. 3.5x3.5 cm ")
            print("5. 3x4 cm ")
            print("6. 5x7 cm")
            print("7. 3.3x4.8 cm")
            print("")
            ch1=int(input("Enter the choice: "))
            if ch1==1 :
                image_size.image_size1(image)
            elif ch1==2:
                image_size.image_size2(image)
            elif ch1==3:
                image_size.image_size3(image)
            elif ch1==4:
                image_size.image_size4(image)
            elif ch1==5:
                image_size.image_size5(image)
            elif ch1==6:
                image_size.image_size6(image)
            elif ch1==7:
                image_size.image_size7(image)
