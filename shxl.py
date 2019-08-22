import pyexcel_xls as p
from collections import OrderedDict
import magicpen.fonts as fonts
import magicpen.tool as mps


fonts = [fonts.HW_XINGKAI, fonts.HW_KAITI, fonts.HW_FANGSONG, fonts.KAITI]
chars = mps.get_chars('./chars.txt')
data = OrderedDict()
row = ['']
row.extend(mps.get_fonts_names(fonts))
sheet = [row]
for char in chars:
    row = [char]
    for font in fonts:
        img = mps.get_gray_image(char, font, 400)
        percent = mps.get_percent(mps.PIL2CV(img, False))
        row.append(percent)
    sheet.append(row)
data.update({'Sheet': sheet})
p.save_data('font.xls', data)
