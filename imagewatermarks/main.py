import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFont


# # ---------------------------- GET IMAGE ------------------------------- ##
# get an image
def add_watermark():
    file_path = askopenfilename(title="Select Image", filetypes=[('Image Files', '*.jpg')])
    file_name = file_path.split("/")[-1]
    # Open an Image
    img = Image.open(file_path)
    img_height = int(img.height/2)
    img_width = int(img.width/10)

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    
    font = ImageFont.truetype("arial.ttf", 40)

    # Add Text to an image
    I1.text((img_width, img_height), "your custom watermark here", fill=(147, 179, 199, 0), font=font)

    # Display edited image
    img.show()

    if not os.path.isdir("C:/Users/jack/Desktop/watermarked"):
        os.makedirs("C:/Users/jack/Desktop/watermarked")
        # Save the edited image
        img.save(f"C:/Users/jack/Desktop/watermarked/{file_name}")
    else:
        # Save the edited image
        img.save(f"C:/Users/jack/Desktop/watermarked/{file_name}")


# # ---------------------------- DESTROY WINDOW ------------------------------- ##
def quit():
    window.destroy()


# # ---------------------------- UI SETUP ------------------------------- ##
# GUI should allow you to select photo / path to add images,
window = Tk()
window.title("Photo Watermark App")

canvas = Canvas(window, width=600, height=500)
canvas.grid(columnspan=5, rowspan=4)

instruction_label = Label(window, text="Select photo to watermark.", font="Ariel")
instruction_label.grid(columnspan=5, column=0, row=1)

# Browse button
browse_btn = Button(window, command=add_watermark, text="Browse", font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
browse_btn.grid(column=2, row=2)

# Quit button
quit_btn = Button(window, command=quit, text="Quit", font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
quit_btn.grid(column=3, row=2)

window.mainloop()  # Keep the window open