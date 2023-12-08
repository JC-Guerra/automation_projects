import cv2
import os
import greyscale_img
import resize_img
import detect
import watermark

#Create directory if none
#os.makedirs(output_dir, exist_ok=True)

def ask_user():
    #ask user for action
    #is there a better way to code multiple lines?
    selected_action = int(input('What do you want to do:\n1. Greysale\n2. Resize\n3. Detect faces\n4. Watermark image\nAnswer: '))
    return selected_action

def process_image(selected_action, input_dir, img_list):
    #call function to process image
    if selected_action == 1:
        greyscale_img.convert_img(input_dir, img_list)
    elif selected_action == 2:
        resize_img.convert_img(input_dir, img_list)
    elif selected_action == 3:
        detect.detect_faces(input_dir)
    elif selected_action == 4:
        watermark.apply_watermark(input_dir)
    else:
        print('Please choose a valid action')
        ask_user()
        process_image(selected_action, input_dir, img_list)

def main():

    #get image list
    input_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
    img_list = os.listdir(input_dir)

    selected_action = ask_user()
    process_image(selected_action, input_dir, img_list)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()