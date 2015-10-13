# Author : http://github.com/jeonghoonkang/

import matplotlib.font_manager

myfnt =  matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
print len(myfnt)
print myfnt  

strings = str(myfnt)

print

if strings.find('NanumGothic.ttf') > 0:
    print 'found NanumGothic.ttf'



