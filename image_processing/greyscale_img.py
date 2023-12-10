import os
import cv2


def convert_img(input_dir, img_list):
    output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'grey_images')

    for img in img_list:
        img_path = os.path.join(input_dir, img)

        #convert to greyscale
        grey_color = cv2.imread(img_path, 0)

        #set new path
        img_name = img.split('.')
        new_img = img_name[0] + '-grey.' + img_name[1]
        new_img_path = os.path.join(output_dir, new_img)

        #write
        cv2.imwrite(new_img_path, grey_color)
        
        print(f'Processed {img} and saved as {new_img} in {output_dir}')