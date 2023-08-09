from tkinter import Tk, filedialog
from PIL import Image
import os

ASCII_CHARS_DETAIL = "@%#*+=-:. "
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def pixels_to_ascii(image, scale=1):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value * (len(ASCII_CHARS) - 1) // 255]
    return ascii_str

def main():
    root = Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if not file_path:
        print("No file selected.")
        return
    
    try:
        image = Image.open(file_path)
    except Exception as e:
        print("Error:", e)
        return
    
    script_directory = os.path.dirname(os.path.abspath(__file__))
    image_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(script_directory, f"{image_name}_ascii.txt")
    
    width = 200

    image = resize_image(image, width)
    image = grayscale_image(image)
    ascii_str = pixels_to_ascii(image)
    
    img_height = image.size[1]
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:i+width] for i in range(0, ascii_str_len, width)])
    
    with open(output_path, "w") as f:
        f.write(ascii_img)
    
    print("ASCII art saved to", output_path)
    input()

if __name__ == "__main__":
    main()
