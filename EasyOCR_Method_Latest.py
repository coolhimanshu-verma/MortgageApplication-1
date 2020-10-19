import easyocr
# import PIL
# from PIL import ImageDraw
# import sys

reader = easyocr.Reader(['en'], gpu = False) #download the model
image = "imagesample.png"#sys.argv[-1]  

class EasyOCR:        
    __instance = None
    def __init__(self):
        """ Virtually private constructor. """
        if EasyOCR.__instance != None:
             raise Exception("This class is a singleton!")
#            print("This class is a singleton!")
        else:            
            EasyOCR.__instance = self
            
    def OCRprocessing(self, image, color='yellow', width=2):
        bounds = reader.readtext(image) # Doing OCR. Get bounding boxes.
#         self.draw_boxes(image, bounds)
#         draw = ImageDraw.Draw(image)
#         for bound in self.bounds:
#             p0, p1, p2, p3 = bound[0]
#             draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)        
        for i in bounds:
            print(i[1])           
#       return image  

             
OCR_obj = EasyOCR()
OCR_obj.OCRprocessing(image)