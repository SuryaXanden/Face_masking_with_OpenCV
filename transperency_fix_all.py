from PIL import Image
from glob import glob
files_list = glob(r"*.png")
for file in files_list:
    print(file)
    img = Image.open(file)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = [ item if (item[255] != 255 and item[1] != 255 and item[2] != 255) else (255, 255, 255, 0) for item in datas ]
    img.putdata(newData)
    img.save(file, "PNG")