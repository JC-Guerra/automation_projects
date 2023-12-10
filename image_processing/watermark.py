import cv2
import os
import resize_img

def apply_watermark(input_dir):

    #set output parameters
    output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'watermarked_image')

    #load images
    image_path = os.path.join(input_dir, 'wine.png')
    watermark_path = os.path.join(input_dir, 'logo.png')
    image = cv2.imread(image_path)
    watermark = cv2.imread(watermark_path)

    #resize watermark
    resize_img.convert_img(input_dir, ['logo.png'])

    #find resized image
    resize_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resized_images')
    resized_watermark = cv2.imread(os.path.join(resize_dir, 'logo-resized.png'))

    print(f'Size of original watermark: {watermark.shape}')
    print(f'Size of resized watermark: {resized_watermark.shape}')
    print(f'Size of image: {image.shape}')

    #set watermark position
    x = image.shape[0] - resized_watermark.shape[0]
    y = image.shape[1] - resized_watermark.shape[1]

    watermark_position = image[x:, y:]
    cv2.imwrite(os.path.join(output_dir, 'watermark_position.png'), watermark_position)
    print(f'watermark_position.png has been created')

    #blend watermark and photo
    blend = cv2.addWeighted(watermark_position, 0.5, resized_watermark, 0.5, 0)
    cv2.imwrite(os.path.join(output_dir, 'blend.png'), blend)
    print(f'blend.png has been created')

    image[x:, y:] = blend
    cv2.imwrite(os.path.join(output_dir, 'wine_watermarked.png'), image)
    print(f'wine.png has been watermarked in {output_dir}')
