from PIL import Image, ImageFont, ImageDraw
import os
import codecs
import itertools 

list_font = [
    ("THSarabunNew","THSarabunNew.ttf" , "New" , "Normal"),
    ("THSarabunNew","THSarabunNew Italic.ttf" , "New" , "Italic"),
    ("THSarabunNew","THSarabunNew Bold.ttf" , "New" , "Bold"),
    ("THSarabunNew","THSarabunNew BoldItalic.ttf" , "New" , "BoldItalic")
]

dataset_txt = 'test.txt'
list_sentences = []
list_lines = []

file = open(dataset_txt, encoding="utf-8")
count = 0
while True: 
    count += 1
 
    # Get next line from file
    line = file.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    # list_sentences = [((line.strip()),(count))]
    list_sentences.append(line.strip())
    list_lines.append(count)

# for tt in list_sentences:
#     print(tt)

# with open(dataset_txt, encoding="utf-8") as f:
#     lines = f.readlines()
#     count = 1
#     while lines:
#         print(count)
#         lines = f.readlines()
#         count += 1
        

#     list_lines.append(count)
#     for text_sen in lines:
#         list_sentences.append(text_sen.strip())

for t in list_font:
    font_path = "./font/{}/".format(t[0])
    font_name = t[1]
    out_path = "./dataset/{}/{}/".format(t[0],t[3])

    font_size = 72 # px
    font_color = "#000000" # HEX Black
    bg_color = '#ffffff'
    width = 1500 
    height = 120

    # Create Font using PIL
    font = ImageFont.truetype(font_path+font_name, font_size)
    
    for (cs,line) in zip(list_sentences,list_lines):
        # Create PNG Image with that size
        img = Image.new("RGBA", (width, height), color=bg_color)
        draw = ImageDraw.Draw(img)
        position = (50,20)
            
        # Draw the character
        draw.text(position, str(cs), font=font, fill=font_color)
        # Save the character as png
        try:
            img.save(out_path + "format_" + "_" + t[0] + "_" + t[3] + "_" + str(line) +  ".png")
            file_name = out_path + "format_" + "_" + t[0] + "_" + t[3] + "_"+ str(line) + ".gt.txt"
            file = codecs.open(file_name, "w", "utf-8") 
            file.write("{}".format(cs)) 
            file.close() 
        except:
            print(f"[-] Couldn't Save:\t{cs}")