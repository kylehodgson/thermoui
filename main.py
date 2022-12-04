from PIL import Image,ImageDraw,ImageFont
from thirdparty.waveshare_epd import epd2in13b_V4
import time

epd=epd2in13b_V4.EPD()

try:
    epd.init()
    font20=ImageFont.truetype("bmp/Font.ttc", 20)
    font18=ImageFont.truetype("bmp/Font.ttc", 18)
    image_bw=Image.new('1', (epd.height, epd.width), 255)
    image_ry=Image.new('1', (epd.height, epd.width), 255)
    draw_bw = ImageDraw.Draw(image_bw)
    draw_ry = ImageDraw.Draw(image_ry)
    draw_bw=ImageDraw.Draw(image_bw)
    draw_ry=ImageDraw.Draw(image_ry)
    draw_bw.text((8, 8), 'thermoWorld', font = font20, fill = 0)
    draw_bw.text((8, 32), 'thermo UI', font = font18, fill = 0)
    draw_ry.line((165,50,165,100), fill = 0)
    epd.display(epd.getbuffer(image_bw),epd.getbuffer(image_ry))
    time.sleep(2)
    epd.sleep()
except Exception as e:
    print(f"caught {repr(e)} exception {e}")


exit()

