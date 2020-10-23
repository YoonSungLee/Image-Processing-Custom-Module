import numpy as np
import cv2
from PIL import Image
import math
import collections
import os


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def on_mouse(event, x, y, flags, params):
    global pt1_x,pt1_y, flag, img_name
    if event == cv2.EVENT_LBUTTONDOWN:
        #print('Start Mouse Position: '+str(x)+', '+str(y))
        pt1_x,pt1_y=x,y
    elif event == cv2.EVENT_LBUTTONUP:
        #print('End Mouse Position: '+str(x)+', '+str(y))
        p1=Point2D(pt1_x,pt1_y)
        p2=Point2D(x,y)
        a = p1.x - p2.x    # 선 a의 길이
        b = p1.y - p2.y    # 선 b의 길이
        c = round(math.sqrt((a * a) + (b * b)), 2)
        print(c)
        data = img_name + ' ' + str(c) + '\n'
        f.write(data)
        cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=2)

path = '/Users/yoonsunglee/Documents/minimal_test'
img_list = os.listdir(path)
img_list = [img for img in img_list if '.ipynb_checkpoints' not in img] # for jupyter user
img_list = [img for img in img_list if '.DS_Store' not in img]          # for mac user
f = open("results/result.txt", 'w')
for img in img_list:
    flag = False
    img_name = img
    print('img name:', img_name)
    img = cv2.imread(os.path.join(path, img))
    pt1_x , pt1_y = None, None

    while(True):
        cv2.namedWindow('real image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('real image', 1000, 1000)
        cv2.setMouseCallback('real image', on_mouse, 0)
        cv2.imshow('real image', img)
        if cv2.waitKey(0) == 110:
            cv2.imwrite('results/line_'+img_name, img)
            break
        if cv2.waitKey(0) == 27:
            cv2.destroyAllWindows()
            break
f.close()