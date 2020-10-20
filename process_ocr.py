import easyocr
import os
import PIL
from PIL import ImageDraw


class ProcessOCR:

    __instance = None

    def __init__(self, imageName, debug=False):
        self.reader = easyocr.Reader(['en'], gpu=False)
        self.color = 'yellow'
        self.width = 2
        self.img = PIL.Image
        self.input_image = imageName
        self.bounds = None
        self.debug = debug

    @staticmethod
    def getInstance(imageName='', debug=False):
        if not ProcessOCR.__instance:
            ProcessOCR.__instance = ProcessOCR(imageName, debug)
        return ProcessOCR.__instance

    def draw_boxes(self):
        self.img = PIL.Image.open(self.input_image)
        draw = ImageDraw.Draw(self.img)
        for bound in self.bounds:
            p0, p1, p2, p3 = bound[0]
            draw.line([*p0, *p1, *p2, *p3, *p0], fill=self.color, width=self.width)

    def ocr_process(self):
        # TODO: Have this be asynchronous if possible.
        self.bounds = self.reader.readtext(self.input_image)  # Doing OCR(Get bounding boxes)
        if self.debug:
            self.draw_boxes()  # Draw bounding boxes

        # saving the output file
        current_directory = os.getcwd()
        output_directory = os.path.join(current_directory, r'ocr_output')
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        self.img.save(output_directory + "/" + self.input_image)

    def get_bounds(self):
        return self.bounds
