class A(object):
    def __init__(self):
       print('A')


a = A()
dir(a)
'''
Results ----------
mAP: 19.8%
CMC curve
Rank-1  : 53.9%
Rank-5  : 74.9%
Rank-10 : 80.7%
Rank-20 : 85.2%
------------------
Finished. Total elapsed time (h:m:s): 6:04:07
'''