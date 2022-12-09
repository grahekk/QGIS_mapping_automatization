import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

path_files = r"\\server.intranet.dvokut-ecro.hr\Ecro\2_StrucneUsluge\1_PUOP\2_PUO\SUO_GOEM_Oikon_plinovodix3\Osijek-Vukovar\2_radno\PP dok\PP_Materijali\proba"
files = [f for f in os.listdir(path_files) if f.endswith('jpg')]
template_map = cv2.imread(r"\\server\Ecro\2_StrucneUsluge\1_PUOP\2_PUO\SUO_GOEM_Oikon_plinovodix3\Osijek-Vukovar\2_radno\PP dok\PP_Materijali\2_2_1_CIJEVNI_TRANSPORT_PLINA_ID2.jpg",0)
template_sast = cv2.imread(r"\\server\Ecro\2_StrucneUsluge\1_PUOP\2_PUO\SUO_GOEM_Oikon_plinovodix3\Osijek-Vukovar\2_radno\PP dok\PP_Materijali\PPUG_Vukovar_3.1.3_Vodno gospodarstvo_001.jpg",0)

for f in files:

    img = cv2.imread(path_files + "\\" + f)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    hh, ww = img.shape[:2]

    # threshold on white
    # Define lower and uppper limits
    lower = np.array([254, 254, 254])
    upper = np.array([255, 255, 255])

    # Create mask to only select black
    thresh = cv2.inRange(img, lower, upper)

    # apply morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # invert morp image
    mask = 255 - morph

    # apply mask to image
    result = cv2.bitwise_and(img, img, mask=mask)

    # #option with model training
    # pre_model = cv2.CascadeClassifier('pre_trained_model.xml')
    # found = pre_model.detectMultiScale(gray, minSize =(20, 20))
    # # Don't do anything if there's 
    # # no sign
    # amount_found = len(found)
    # if amount_found != 0:
    #     # There may be more than one
    #     # sign in the image
    #     for (x, y, width, height) in found:
    #         # We draw a green rectangle around
    #         # every recognized sign
    #         cv2.rectangle(img, (x, y), 
    #                     (x + height, y + width), 
    #                     (0, 255, 0), 5)
    
    #drawing rectangles and contours
    # #reparation of rectangle
    # kernel = np.ones((5,5),np.uint8)
    # erosion = cv2.erode(gray,kernel,iterations = 10)
    # dilate = cv2.dilate(erosion,kernel,iterations = 10)

    # #threshold
    # ret,thresh = cv2.threshold(gray,50,255,0)
    # contours,hierarchy = cv2.findContours(thresh, 1, 2)
    # print("Number of contours detected:", len(contours))
    # contours = sorted(contours, key=cv2.contourArea, reverse= True)
    # contours = contours[0:100]

    # rectangles = []
    # for cnt in contours:
    #     x1,y1 = cnt[0][0]
    #     approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    #     if len(approx) == 4:
    #         x, y, w, h = cv2.boundingRect(cnt)
    #         rectangles.append(cnt)
    # #         ratio = float(w)/h
    # #         if ratio >= 0.9 and ratio <= 1.1:
    # #             img = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
    # #             cv2.putText(img, 'Square', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
    # #         else:
    # #             cv2.putText(img, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    # #             img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
    # print("Number of rectangles detected: ", len(rectangles))
    # sorted_rectangles= sorted(rectangles, key=cv2.contourArea, reverse= True)
    # largest_item = sorted_rectangles[0:30]
    # cv2.drawContours(img, largest_item, -1, (255,0,0),10)
    # #cv2.imwrite(path_files + "\\" + f + '_treshold.jpg', thresh)
    cv2.imwrite(path_files + "\\" + f + '_res.jpg', result)
    print(f +" exported!")

print("all files exported!")