from PIL import Image, ImageFont, ImageDraw
import codecs
import os
from numpy.lib.function_base import append
import pandas as pd
from pandas._config.config import set_option
import re


listfont = [#("THSarabunIT9","THSarabunIT๙.ttf" , "IT9" , "Normal")
#  ("THSarabunIT9","THSarabunIT๙ Italic.ttf" , "IT9" , "Italic")
# ("THSarabunIT9","THSarabunIT๙ Bold.ttf" , "IT9" , "Bold"),
# ("THSarabunIT9","THSarabunIT๙ BoldItalic.ttf" , "IT9" , "BoldItalic"),
# ("THSarabunPSK","THSarabun.ttf" , "PSK" , "Normal"),
# ("THSarabunPSK","THSarabun Italic.ttf" , "PSK" , "Italic"),
# ("THSarabunPSK","THSarabun Bold.ttf" , "PSK" , "Bold"),
# ("THSarabunPSK","THSarabun BoldItalic.ttf" , "PSK" , "BoldItalic"),
 ("THSarabunNew","THSarabunNew.ttf" , "New" , "Normal")
# ("THSarabunNew","THSarabunNew Italic.ttf" , "New" , "Italic"),
# ("THSarabunNew","THSarabunNew Bold.ttf" , "New" , "Bold"),
# ("THSarabunNew","THSarabunNew BoldItalic.ttf" , "New" , "BoldItalic")
]

df = pd.read_csv('data.csv')

# list_of_rows = [list(row) for row in df.values]

# out_path = "Dataset2/"
   

# for dataset in list_of_rows:
#     # initializing bad_chars_list
#     bad_chars = [';', "*" , "" , "#" , "&quote"] 
    
#     # initializing test string
#     test_string = dataset[4]
    
#     # printing original string
#     print("Original String : " + test_string)
    
#     # using filter() to
#     # remove bad_chars
#     test_string = ''.join((filter(lambda i: i not in bad_chars, test_string)))
#     # printing resultant string
#     # print("Resultant list is : " + str(test_string))
#     re.sub(' +', ' ', test_string)
#     print("Resultant list is : " + str(test_string))
   
   

for t in listfont:
    # font_path = "fonts/{}/".format(t[0])
    # font_name = t[1]
    # out_path = "Dataset2/{}/{}/".format(t[0],t[3])

    # font_size = 30 # px
    # font_color = "#000000" # HEX Black
    # bg_color = '#ffffff'
    # width = 1000 
    # height = 100

    # # Create Font using PIL
    # font = ImageFont.truetype(font_path+font_name, font_size)

    list_of_rows = [list(row) for row in df.values]
   
    for dataset in list_of_rows:
         # initializing bad_chars_list
        bad_chars = [';', "*" , "" , "#" , "&quote" , "&quot"]
        
        # initializing test string
        test_string = dataset[4]
             
        # using filter() to
        # remove bad_chars
        test_string = ''.join((filter(lambda i: i not in bad_chars, test_string)))
        
        re.sub(' +', ' ', test_string)
        # Create PNG Image with that size
        img = Image.new("RGBA", (width, height), color=bg_color)
        draw = ImageDraw.Draw(img)
        position = (40,25)
                    
        # Draw the character
        draw.text(position, str(test_string), font=font, fill=font_color)

        # Save the character as png
        # try:
        #     #img.save(out_path + "format_"  + t[0] + "_" + t[3] + "_" + "nn{}".format(dataset[1]) + ".png")
        #     file_name = out_path + "format_" + t[0] + "_" + t[3] + "_" + "nn{}".format(dataset[1]) + ".gt.txt"
        #     file = codecs.open(file_name, "w", "utf-8") 
        #     file.write("{}".format(test_string)) 
        #     file.close() 
        # except:
        #     print(f"[-] Couldn't Save:\t{dataset[1]}")