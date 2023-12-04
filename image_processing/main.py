import cv2
import os

#convert all images to greyscale

input_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'grey_images')

#Create directory if none
#os.makedirs(output_dir, exist_ok=True)

#Get image list
img_list = os.listdir(input_dir)

for img in img_list:
    img_path = os.path.join(input_dir, img)

    grey_color = cv2.imread(img_path, 0)
    img_name = img.split('.')
    new_img = img_name[0] + '-new.' + img_name[1]
    new_img_path = os.path.join(output_dir, new_img)
    cv2.imwrite(new_img_path, grey_color)
    
    print(f'Processed {img} and saved as {new_img} in {output_dir}')






# color = cv2.imread('galaxy.jpeg', 1)
# print(type(color))
# print(color.ndim)

# #convert to grayscale
# grey_color = cv2.imread('galaxy.jpeg', 0)
# cv2.imwrite('galaxy-grey.jpeg', grey_color)
# print('greyscale photo is created')