'''
Initial idea is to group the users with similar location and then to find
the euclidean distance between each parameter.
Used binascii to convert the string into binary stream
'''
import numpy as np
def distance(nam1,nam2):
  def convert1(x):
    if x == '0':
      return 0
    else:
      return 1
  nl1 = nam1.split(' ')
  nl2 = nam2.split(' ')
  name1 = nl1[0].encode('ascii')
  name2 = nl2[0].encode('ascii')
  name11 = nl1[1].encode('ascii')
  name22 = nl2[1].encode('ascii')
  n1 = bin(int(binascii.hexlify(name1),16))
  n2 = bin(int(binascii.hexlify(name2),16))
  n11 = bin(int(binascii.hexlify(name11),16))
  n22 = bin(int(binascii.hexlify(name22),16))
  b1 = list(n1)
  b2 = list(n2)
  b11 = list(n11)
  b22 = list(n22)
  #Remove the character 'b' added in the binary stream representation
  b1.remove('b')
  b2.remove('b')
  b11.remove('b')
  b22.remove('b')
  c1 = list(map(convert1,b1))
  c2 = list(map(convert1,b2))
  c11 = list(map(convert1,b11))
  c22 = list(map(convert1,b22))
  a1 = np.asarray(c1)
  a2 = np.asarray(c2)
  a11 = np.asarray(c11)
  a22 = np.asarray(c22)
  #Padding the lists to generalise the size
  l1 = 1024-len(a1)
  l2 = 1024-len(a2)
  l11 = 1024-len(a11)
  l22 = 1024-len(a22)
  fn1 = np.pad(a1,(l1,0),mode='constant')
  fn2 = np.pad(a2,(l2,0),mode='constant')
  ln1 = np.pad(a11,(l11,0),mode='constant')
  ln2 = np.pad(a22,(l22,0),mode='constant')
  #Euclidean distance between the names
  distfn = np.linalg.norm(fn1-fn2)
  distln = np.linalg.norm(ln1-ln2)
  bias = 0.0
  if distfn==0:
    bias += 1.50
  if distln==0:
    bias += 1
  if distfn==0.0 and distln==0.0:
    return 0.0
  points = abs(distfn*1 + distln*0.6 - bias)
  return points
#print(distance('John Doe','John D'))