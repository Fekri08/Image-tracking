#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Import Libraries

import sys
sys.path.append(r'C:\Users\FMA\AppData\Local\Programs\Python\Lib\site-packages')
from random import randint
import cv2

# Tracker Types
tracker_type = ['BOOSTING',
                'MIL',
                'KCF',
                'TLD',
                'MEDIANFLOW',
                'GOTURN',
                'MOSEE',
                'CSRT']

# Define trackers by name
def tracker_name(tracker_type):
    

    # Create trackers by name with if statement
    if tracker_type == tracker_type[0]:   
        tracker = cv2.TrackerBoosting_create()
    elif tracker_type == tracker_type[1]:
        tracker = cv2.TrackerMIL_create() 
    elif tracker_type == tracker_type[2]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_type == tracker_type[3]:
        tracker = cv2.TrackerKCF_create()
    elif tracker_type == tracker_type[4]:
        tracker = cv2.TrackerTLD_create()
    elif tracker_type == tracker_type[5]:
        tracker = cv2.TrackerMedianFlow_create()
    elif tracker_type == tracker_type[6]:
        tracker = cv2.TrackerGOTURN_create()
    elif tracker_type == tracker_type[7]:
        tracker = cv2.TrackerCSRT_create()
    
    
        

    # else statement
    else :
        tracker = None
        print('no tracker found')
        print('choose from these trackers')
        for tr in tracker_type:
            print(tr)
    
    # return
    return tracker

if __name__ == '__main__':
    print("Default tracking algorithm MOSSE \n"
        "Available algorithms are: \n")
    for tr in tracker_type:
        print(tr)
        
    trackerType = 'MOSSE'
    


    # Create a video capture
    cap = cv2.VideoCapture('Video/Vehicles.mp4')
    
    # Read first frame
    success, frame = cap.read()
    
    # Quit if failure
    if not success:
        print('cannot read video')
    
    # Select boxes and colors
    rects = []
    colors = []

    # While loop
    
    while True:
        
        # draw rectangles, select ROI, open new window
        rect_box = cv2.selectROI('MultiTracker', frame)
        rects.append(rect_box)
        colors.append((randint(60,255),randint(60,255))) 
        print("press q to stop selecting boxes and start multitracking")
        print("press any key to select another box")
        
        #close window
        if cv2.waitKey(0) & 0xFF == 113:
            break
        
    # print message
    print(f'selected boxes {rects}')
    
    
    # Create multitracker
    multitracker = cv2.MultiTracker_create()
    
    # Initialize multitracker
    for rec_box in rects:
        multitracker.add(tracker_name(tracker_type),
                        frame,
                        rect_box)
    
    #Video and Tracker
    # while loop
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        # update location objects
        success, boxes = multitracker.udate(frzme)
        
        # draw the objectes tracked
        for i , newbox in enumerate(boxes):
            pts1 = (int(newbox[0]),
                   int(newbox[1]))
            pts2 = (int(newbox[0]+ newbox[2]),
               int((newbox1)+ newbox[3]))
            cv2.rectangle(frame, 
                         pts1,
                         pts2,
                         colors[i],
                         2,
                         1)
        
        # display frame
        cv2.imshow('Multitracker', frame)
        
    
        # Close the frame
        if cv2.waitKey(20) & 0xFF == 27:
            break
    
# Release and Destroy
cap.release()
cv2.destroyAllWindows()


# In[ ]:




