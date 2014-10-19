#http://docs.python-guide.org/en/latest/scenarios/scrape/
#from subprocess import call
from lxml import html #Html parsing
import requests #Request page from server
from wand.image import Image # Image manipulator http://wand-py.org
from urllib2 import urlopen # Open image url for imageMagickWand to parse
from datetime import datetime

def pyScrape(i):    
    page = requests.get('http://tldrwikipedia.tumblr.com/')
    parsed_html = page.text
    tree = html.fromstring(page.text)
    
    #posts = tree.xpath('//div[@class="post photo"]/text()')
    #print tree
    post= tree.find_class('post photo')
    # Take first instance of the post photo div list
    div_photo = html.tostring(post[i])
    # Remove whitespace and then add in single spaces
    div_clean = ' '.join(div_photo.split())
    # Re-parse individual posts
    divtree = html.fromstring(div_clean)
    # Get Link to image
    pImages = divtree.xpath("//img/@src")
    pDate = divtree.find_class('date')
    print div_clean
    print pImages[0]
    print pDate[0].text_content() 
    return {'pImage': str(pImages[0]), 'pDate': str(pDate[0].text_content())}    
    #call(['convert', 'test.png -colorspace RGB +sigmoidal-contrast 11.69 -define filter:filter=Sinc -define filter:window=Jinc -define filter:lobes=3 -resize 400% -sigmoidal-contrast 11.69 -colorspace sRGB output.png'])
    '''
    f = urlopen(images[0])
    
    
    imgmgkarg = f, ' +sigmoidal-contrast 11.69 -define filter:lobes=3 -resize 400% ', imgdate, '.png'
    call(['convert '+str(imgmgkarg)])
    '''
def resizeImg(pImages):
    dt = datetime.now()
    #imgdate = dt.strftime('%Y.%m.%d_%H.%M')+'.png'
    f = urlopen(pImages)
    with Image(file=f) as img:
       #width = img.width
       #height = img.height
        print 'initial size: ' + str(img.size)
       #img.gravity('East')
        img.crop(0, 0, width=350, height=150)
        img.transform(resize='400%')
        img.save(filename='output.png')
        print 'final size: ' + str(img.size)
    f.close()
#resizeImg()
