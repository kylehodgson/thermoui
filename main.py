from PIL import Image,ImageDraw,ImageFont
from thirdparty.TP_lib import epd2in13_V3
from thirdparty.TP_lib import gt1151
import time

epd=epd2in13_V3.EPD()
gt = gt1151.GT1151()

try:
    epd.init(epd.FULL_UPDATE)
    gt.GT_Init()
    epd.Clear(0xFF)

    image=Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)
    font=ImageFont.truetype("bmp/Font.ttc", 24)
    draw.text((8, 12), 'thermoWorld', font = font, fill = 155)
    epd.display(epd.getbuffer(image))
    time.sleep(2)
except Exception as e:
    print(f"caught {typeof(e)} exception {e}")


print(f"exiting module")
epd.Dev_exit()
exit()

