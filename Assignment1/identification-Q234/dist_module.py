# 
# compute chi2 distance between x and y
#
def dist_chi2(x,y):
  # your code here
  dist=0
  for i in range(0,len(x)):
    dist+=((y[i]-x[i])**2)/(y[i]+1)
  # print("1jjj"+str(dist))
  return dist

# 
# compute l2 distance between x and y
#
def dist_l2(x,y):
  # your code here
  dist=0
  for i in range(0,len(x)):
    dist+=(y[i]-x[i])**2
  dist=dist**0.5
  # print("2hh"+str(dist))
  return dist

# 
# compute intersection distance between x and y
# return 1 - intersection, so that smaller values also correspond to more similart histograms
#
def dist_intersect(x,y):
  dist=0
  for i in range(0,len(x)):
    dist+=min(y[i],x[i])

  return 1-dist
  # your code here

def get_dist_by_name(x, y, dist_name):
  if dist_name == 'chi2':
    return dist_chi2(x,y)
  elif dist_name == 'intersect':
    return dist_intersect(x,y)
  elif dist_name == 'l2':
    return dist_l2(x,y)
  else:
    assert 'unknown distance: %s'%dist_name
  




