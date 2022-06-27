from ast import While
import cv2
import numpy as np
import os
import pandas as pd

FOLDER = 'C:\\Users\\Alexis\\Desktop\\Data Science\\Webscraping\\imgs'

# Function that goes through all images and lets the user label them.
# Controls: a = label as 0
#           d = label as 1
#           w = discard image
#           q = saves the data in a CSV file and quits 
def image_classifier(folder_location):
    list = os.listdir(folder_location)
    data_dict = {'img_name': [], 'Label': []}

    def append_to_dict(name, label):
        data_dict['img_name'].append(name)
        data_dict['Label'].append(label)

    for img_dir in list:
        print(img_dir)
        actual_image = cv2.imread(folder_location + '\\' + img_dir)


        while True:
            cv2.imshow('Make A Choice', actual_image)

            k = cv2.waitKey(1)
            if k == ord('a'):
                print('[SELECTION] 0')
                append_to_dict(img_dir, 0)
                cv2.destroyAllWindows()
                break

            if k == ord('d'):
                print('[SELECTION] 1')
                append_to_dict(img_dir, 1)
                cv2.destroyAllWindows()
                break

            if k == ord('w'):
                print('[IMAGE DISCARDED]')
                cv2.destroyAllWindows()
                os.remove(folder_location + '\\' + img_dir)
                break
   
            if k == ord('q'):
                print('[SAVE AND QUIT]')
                df = pd.DataFrame(data_dict)
                df.to_csv(folder_location + '\\' + 'Labels')
                cv2.destroyAllWindows()
                break


image_classifier(FOLDER)
