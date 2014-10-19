#dependencies: python >2.5, pyocr, PIL(Pillow), tesseract, imagemagick

#Image conversion for resizing and better quality through imagemagick
#convert test.png -colorspace RGB +sigmoidal-contrast 11.69 -define filter:filter=Sinc -define filter:window=Jinc -define filter:lobes=3 -resize 400% -sigmoidal-contrast 11.69 -colorspace sRGB output.png

from PIL import Image
import sys

import pyocr
import pyocr.builders

def outputOCR():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    tool = tools[0]
    #print("Will use tool '%s'" % (tool.get_name()))
    #print("Will use tool '%s'" % (tool.get_name()))
    # Ex: Will use tool 'tesseract'
    
    langs = tool.get_available_languages()
    #print("Available languages: %s" % ", ".join(langs))
    lang = langs[0]
    #print("Will use lang '%s'" % (lang))
    # Ex: Will use lang 'fra'
    
    txt = tool.image_to_string(Image.open('output.png'),
                               lang=lang,
                               builder=pyocr.builders.TextBuilder())
    #word_boxes = tool.image_to_string(Image.open('test.png'),
    #                                  lang=lang,
    #                                  builder=pyocr.builders.WordBoxBuilder())
    #line_and_word_boxes = tool.image_to_string(
    #        Image.open('test.png'), lang=lang,
    #        builder=pyocr.builders.LineBoxBuilder())
    
    txt = txt.replace("\r"," ")
    txt = txt.replace("\n"," ")
    #print txt
    #print "================"
    #print word_boxes
    #print "================"
    #print line_and_word_boxes
    # Digits - Only Tesseract
    #digits = tool.image_to_string(Image.open('test-digits.png'),
    #                              lang=lang,
    #                              builder=pyocr.tesseract.DigitBuilder())
    return txt
