__author__ = 'joey'

from jpgtodata import todata

f = file('feature/test.txt', 'w')
train_jpgs = ['1j', '2j', '3j', '4j', '1q', '2q', '3q', '4q', '1k', '2k', '3k', '4k']
test_jpgs = ['1kx', '1kx2', '1qx', '3kx', '3kx2', '4jx', '2qx2']

for i in range(0, len(test_jpgs)):
    xyarr = todata("test_sample/%s.jpg" % test_jpgs[i])

    jpgn = test_jpgs[i][0:2]

    for j in range(0, len(train_jpgs)):
        if (jpgn == train_jpgs[j]):
            f.write('%s' % j)

    for m in range(1, len(xyarr) + 1):
        f.write(' %s:%s' % (m, xyarr[m - 1]))

    f.write('\n')
f.close()