from PIL import Image,ImageDraw,ImageFont
from thirdparty.waveshare_epd import epd2in13b_V4
import time

epd=epd2in13b_V4.EPD()

try:
    epd.init()
    fontM=ImageFont.truetype("bmp/Font.ttc", 18)
    fontXL=ImageFont.truetype("bmp/Font.ttc", 80)
    fontL=ImageFont.truetype("bmp/Font.ttc", 40)
    image_bw=Image.new('1', (epd.height, epd.width), 255)
    image_ry=Image.new('1', (epd.height, epd.width), 255)
    draw_bw = ImageDraw.Draw(image_bw)
    draw_ry = ImageDraw.Draw(image_ry)
    draw_bw=ImageDraw.Draw(image_bw)
    draw_ry=ImageDraw.Draw(image_ry)
    draw_bw.text((4, 2), 'zone set to 22.0c', font = fontM, fill = 0)
    draw_bw.text((4, 100), 'current conditions', font = fontM, fill = 0)
    draw_bw.text((4, 20), '20.4c', font = fontXL, fill = 0)
    draw_bw.line((0,0,0,epd.width), fill = 0)
    draw_bw.line((0,0,epd.height,0), fill = 0)
    epd.display(epd.getbuffer(image_bw),epd.getbuffer(image_ry))
    epd.sleep()
except Exception as e:
    print(f"caught exception {e}")


exit()

