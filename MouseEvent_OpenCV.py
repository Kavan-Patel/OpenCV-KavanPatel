#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


# events= [i for i in dir(cv) if 'EVENT' in i]
# print(events)


# In[3]:


def click_event(event, x, y, flags, param):
#     if event==cv.EVENT_LBUTTONDOWN:
#         font=cv.FONT_HERSHEY_COMPLEX
#         strXY= str(x)+', '+str(y)
#         cv.putText(img, strXY, (x,y), font, 0.5, (255,0,255), 1)
#         cv.imshow('image',img)
    if event==cv.EVENT_LBUTTONDOWN:
        blue=img[y, x, 0]
        green=img[y,x,1]
        red= img[y,x,2]
        font=cv.FONT_HERSHEY_COMPLEX
        print(red)
        print(blue)
        print(green)
        bgr= f'{blue},{green},{red}'
        cv.putText(img, bgr, (x,y), font, 0.5, (0,255,255), 1)
        cv.imshow('image',img)


# In[ ]:


img= np.zeros([512,512], np.uint8)
cv.imshow('image',img)
cv.setMouseCallback('image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:




