# IPython log file

import itertools
get_ipython().set_next_input(u'itertools.izip(itertools.repeat');get_ipython().magic(u'pinfo itertools.repeat')
itertools.combinations((-1, 0, 1), (-1. 0, 1))
itertools.combinations((-1, 0, 1), (-1, 0, 1))
itertools.combinations/
get_ipython().magic(u'pinfo itertools.combinations')
itertools.combinations((-1, 0, 1), 2)
#[Out]# <itertools.combinations object at 0x9529eb4>
list(itertools.combinations((-1, 0, 1), 2))
#[Out]# [(-1, 0), (-1, 1), (0, 1)]
list(itertools.permutations((-1, 0, 1), 2))
#[Out]# [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
list(itertools.permutations((-1, 0, 1), 2))
#[Out]# [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
list(itertools.product((-1, 0, 1)*2)
0
list(itertools.product((-1, 0, 1)*2))
#[Out]# [(-1,), (0,), (1,), (-1,), (0,), (1,)]
list(itertools.product((-1, 0, 1), (-1, 0, 1))
)
#[Out]# [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
print '\n'.join(itertools.product((-1, 0, 1), (-1, 0, 1)))
print '\n'.join(str(x) for x in itertools.product((-1, 0, 1), (-1, 0, 1)))
print '\n'.join(str(x[::-1]) for x in itertools.product((-1, 0, 1), (-1, 0, 1)))
(x[::-1] for x in itertools.product((-1, 0, 1), (-1, 0, 1)))
#[Out]# <generator object <genexpr> at 0x959402c>
print '\n'.join(x[::-1] for x in itertools.product((-1, 0, 1), (-1, 0, 1)))
print '\n'.join(str(x[::-1]) for x in itertools.product((-1, 0, 1), (-1, 0, 1)))
transforms=list(x[::-1] for x in itertools.product((-1, 0, 1), (-1, 0, 1)))
transforms
#[Out]# [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
point = (0,0)
for t in transforms:
   print t+point
for t in transforms:
   print t[0]+point[0], t[1]+point[1]
point=(20,20)
for t in transforms:
   print t[0]+point[0], t[1]+point[1]
for t in transforms:
   print t[0]+point[0], t[1]+point[1]
transforms
#[Out]# [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
transforms.remove(4)
transforms.pop(4)
#[Out]# (0, 0)
transforms
#[Out]# [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
for t in transforms:
   print t[0]+point[0], t[1]+point[1]
import collections
i=3
i+=2
i
#[Out]# 5
import random
get_ipython().magic(u'pinfo random.randint')
random.randint(0,1)
#[Out]# 0
random.randint(0,1)
#[Out]# 0
random.randint(0,1)
#[Out]# 1
random.randint(0,1)
#[Out]# 0
get_ipython().magic(u'pinfo random.gauss')
itertools.product(xrange(10), xrange(10))
#[Out]# <itertools.product at 0x9594aa4>
list(itertools.product(xrange(10), xrange(10)))
#[Out]# [(0, 0),
#[Out]#  (0, 1),
#[Out]#  (0, 2),
#[Out]#  (0, 3),
#[Out]#  (0, 4),
#[Out]#  (0, 5),
#[Out]#  (0, 6),
#[Out]#  (0, 7),
#[Out]#  (0, 8),
#[Out]#  (0, 9),
#[Out]#  (1, 0),
#[Out]#  (1, 1),
#[Out]#  (1, 2),
#[Out]#  (1, 3),
#[Out]#  (1, 4),
#[Out]#  (1, 5),
#[Out]#  (1, 6),
#[Out]#  (1, 7),
#[Out]#  (1, 8),
#[Out]#  (1, 9),
#[Out]#  (2, 0),
#[Out]#  (2, 1),
#[Out]#  (2, 2),
#[Out]#  (2, 3),
#[Out]#  (2, 4),
#[Out]#  (2, 5),
#[Out]#  (2, 6),
#[Out]#  (2, 7),
#[Out]#  (2, 8),
#[Out]#  (2, 9),
#[Out]#  (3, 0),
#[Out]#  (3, 1),
#[Out]#  (3, 2),
#[Out]#  (3, 3),
#[Out]#  (3, 4),
#[Out]#  (3, 5),
#[Out]#  (3, 6),
#[Out]#  (3, 7),
#[Out]#  (3, 8),
#[Out]#  (3, 9),
#[Out]#  (4, 0),
#[Out]#  (4, 1),
#[Out]#  (4, 2),
#[Out]#  (4, 3),
#[Out]#  (4, 4),
#[Out]#  (4, 5),
#[Out]#  (4, 6),
#[Out]#  (4, 7),
#[Out]#  (4, 8),
#[Out]#  (4, 9),
#[Out]#  (5, 0),
#[Out]#  (5, 1),
#[Out]#  (5, 2),
#[Out]#  (5, 3),
#[Out]#  (5, 4),
#[Out]#  (5, 5),
#[Out]#  (5, 6),
#[Out]#  (5, 7),
#[Out]#  (5, 8),
#[Out]#  (5, 9),
#[Out]#  (6, 0),
#[Out]#  (6, 1),
#[Out]#  (6, 2),
#[Out]#  (6, 3),
#[Out]#  (6, 4),
#[Out]#  (6, 5),
#[Out]#  (6, 6),
#[Out]#  (6, 7),
#[Out]#  (6, 8),
#[Out]#  (6, 9),
#[Out]#  (7, 0),
#[Out]#  (7, 1),
#[Out]#  (7, 2),
#[Out]#  (7, 3),
#[Out]#  (7, 4),
#[Out]#  (7, 5),
#[Out]#  (7, 6),
#[Out]#  (7, 7),
#[Out]#  (7, 8),
#[Out]#  (7, 9),
#[Out]#  (8, 0),
#[Out]#  (8, 1),
#[Out]#  (8, 2),
#[Out]#  (8, 3),
#[Out]#  (8, 4),
#[Out]#  (8, 5),
#[Out]#  (8, 6),
#[Out]#  (8, 7),
#[Out]#  (8, 8),
#[Out]#  (8, 9),
#[Out]#  (9, 0),
#[Out]#  (9, 1),
#[Out]#  (9, 2),
#[Out]#  (9, 3),
#[Out]#  (9, 4),
#[Out]#  (9, 5),
#[Out]#  (9, 6),
#[Out]#  (9, 7),
#[Out]#  (9, 8),
#[Out]#  (9, 9)]
list(x[::-1] for x in itertools.product(xrange(10), xrange(10)))
#[Out]# [(0, 0),
#[Out]#  (1, 0),
#[Out]#  (2, 0),
#[Out]#  (3, 0),
#[Out]#  (4, 0),
#[Out]#  (5, 0),
#[Out]#  (6, 0),
#[Out]#  (7, 0),
#[Out]#  (8, 0),
#[Out]#  (9, 0),
#[Out]#  (0, 1),
#[Out]#  (1, 1),
#[Out]#  (2, 1),
#[Out]#  (3, 1),
#[Out]#  (4, 1),
#[Out]#  (5, 1),
#[Out]#  (6, 1),
#[Out]#  (7, 1),
#[Out]#  (8, 1),
#[Out]#  (9, 1),
#[Out]#  (0, 2),
#[Out]#  (1, 2),
#[Out]#  (2, 2),
#[Out]#  (3, 2),
#[Out]#  (4, 2),
#[Out]#  (5, 2),
#[Out]#  (6, 2),
#[Out]#  (7, 2),
#[Out]#  (8, 2),
#[Out]#  (9, 2),
#[Out]#  (0, 3),
#[Out]#  (1, 3),
#[Out]#  (2, 3),
#[Out]#  (3, 3),
#[Out]#  (4, 3),
#[Out]#  (5, 3),
#[Out]#  (6, 3),
#[Out]#  (7, 3),
#[Out]#  (8, 3),
#[Out]#  (9, 3),
#[Out]#  (0, 4),
#[Out]#  (1, 4),
#[Out]#  (2, 4),
#[Out]#  (3, 4),
#[Out]#  (4, 4),
#[Out]#  (5, 4),
#[Out]#  (6, 4),
#[Out]#  (7, 4),
#[Out]#  (8, 4),
#[Out]#  (9, 4),
#[Out]#  (0, 5),
#[Out]#  (1, 5),
#[Out]#  (2, 5),
#[Out]#  (3, 5),
#[Out]#  (4, 5),
#[Out]#  (5, 5),
#[Out]#  (6, 5),
#[Out]#  (7, 5),
#[Out]#  (8, 5),
#[Out]#  (9, 5),
#[Out]#  (0, 6),
#[Out]#  (1, 6),
#[Out]#  (2, 6),
#[Out]#  (3, 6),
#[Out]#  (4, 6),
#[Out]#  (5, 6),
#[Out]#  (6, 6),
#[Out]#  (7, 6),
#[Out]#  (8, 6),
#[Out]#  (9, 6),
#[Out]#  (0, 7),
#[Out]#  (1, 7),
#[Out]#  (2, 7),
#[Out]#  (3, 7),
#[Out]#  (4, 7),
#[Out]#  (5, 7),
#[Out]#  (6, 7),
#[Out]#  (7, 7),
#[Out]#  (8, 7),
#[Out]#  (9, 7),
#[Out]#  (0, 8),
#[Out]#  (1, 8),
#[Out]#  (2, 8),
#[Out]#  (3, 8),
#[Out]#  (4, 8),
#[Out]#  (5, 8),
#[Out]#  (6, 8),
#[Out]#  (7, 8),
#[Out]#  (8, 8),
#[Out]#  (9, 8),
#[Out]#  (0, 9),
#[Out]#  (1, 9),
#[Out]#  (2, 9),
#[Out]#  (3, 9),
#[Out]#  (4, 9),
#[Out]#  (5, 9),
#[Out]#  (6, 9),
#[Out]#  (7, 9),
#[Out]#  (8, 9),
#[Out]#  (9, 9)]
list(x[::-1] for x in itertools.product(xrange(10), xrange(10)))
#[Out]# [(0, 0),
#[Out]#  (1, 0),
#[Out]#  (2, 0),
#[Out]#  (3, 0),
#[Out]#  (4, 0),
#[Out]#  (5, 0),
#[Out]#  (6, 0),
#[Out]#  (7, 0),
#[Out]#  (8, 0),
#[Out]#  (9, 0),
#[Out]#  (0, 1),
#[Out]#  (1, 1),
#[Out]#  (2, 1),
#[Out]#  (3, 1),
#[Out]#  (4, 1),
#[Out]#  (5, 1),
#[Out]#  (6, 1),
#[Out]#  (7, 1),
#[Out]#  (8, 1),
#[Out]#  (9, 1),
#[Out]#  (0, 2),
#[Out]#  (1, 2),
#[Out]#  (2, 2),
#[Out]#  (3, 2),
#[Out]#  (4, 2),
#[Out]#  (5, 2),
#[Out]#  (6, 2),
#[Out]#  (7, 2),
#[Out]#  (8, 2),
#[Out]#  (9, 2),
#[Out]#  (0, 3),
#[Out]#  (1, 3),
#[Out]#  (2, 3),
#[Out]#  (3, 3),
#[Out]#  (4, 3),
#[Out]#  (5, 3),
#[Out]#  (6, 3),
#[Out]#  (7, 3),
#[Out]#  (8, 3),
#[Out]#  (9, 3),
#[Out]#  (0, 4),
#[Out]#  (1, 4),
#[Out]#  (2, 4),
#[Out]#  (3, 4),
#[Out]#  (4, 4),
#[Out]#  (5, 4),
#[Out]#  (6, 4),
#[Out]#  (7, 4),
#[Out]#  (8, 4),
#[Out]#  (9, 4),
#[Out]#  (0, 5),
#[Out]#  (1, 5),
#[Out]#  (2, 5),
#[Out]#  (3, 5),
#[Out]#  (4, 5),
#[Out]#  (5, 5),
#[Out]#  (6, 5),
#[Out]#  (7, 5),
#[Out]#  (8, 5),
#[Out]#  (9, 5),
#[Out]#  (0, 6),
#[Out]#  (1, 6),
#[Out]#  (2, 6),
#[Out]#  (3, 6),
#[Out]#  (4, 6),
#[Out]#  (5, 6),
#[Out]#  (6, 6),
#[Out]#  (7, 6),
#[Out]#  (8, 6),
#[Out]#  (9, 6),
#[Out]#  (0, 7),
#[Out]#  (1, 7),
#[Out]#  (2, 7),
#[Out]#  (3, 7),
#[Out]#  (4, 7),
#[Out]#  (5, 7),
#[Out]#  (6, 7),
#[Out]#  (7, 7),
#[Out]#  (8, 7),
#[Out]#  (9, 7),
#[Out]#  (0, 8),
#[Out]#  (1, 8),
#[Out]#  (2, 8),
#[Out]#  (3, 8),
#[Out]#  (4, 8),
#[Out]#  (5, 8),
#[Out]#  (6, 8),
#[Out]#  (7, 8),
#[Out]#  (8, 8),
#[Out]#  (9, 8),
#[Out]#  (0, 9),
#[Out]#  (1, 9),
#[Out]#  (2, 9),
#[Out]#  (3, 9),
#[Out]#  (4, 9),
#[Out]#  (5, 9),
#[Out]#  (6, 9),
#[Out]#  (7, 9),
#[Out]#  (8, 9),
#[Out]#  (9, 9)]
from __future__ import print_function
get_ipython().magic(u'pinfo print')
import queue
import Queue
get_ipython().magic(u'pinfo Queue.Queue')
Queue.Queue
#[Out]# Queue.Queue
q = Queue.Queue(4)
q.qsize
#[Out]# <bound method Queue.qsize of <Queue.Queue instance at 0x95a148c>>
q.qsize()
#[Out]# 0
get_ipython().magic(u'pinfo q.put_nowait')
get_ipython().magic(u'pinfo q.put')
[q.put(n) for n in [1,2,3,4]]
#[Out]# [None, None, None, None]
[q.put(n) for n in range(5,7)]
