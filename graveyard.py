def input_gcp_name_by_index(gcp_index_map, instruction_str=None):
    if instruction_str:
        print(instruction_str)
    else:
        print("\n")

    text = ""
    letters = string.ascii_lowercase + string.digits
    while True:
        key = cv.waitKey(0)
        for letter in letters:
            if key == ord(letter):
                text = text + letter
                print(text, end='\r')
        if key == ord("\b"):
            text = text[:-1]
            print(''*30, end='\r')
            print(text, end='\r')
        if key == ord("\n") or key == ord("\r"): # Enter Key
            break
    return text