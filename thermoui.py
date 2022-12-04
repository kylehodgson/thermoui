from PIL import Image,ImageDraw,ImageFont
from thirdparty.waveshare_epd import epd2in13b_V4
import time

class ThermoUI:
    setpoint: float
    current: float
    def __init__(self) -> None:
        self.epd=epd2in13b_V4.EPD()
    def write_display(self, setpoint:float, current: float) -> None:
        line1=f"zone set to {setpoint}c"
        line2=f"{current}c"
        line3=f"current conditions"
        try:
            self.epd.init()
            fontM=ImageFont.truetype("bmp/Font.ttc", 18)
            fontXL=ImageFont.truetype("bmp/Font.ttc", 80)
            fontL=ImageFont.truetype("bmp/Font.ttc", 40)
            image_bw=Image.new('1', (self.epd.height, self.epd.width), 255)
            image_ry=Image.new('1', (self.epd.height, self.epd.width), 255)
            draw_bw = ImageDraw.Draw(image_bw)
            draw_ry = ImageDraw.Draw(image_ry)
            draw_bw=ImageDraw.Draw(image_bw)
            draw_ry=ImageDraw.Draw(image_ry)
            draw_bw.text((4, 2), line1, font = fontM, fill = 0)
            draw_bw.text((4, 20), line2, font = fontXL, fill = 0)
            draw_bw.text((4, 100), line3, font = fontM, fill = 0)
            draw_bw.line((0,0,0,self.epd.width), fill = 0)
            draw_bw.line((0,0,self.epd.height,0), fill = 0)
            self.epd.display(self.epd.getbuffer(image_bw),self.epd.getbuffer(image_ry))
            self.epd.sleep()
        except Exception as e:
            print(f"caught exception {e}")


