##Note - When trying to use a function, the object PyMath must be used. So in your own objects it would look something like

##PyMath.FSIA(arr1,arr2,total)


##PYMATH CLASS------------------------------------------------------------------------------------------------------------

decBins = []


for i in range(100):
  decBins.append(pow(2,i))
  

class PyMaths():

  def __init__(self):

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


  def Dec2Bin(self,num):

    mynum = num                 #Supports up to 100th binary number (633825300114114700748351602688)
    numarray = []
    binarray = [128,64,32,16,8,4,2,1]

    if type(mynum) != int:

      print(f"Looking for type Integer, got {type(mynum)}...\nExiting function call")
      return

    else:

      while mynum >=1:

          for i in range(len(binarray)):

            if mynum >= decBins[i]:

              mynum -= decBins[i]
              numarray.append(1)
            else:
              numarray.append(0)
            
    return numarray


  def IP2BIN(self,IP):
                            #This functions converts an IP address from its denary to its binary counterpart

    splitIP = IP.split(".")
    binARR = []

    for i in range(len(splitIP)):

        binARR.append(self.dec2bin(int(splitIP[i])))
      
    print(binARR)


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

    num1.reverse()
    num2.reverse() #NEEDS TO BE FIXED

    if type(num1)!= list or type(num2)!= list :

      print(f"Exiting function call, expected type list but got {type(num1)} and {type(num2)}")
      
    else:

      dec1 = 0
      dec2 = 0

      for i in range(len(num1)):

        if num1[i] == 1:
          dec1 += pow(2,i)
      for i in range(len(num2)):

        if num2[i] == 1:
          dec2 += pow(2,i)

      print(dec2)
      print(dec1)
      return(self.Dec2Bin(dec1+dec2))


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


PyMath = PyMaths()

x = PyMath.findFactors(36)

print(x)

###



