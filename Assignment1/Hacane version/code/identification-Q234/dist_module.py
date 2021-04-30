# 
# compute chi2 distance between x and y
import numpy as np
def dist_chi2(x,y):
  # your code here
  if(np.sum(x) != np.sum(y)):
    print("Warning! the two hitograms are not normalized to the same unit therefore they cant be compared")

  d=0
  for i in range(0,x.size): 
    if(float(x[i]) != 0.0): #if the value is zero means the bin is empty therfore its not comparable 
      d+=((x[i]-y[i])**2)/x[i]

  return d

# 
# compute l2 distance between x and y
#
def dist_l2(x,y):
  # your code here
  if(np.sum(x) != np.sum(y)):
    print("Warning! the two hitograms are not normalized to the same unit therefore they cant be compared")

  d=0
  for i in range(0,x.size): 
    d+=(x[i]-y[i])**2
  d=d**0.5
  return d

# 
# compute intersection distance between x and y
# return 1 - intersection, so that smaller values also correspond to more similart histograms
#
def dist_intersect(x,y):
  # your code here
  if(np.sum(x) != np.sum(y)):
    print("Warning! the two hitograms are not normalized to the same unit therefore they cant be compared")

  d=0
  for i in range(0,x.size): 
    d+=min(x[i],y[i])

  return d







def get_dist_by_name(x, y, dist_name):
  if dist_name == 'chi2':
    return dist_chi2(x,y)
  elif dist_name == 'intersect':
    return dist_intersect(x,y)
  elif dist_name == 'l2':
    return dist_l2(x,y)
  else:
    assert 'unknown distance: %s'%dist_name
  




