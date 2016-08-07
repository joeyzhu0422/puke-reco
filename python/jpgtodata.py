__author__ = 'joey'

import numpy
import Image

def todata(path):
    im = Image.open(path)
    Lim = im.convert("1")

    sim = Lim.resize((75, 100), Image.ANTIALIAS)

#    sim.show()

    pixdata = sim.load()

    x, y = sim.size

    xarr = numpy.zeros(x)
    yarr = numpy.zeros(y)

    for j in xrange(y):
        for i in xrange(x):
        #        print i, j, pixdata[i, j]
            if pixdata[i, j] == 0:
                xarr[i] = xarr[i] + 1
                #            print xarr
                yarr[j] = yarr[j] + 1

    xyarr = numpy.hstack((xarr, yarr))
    return xyarr