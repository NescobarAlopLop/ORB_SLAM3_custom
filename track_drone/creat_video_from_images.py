import cv2
import glob
import time
import sys


if __name__ == '__main__':
    i = 0
    start = time.time()
    decoder = cv2.VideoWriter_fourcc(*'XVID')
    image_file_path = sys.argv[1]
    output_video_name = sys.argv[2]
    firs_im_filename = image_file_path + '001.png'
    img = cv2.imread(firs_im_filename)
    height, width, layers = img.shape
    size = (width, height)
    out = cv2.VideoWriter(output_video_name, decoder, 5, size)
    for f in glob.glob(image_file_path + '*.png'):
        if i == 38 or i == 67:
            continue
        if i < 10:
            filename = image_file_path + '00' + str(i) + '.png'
        else:
            filename = image_file_path + '0' + str(i) + '.png'
        print(filename)
        img = cv2.imread(filename)
        out.write(img)
        i += 1
    out.release()
    end = time.time()
    print(end - start)
