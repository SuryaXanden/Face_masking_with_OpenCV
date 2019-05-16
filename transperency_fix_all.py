from PIL import Image
from glob import glob
files_list = glob(r"images/*.png")
for file in files_list:
    print(file)
    img = Image.open(file)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(file, "PNG")
