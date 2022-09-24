import base64

def write_image_as_string_to_file(source_path : str, destination_path: str):
  
    with open(source_path, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    # print(converted_string)
    
    with open(destination_path, "wb") as file:
        file.write(converted_string)

def string_to_image(source_path : str, destination_path: str):
    file = open(source_path, 'rb')
    byte = file.read()
    file.close()
    
    decodeit = open(destination_path, 'wb')
    decodeit.write(base64.b64decode((byte)))
    decodeit.close()

# write_image_as_string_to_file("C:/Users/lanozie/Pictures/Informationsfabrik_Logo_4c_ohne Slogan.jpg",
# "C:/Users/lanozie/Pictures/Informationsfabrik_Logo_4c_ohne Slogan.bin")


# string_to_image("C:/Users/lanozie/Documents/Code/give_box_ms_hack/fastapi-backend/data/images/5",
# "C:/Users/lanozie/Documents/Code/give_box_ms_hack/fastapi-backend/data/images/5_recovered.jpg")