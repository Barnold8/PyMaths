##Note - When trying to use a function, the object of what you are trying to access has to be made. So a number function needs to have Number object. Then you can call a number function. This is because the class may need to refer to multiple functions in one method.



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
    
##------------------------------------------------------------------------------------------------------------

### AREA RESERVED FOR TESTING

E = IT()
x = E.IP2BIN("192.192.192.192")
print(x)
###



