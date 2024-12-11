from tkinter import *
from tkinter import filedialog, colorchooser, font
from PIL import Image, ImageTk, ImageDraw, ImageFont
from matplotlib import font_manager


add_file_path = ""
files = []
preview_file_path = ""

def add_file():
    global add_file_path, files
    add_file_path = filedialog.askopenfilename(initialdir="image_watermark\\assets", title="Select a file!")
    if add_file_path not in files:
        files.append(add_file_path)
    for img in files:
        listbox.insert(files.index(img), img)
        files.remove(img)
      
def clear_listbox():
    listbox.delete(0,END)
    for item in files:
        files.remove(item)
    canvas.itemconfig(background_img, anchor=NW, image="")
    canvas.itemconfig(preview_text, text="Preview..")

def select_item(event1):
    global preview_file_path
    preview_file_path = listbox.get(listbox.curselection())
    canvas.itemconfig(preview_text, text="")
    preview_imgs()
    
def preview_imgs():
    global cached
    image = Image.open(preview_file_path)
    resized_img = image.resize((700, 800), Image.Resampling.LANCZOS)
    selected_image = ImageTk.PhotoImage(resized_img)
    canvas.itemconfig(preview_text, text="")
    canvas.itemconfig(background_img, anchor=NW, image=selected_image)
    # anti python garbage collection
    cached = selected_image
    cached.image = selected_image
    
def set_fonts():
    for f in font_manager.get_font_names():
        font_listbox.insert('end', f)

def get_color():
    global print_font_fill
    
    font_fill_color = colorchooser.askcolor()
    canvas.itemconfig(upper_left, fill=font_fill_color[1])
    canvas.itemconfig(top_center, fill=font_fill_color[1])
    canvas.itemconfig(upper_right, fill=font_fill_color[1])
    canvas.itemconfig(mid_left, fill=font_fill_color[1])
    canvas.itemconfig(mid_center, fill=font_fill_color[1])
    canvas.itemconfig(mid_right, fill=font_fill_color[1])
    canvas.itemconfig(bottom_left, fill=font_fill_color[1])
    canvas.itemconfig(bottom_center, fill=font_fill_color[1])
    canvas.itemconfig(bottom_right, fill=font_fill_color[1])
    print_font_fill = font_fill_color[0]
    
def select_font(event):
    global print_watermark_font
    print_watermark_font = font_listbox.get(font_listbox.curselection())
    watermark_font.config(family=font_listbox.get(font_listbox.curselection()))
    
def font_size(value):
   global print_watermark_size
   print_watermark_size = 10 + int(value) 
   watermark_font.config(size=10+int(value))  

def save():
    font_fill = print_font_fill
    font_selected = font_listbox.get(font_listbox.curselection())
    save_path = filedialog.asksaveasfile(
        confirmoverwrite=True,
        defaultextension="png",  
        filetypes=[("jpeg", ".jpg"),("png", ".png"),("bitmap", "bmp"),("gif", ".gif")])
    
    with Image.open(preview_file_path).convert("RGB") as base:
        resized_img = base.resize((700, 800), Image.Resampling.LANCZOS)
        file = font_manager.findfont(font_selected)

        fnt = ImageFont.truetype(file, int(print_watermark_size))
        draw = ImageDraw.Draw(resized_img)
        
        if var1.get():
            draw.text((10, 30), text=watermark_text.get(), font=fnt, fill=font_fill)
        if var2.get():
            draw.text((350, 30), text=watermark_text.get(), font=fnt, fill=font_fill)
        if var3.get():
            draw.text((600, 30), text=watermark_text.get(), font=fnt, fill=font_fill)
        if var4.get():
            draw.text((10, 400), text=watermark_text.get(), font=fnt, fill=font_fill)
        if var5.get():
            draw.text((350, 400), text=watermark_text.get(), font=fnt, fill=font_fill)
        if var6.get():
            draw.text((600, 400), text=watermark_text.get(), font=fnt, fill=font_fill)
        if var7.get():
            draw.text((10, 750), text=watermark_text.get(), font=fnt, fill=font_fill)
        if var8.get():
            draw.text((350, 750), text=watermark_text.get(), font=fnt, fill=font_fill)
        if var9.get():
            draw.text((600, 750), text=watermark_text.get(), font=fnt, fill=font_fill)
        resized_img.save(save_path)

def place_watermark():
    canvas.itemconfig(preview_text, text="")
    if var1.get():
        canvas.itemconfig(upper_left, text=watermark_text.get())
    if var2.get():
        canvas.itemconfig(top_center, text=watermark_text.get())
    if var3.get():
        canvas.itemconfig(upper_right, text=watermark_text.get())
    if var4.get():
        canvas.itemconfig(mid_left, text=watermark_text.get())
    if var5.get():
        canvas.itemconfig(mid_center, text=watermark_text.get())
    if var6.get():
        canvas.itemconfig(mid_right, text=watermark_text.get())
    if var7.get():
        canvas.itemconfig(bottom_left, text=watermark_text.get())
    if var8.get():
        canvas.itemconfig(bottom_center, text=watermark_text.get())
    if var9.get():
        canvas.itemconfig(bottom_right, text=watermark_text.get())
    clear_watermarks()
    
def clear_watermarks():
    if not var1.get():
        canvas.itemconfig(upper_left, text="")
    if not var2.get():
        canvas.itemconfig(top_center, text="")
    if not var3.get():
        canvas.itemconfig(upper_right, text="")
    if not var4.get():
        canvas.itemconfig(mid_left, text="")
    if not var5.get():
        canvas.itemconfig(mid_center, text="")
    if not var6.get():
        canvas.itemconfig(mid_right, text="")
    if not var7.get():
        canvas.itemconfig(bottom_left, text="")
    if not var8.get():
        canvas.itemconfig(bottom_center, text="")
    if not var9.get():
        canvas.itemconfig(bottom_right, text="") 

def reset_watermark():
    canvas.itemconfig(upper_left, text="", fill="#000000")
    canvas.itemconfig(top_center, text="", fill="#000000")
    canvas.itemconfig(upper_right, text="", fill="#000000")
    canvas.itemconfig(mid_left, text="", fill="#000000")
    canvas.itemconfig(mid_center, text="", fill="#000000")
    canvas.itemconfig(mid_right, text="", fill="#000000")
    canvas.itemconfig(bottom_left, text="", fill="#000000")
    canvas.itemconfig(bottom_center, text="", fill="#000000")
    canvas.itemconfig(bottom_right, text="", fill="#000000")
    var1.set(0) 
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    font_size_button.set(0)
    watermark_font.config(family="Arial", size=10)
    watermark_text.delete(0, END)

    

root = Tk()
root.title("Image Watermark App")
root.config(padx=50, pady=50)
 
frame = Frame(root)  
frame.grid(row=0, column=0)

app_font = font.Font(family="Arial", size=10)
watermark_font = font.Font(family="Arial", size=10)

# canvas:
canvas = Canvas(frame, width=700, height=800, bd=1)
canvas.grid(row=0, column=1, rowspan=15, padx=10, sticky=E)
canvas.config(relief="sunken")

# default canvas image
background_img = canvas.create_image(0, 0, image="")

# default text:
preview_text = canvas.create_text(350, 400, text="Preview..", fill="black", font=app_font)

# default watermarks text:
upper_left = canvas.create_text(10, 30, text="", font=watermark_font, anchor=W)
top_center = canvas.create_text(350, 30, text="", font=watermark_font, anchor=CENTER)
upper_right = canvas.create_text(600, 30, text="", font=watermark_font, anchor=W)
mid_left = canvas.create_text(10, 400, text="", font=watermark_font, anchor=W)
mid_center = canvas.create_text(350, 400, text="", font=watermark_font, anchor=CENTER)
mid_right = canvas.create_text(600, 400, text="", font=watermark_font, anchor=W)
bottom_left = canvas.create_text(10, 750, text="", font=watermark_font, anchor=W)
bottom_center = canvas.create_text(350, 750, text="", font=watermark_font, anchor=CENTER)
bottom_right = canvas.create_text(600, 750, text="", font=watermark_font, anchor=W)

# general labels
title_label = Label(frame, text="Why don't you personalize your images?", font=("Arial", 10, "italic"))
title_label.grid(row=0, column=0, sticky=W, padx=5)

subtitle_label = Label(frame, text="Add a watermark..", font=("Arial", 10, "underline"))
subtitle_label.grid(row=1, column=0, sticky=W, padx=5)


'''ADD FILE FRAME:'''
file_frame = LabelFrame(frame, text="Add File", font=("Arial", 10, "bold"))  
file_frame.grid(row=2, column=0, sticky=W, padx=1)

# labels:
browse_label = Label(file_frame, text="Select a file:", font=app_font)
browse_label.grid(row=0, column=0, sticky=W, padx=10)

select_label = Label(file_frame, text='Uploded files:', font=app_font)
select_label.grid(row=1, column=0, sticky=W, padx=10)

supported_files_label = Label(file_frame, text="*.jpg, .jpeg, .png", font=("Arial", 8, "normal"))
supported_files_label.grid(row=0, column=2, sticky=SW)

# entries:
# listbox:
listbox = Listbox(file_frame, height=5, width=70, exportselection=False)
listbox.grid(row=1, column=1, columnspan=3, padx=13, pady=10, sticky="news")
listbox.bind("<<ListboxSelect>>", select_item)


# buttons:
select_file = Button(file_frame, text="Browse File", font=("Arial", 9, "normal"), command=add_file)
select_file.grid(row=0, column=1, padx=10, pady=5, sticky=EW)

clear_listbox_button = Button(file_frame, text="Clear Files", font=("Arial", 9, "normal"), command=clear_listbox)
clear_listbox_button.grid(row=0, column=3, padx=10, pady=5, sticky=EW)


'''ADD WATERMARK:'''
watermark_frame = LabelFrame(frame, text="Add Watermark", font=("Arial", 10, "bold"))
watermark_frame.grid(row=3, column=0, pady=10, sticky=W)

# labels:
write_mark = Label(watermark_frame, text="Compose watermark:", font=app_font)
write_mark.grid(row=1, column=0, padx=10, sticky=W)

options_label = Label(watermark_frame, text="Placing options:", font=app_font)
options_label.grid(row=2, column=0, rowspan=3, sticky=W, padx=10)

choose_font_label = Label(watermark_frame, text="Choose font:", font=app_font)
choose_font_label.grid(row=5, column=0, padx=10, sticky=W)

choose_size_label = Label(watermark_frame, text="Choose watermark size:", font=app_font)
choose_size_label.grid(row=7, column=0, sticky=W, padx=10)

choose_color_label = Label(watermark_frame, text="Choose color:", font=app_font)
choose_color_label.grid(row=8, column=0, sticky=W, padx=10)

# entries:
watermark_text = Entry(watermark_frame, width=60)
watermark_text.grid(row=1, column=1, columnspan=3, sticky=W, padx=10)

# listbox:
font_listbox = Listbox(watermark_frame, selectmode=SINGLE, height=5, width=50, highlightthickness=0, exportselection=False)
font_listbox.grid(row=5, column=1, columnspan=3, padx=10, pady=10, sticky="news")
font_listbox.bind("<ButtonRelease-1>", select_font)

#buttons:
font_size_button = Scale(watermark_frame, from_=0, to=50, orient=HORIZONTAL, sliderlength=30, command=font_size)
font_size_button.grid(row=7, column=1, columnspan=3, sticky=EW, padx=8)

choose_color_button = Button(watermark_frame, text='Color', command=get_color)
choose_color_button.grid(row=8, column=1, padx=10, pady=10, sticky=W)

reset_button = Button (watermark_frame, text='Reset Watermark', command=reset_watermark)
reset_button.grid(row=10, column=1, columnspan=3, padx=10, pady=10, sticky=EW)

'''PLACING OPTIONS FRAME:'''
placing_options_frame = LabelFrame(watermark_frame, text="Options", font=("Arial", 10, "bold"))
placing_options_frame.grid(row=2, column=1, columnspan=3, pady=10, padx=10, sticky=EW)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()

upper_left_button = Checkbutton(placing_options_frame, text="Top Left", onvalue=1, offvalue=0, variable=var1, command=place_watermark)
upper_left_button.grid(row=2, column=1, sticky=W)

top_center_button = Checkbutton(placing_options_frame, text="Top Center", onvalue=1, offvalue=0, variable=var2, command=place_watermark)
top_center_button.grid(row=2, column=2, sticky=W)

upper_right_button = Checkbutton(placing_options_frame, text="Top Right", onvalue=1, offvalue=0, variable=var3, command=place_watermark)
upper_right_button.grid(row=2, column=3, sticky=W,)

mid_left_button = Checkbutton(placing_options_frame, text="Center Left", onvalue=1, offvalue=0, variable=var4, command=place_watermark)
mid_left_button.grid(row=3, column=1, sticky=W)

mid_center_button = Checkbutton(placing_options_frame, text="Center Middle", onvalue=1, offvalue=0, variable=var5, command=place_watermark)
mid_center_button.grid(row=3, column=2, sticky=W)

mid_right_button = Checkbutton(placing_options_frame, text="Center Right", onvalue=1, offvalue=0, variable=var6, command=place_watermark)
mid_right_button.grid(row=3, column=3, sticky=W)

bottom_left_button = Checkbutton(placing_options_frame, text="Bottom Left", onvalue=1, offvalue=0, variable=var7, command=place_watermark)
bottom_left_button.grid(row=4, column=1, sticky=W)

bottom_center_button = Checkbutton(placing_options_frame, text="Bottom Center", onvalue=1, offvalue=0, variable=var8, command=place_watermark)
bottom_center_button.grid(row=4, column=2, sticky=W)

bottom_right_button = Checkbutton(placing_options_frame, text="Bottom Right", onvalue=1, offvalue=0, variable=var9, command=place_watermark)
bottom_right_button.grid(row=4, column=3, sticky=EW)

''' SAVE '''
save_frame = LabelFrame(frame, text="Save Your Work", font=("Arial", 10, "bold"))
save_frame.grid(row=4, column=0, pady=10, sticky=W)

# labels:
the_end_label = Label(save_frame, text="...here you go!", font=("Arial", 10, "italic", "bold"))
the_end_label.grid(row=1, column=0)

#buttons:
save_watermark_button = Button(save_frame, text='Save!', font=app_font, command=save)
save_watermark_button.grid(row=1, column=1,sticky="news", columnspan=3, pady=10, padx=10)


set_fonts()
root.mainloop()