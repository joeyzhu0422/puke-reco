__author__ = 'joey'

from jpgtodata import todata

f = file('feature/train.txt', 'w')
train_jpgs = ['1j', '2j', '3j', '4j', '1q', '2q', '3q', '4q', '1k', '2k', '3k', '4k']

for i in range(0, len(train_jpgs)):
    xyarr = todata("train_sample/%s.jpg" % train_jpgs[i])

    jpgn = train_jpgs[i][0:2]

    for j in range(0, len(train_jpgs)):
        if (jpgn == train_jpgs[j]):
            f.write('%s' % j)

    for m in range(1, len(xyarr) + 1):
        f.write(' %s:%s' % (m, xyarr[m - 1]))

    f.write('\n')
f.close()