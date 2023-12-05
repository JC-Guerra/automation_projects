import os
import cv2

def img_scale(scale_percentage, width, height):
    new_width = width * scale_percentage / 100
    new_height = height * scale_percentage / 100
    return(int(new_width), int(new_height))

def convert_img(input_dir, img_list):
    output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resized_images')

    for img in img_list:
        img_path = os.path.join(input_dir, img)

        #resize image
        image = cv2.imread(img_path)
        new_dim = img_scale(10, image.shape[1], image.shape[0])

        #set new path
        img_name = img.split('.')
        new_img = img_name[0] + '-resized.' + img_name[1]
        new_img_path = os.path.join(output_dir, new_img)
        
        #write
        resized_img = cv2.resize(image, new_dim)
        cv2.imwrite(new_img_path, resized_img)
        
        print(f'Processed {img} and saved as {new_img} in {output_dir}')