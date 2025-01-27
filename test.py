import cv2 as cv

# function to display the coordinates of 
# of the points clicked on the image  
def click_event(event, x, y, flags, params): 
  
    # checking for left mouse clicks 
    if event == cv.EVENT_LBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        print(x, ' ', y) 
  
        # displaying the coordinates 
        # on the image window 
        font = cv.FONT_HERSHEY_SIMPLEX 
        cv.putText(img, str(x) + ',' +
                    str(y), (x,y), font, 
                    1, (255, 0, 0), 2) 
        cv.imshow('image', img) 
  
    # checking for right mouse clicks      
    if event==cv.EVENT_RBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        print(x, ' ', y) 
  
        # displaying the coordinates 
        # on the image window 
        font = cv.FONT_HERSHEY_SIMPLEX 
        b = img[y, x, 0] 
        g = img[y, x, 1] 
        r = img[y, x, 2] 
        cv.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r), 
                    (x,y), font, 1, 
                    (255, 255, 0), 2) 
        cv.imshow('image', img) 
  
# driver function 
if __name__=="__main__": 
  
    # reading the image 
    img = cv.imread('openCV_click_test_image.png', 1) 
  
    # displaying the image 
    cv.imshow('image', img) 
  
    # setting mouse handler for the image 
    # and calling the click_event() function 
    cv.setMouseCallback('image', click_event) 
  
    # wait for a key to be pressed to exit 
    cv.waitKey(0) 
  
    # close the window 
    cv.destroyAllWindows() 