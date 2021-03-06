##Maths file

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
  
  def power(num,power):

    mynum = 1
    mypower = power
    
    while mypower != 0:

      mynum *= num
      mypower -= 1

    return mynum


  def dec2bin(self,num):

    mynum = num                 #Supports byte but not greater than byte
    numarray = []
    binarray = [128,64,32,16,8,4,2,1]

    if type(mynum) != int:

      print(f"Looking for type Integer, got {type(mynum)}...\nExiting function call")
      return

    else:

      while mynum >=1:

          for i in range(len(binarray)):

            if mynum >= binarray[i]:

              mynum -= binarray[i]
              numarray.append(1)
            else:
              numarray.append(0)
            
    return numarray


  def IP2BIN(self,IP):


    splitIP = IP.split(".")
    binARR = []

    for i in range(len(splitIP)):

        binARR.append(self.dec2bin(int(splitIP[i])))
      
    print(binARR)

    

E = PyMaths() #Init of class object to use functions that need to use self

E.IP2BIN("192.168.1.2")


