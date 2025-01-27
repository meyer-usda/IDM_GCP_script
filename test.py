import cv2 as cv, glob, os

# function to save (and display) the coordinates of the last point clicked on the image  
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks 
    if event == cv.EVENT_LBUTTONDOWN: 
        # Save the clicked pixel as the location of the GCP
        GCPs[-1][0] = x
        GCPs[-1][1] = img.shape[0] - y # shift y origin to bottom left

        # Display a circle around the clicked point
        img2 = img.copy()
        cv.circle(img2, (x,y), 8, (0,0,255), 2)
        cv.imshow('image', img2)

def get_images(folder_path):
    image_extensions = ['jpg', 'jpeg', 'png']#, 'gif', 'bmp']
    images = []
    for extension in image_extensions:
        images.extend(glob.glob(f"{folder_path}/**/*.{extension}", recursive=True))
    return images


# driver function 
if __name__=="__main__": 
    images_dir = r'C:\Users\MeyerTaffel\local\coding\GCP_scripting'
    images = get_images(images_dir)

    # GCP format: [im_x, im_y, image_name]
    GCPs = []

    for image_path in images:
        GCPs.append([0, 0, os.path.basename(image_path), "ADD_GCP_NAME_HERE"])

        # reading the image 
        # img = cv.imread('openCV_click_test_image.png', 1)
        img = cv.imread(image_path, 1)

        # displaying the image 
        cv.imshow('image', img) 
    
        # setting mouse handler for the image 
        # and calling the click_event() function 
        cv.setMouseCallback('image', click_event)

        # # wait for a key to be pressed to exit
        # cv.waitKey(0)

        while True:
            if cv.waitKey(1) & 0xFF == 13: # ENTER key ASCII
                # GCPs[-1][1] = img.shape[0] - GCPs[-1][1]
                # GCPs[-1].append(os.path.basename(images[0]))
                break
        
        # close the window 
        cv.destroyAllWindows() 

    print(GCPs)
    filename = "gcp_list.txt"
    with open(os.path.join(images_dir, filename), 'w') as file:
        for gcp in GCPs:
            file.write(" ".join(str(el) for el in gcp) + "\n")
    print(f"File '{filename}' created successfully.")
