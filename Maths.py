##Note - When trying to use a function, the object of what you are trying to access has to be made. So a number function needs to have Number object. Then you can call a number function. This is because the class may need to refer to multiple functions in one method.

import math

##------------------------------------------------------------------IT
  

default_binary_list = []

for i in range(100):
  default_binary_list.append(pow(2,i))


class IT:

  def __init__(self):

    self.decBins = []
    self.number = Number()
    
    for i in range(200):
      self.decBins.append(pow(2,i))

  def IP2BIN(self,IP):
                            #This functions converts an IP address from its denary to its binary counterpart - Needs to be fixed

      splitIP = IP.split(".")
      binARR = []

      for i in range(len(splitIP)):

          binARR.append(self.number.Dec2Bin(int(splitIP[i])))
        
      return binARR

##------------------------------------------------------------------Number

class Number():

  def __init__(self):
    #used to allow object init
    pass

  def FSIA(arr1, arr2, total):

    working_sums = []

    for i in range(len(arr1)):
      for y in range(len(arr2)):
        
        if arr1[i] + arr2[y] >= total:


            working_sums.append(f"{arr1[i]} + {arr2[y]}")

            #find sums in arrays
  
    return working_sums
  
  def power(self,num,power):

    mynum = 1
    mypower = power
    
    while mypower != 0:

      mynum *= num
      mypower -= 1

    return mynum


  def Dec2Bin(self,num,binArr = default_binary_list, cleanup = True): #Default binary list can be used to define the highest numbers used for dec2bin

    numArray = []
    binArr.reverse()
  
    for i in range(len(binArr)):
      if num >= binArr[i]:
        num -= binArr[i]
        numArray.append(1)
      else:
        numArray.append(0)
   
    if cleanup:
      
      newARR = []
      found = False

      for i in range(len(numArray)):
      
        if found:
          newARR.append(numArray[i])
           
        elif numArray[i] == 1:
          found = True
  
      newARR.insert(0,1)    
      return newARR
      
      
    
    return numArray



  def Hex2Den(self,HexINP):

    nums = []
    x = HexINP.upper()
    emptList = []
    endNum = 0
    
    hexDict = {
      "A":10,
      "B":11,
      "C":12,
      "D":13,
      "E":14,
      "F":15
  }
    
    hexARR = list(x)
    
    for i in range(10):
      nums.append(str(i))
    
    for i in range(len(hexARR)):

      if hexARR[i] in nums:
        emptList.append(int(hexARR[i]))

      else:
        
        emptList.append(hexDict[hexARR[i]])

    emptList.reverse()
      
    for i in range(len(emptList)):


      endNum += emptList[i] * pow(16,i)
      

    return endNum


  def AddBinNums(self,num1,num2):

    ##ALL CODE DELETED BECAUSE THE FUNCTION DIDNT WORK

  ##TODO: FINISH THE FUNCTION
    pass


  def findFactors(self,num):

    factors = []
    filtered_factors = []
    for i in range(num+1):

      if i >=1:

        for y in range(num +1 ):
      
          temp = []     
          if i*y == num:
            temp.append(i)
            temp.append(y)
            factors.append(temp)

    for i in range(len(factors)):
      for y in range(1):
        filtered_factors.append(factors[i][y])
    return filtered_factors

  def LPWR(self,p,r):

    pows = []
    
    for i in range(r):
      if i !=0:
        x = self.power(i,p)
        pows.append(x)
    return pows


class Shapes:

  def __init__(self):

    pass

  def CCollider(self,obj1,obj2): #Takes to circles and sees if they have collided
    
    dx = obj1.x - obj2.x
    dy = obj1.y - obj2.y
    distance = math.sqrt(dx * dx + dy * dy)

    if distance < obj1.r + obj2.r:

      return True

    else:
      return False
    
  def RCollider(self,obj1,obj2): #Can be repurposed to be a sqaure on sqaure detector too. Just make w and h equal in shape definition


    if obj1.x < obj2.x + obj2.w and obj1.x + obj1.w > obj2.x and obj1.y < obj2.y + obj2.h and obj1.y + obj1.h > obj2.y : 

      return True
    else:
      return False
       
##------------------------------------------------------------------------------------------------------------

### AREA RESERVED FOR TESTING
    
##Dummy classes - These classes could be used to make a basic shape but when you can write your own it would be better

class Circle:

  def __init__(self,x,y,r):  #basic circle class to hold values of a circle
    
      self.x = x
      self.y = y
      self.r = r

class Rect:

  def __init__(self,x,y,w,h):

      self.x = x
      self.y = y
      self.w = w
      self.h = h

##-------------------

circle1 = Rect(100,10,5,3)
circle2 = Rect(10,12,5,4)

E = Shapes()
f = E.RCollider(circle1,circle2)
print(f)

###







