__author__ = 'joey'

from svmutil import *

train_jpgs = ['1j', '2j', '3j', '4j', '1q', '2q', '3q', '4q', '1k', '2k', '3k', '4k']

y, x = svm_read_problem('feature/train.txt')
y2, x2 = svm_read_problem('feature/test.txt')
m = svm_train(y[:250], x[:250], '-c 5')
label, acc, val = svm_predict(y2[0:], x2[0:], m, '-b 0')
print y2
print label

#print jpgs[label]
