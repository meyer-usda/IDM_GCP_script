import cv2 as cv, glob, os, string

# function to save (and display) the coordinates of the last point clicked on the image  
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks 
    if event == cv.EVENT_LBUTTONDOWN: 
        # Save the clicked pixel as the location of the GCP
        GCPs[-1][0] = x
        GCPs[-1][1] = img.shape[0] - y # shift y origin to bottom left

        # Display a circle around the clicked point
        img2 = img.copy()
        cv.circle(img2, (x,y), 14, (0,0,255), 2)
        cv.imshow('image', img2)

def get_images(folder_path):
    image_extensions = ['jpg', 'jpeg', 'png']#, 'gif', 'bmp']
    images = []
    for extension in image_extensions:
        images.extend(glob.glob(f"{folder_path}/*.{extension}", recursive=True))
    return images

def get_gcp_array(path):
    lines = []
    with open(path, 'r') as file:
        for line in file:
            formatted_line = []
            for el in line.split(','):
                try:
                    formatted_line.append(float(el.strip()))
                except:
                    formatted_line.append(el.strip())

            if type(formatted_line[1]) == float:
                lines.append(formatted_line)

    return lines

def get_gcp_index_map(gcp_arr):
    gcp_i_map = []
    for i, gcp in enumerate(gcp_arr):
        gcp_i_map.append(f"{str(i+1)}: {gcp[0]}")
    return gcp_i_map

def input_gcp_name_by_index(instruction_str=None):
    if instruction_str:
        print(instruction_str)
    else:
        print("\n")

    text = ""
    letters = string.digits
    while True:
        key = cv.waitKey(0)
        for letter in letters:
            if key == ord(letter):
                text = text + letter
                print(text, end='\r')
        if key == ord("\b"):
            text = text[:-1]
            print('')
            print(text, end='\r')
        if key == ord("\n") or key == ord("\r"): # Enter Key
            break
    return text

# driver function 
if __name__=="__main__": 
    # images_dir = r'C:\Users\MeyerTaffel\local\coding\GCP_scripting\Pix4Dmapper_Pix4Dmatic_ex1_data\100MSDCF'
    images_dir = r'C:\Users\MeyerTaffel\local\coding\GCP_scripting'
    gcp_reference_filepath = r'C:\Users\MeyerTaffel\local\coding\GCP_scripting\gcp_ref.txt'

    images = get_images(images_dir)
    gcp_ref = get_gcp_array(gcp_reference_filepath)
    gcp_index_map = get_gcp_index_map(gcp_ref)

    # GCP format: [im_x, im_y, image_name]
    GCPs = []

    print("GCP Reference Index:")
    print('\n'.join(gcp_index_map))

    for image_path in images:
        GCPs.append([0, 0, os.path.basename(image_path), "ADD_GCP_NAME_HERE"])

        # reading the image 
        # img = cv.imread('openCV_click_test_image.png', 1)
        cv.namedWindow('image', cv.WINDOW_NORMAL)
        cv.resizeWindow('image', 812, 609) 
        img = cv.imread(image_path, 1)

        # displaying the image 
        cv.imshow('image', img) 
    
        # setting mouse handler for the image 
        # and calling the click_event() function 
        cv.setMouseCallback('image', click_event)

        # # wait for a key to be pressed to exit
        # cv.waitKey(0)

        print("Click on GCP and press Enter. Backspace to skip image (click image first)")
        while True:
            if cv.waitKey(0) & 0xFF == 13: # Enter key ASCII
                if GCPs[-1][0:2] == [0,0]:
                    print("Click on GCP and press Enter. Backspace to skip image (click image first)")
                    continue

                gcp_i = input_gcp_name_by_index("Type GCP index from list then press Enter:")
                try:
                    # Add gcp name and corresponding lon lat z coords
                    gcp = gcp_ref[int(gcp_i)-1]
                    GCPs[-1][3] = gcp[0]
                    GCPs[-1] = gcp[1:] + GCPs[-1]
                    print(f"GCP name set: {GCPs[-1][-1]}")
                except:
                    print("Incorrect input. Check gcp_list.txt for needed corrections")
                    break
                break
            if cv.waitKey(0) & 0xFF == 8: # Backspace key ASCII
                GCPs.pop() # remove that image from the final list of GCPs
                break
        
        # close the window 
        cv.destroyAllWindows() 

    print(GCPs)
    filename = "gcp_list.txt"
    with open(os.path.join(images_dir, filename), 'w') as file:
        for gcp in GCPs:
            file.write(" ".join(str(el) for el in gcp) + "\n")
    print(f"File '{filename}' created successfully.")
