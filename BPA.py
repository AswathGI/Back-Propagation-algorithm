####################################################################################
#                                                                                                                                                           #
#   Developer: Aswath G.I.                                                                                                                    #
#   Project: Back Propogation Algorithm                                                                                               #
#   Type: 2-input, 1-Hidden Layer,                                                                                                       #
#   Function: Bipolar Sigmoidal Function                                                                                            #
#                                                                                                                                                      #
################################################################################


#Getting 2- inputs data:
print("########################################################")
x1= float(input("X1 =  "))
x2= float(input("X2 =  "))
print("########################################################")

#Intializing 1- Hidden Layer
print(" Intializing 1- Hidden Layer -- Z1 & Z2  ")
print("########################################################")

#Getting Weights data:
w11 =  float(input("w11 =  "))
w12 =  float(input("w12 =  "))
w21 =  float(input("w21 =  "))
w22 =  float(input("w22 =  "))

v1 =  float(input("v1 =  "))
v2 =  float(input("v2 =  "))
print("########################################################")

#Getting Base data:
bz1 =  float(input("bz1 =  "))
bz2 =  float(input("bz2 =  "))
by =  float(input("bY =  "))
print("########################################################")

#Getting Target Value & Learning Rate:
t =  float(input("Target =  "))
alpha = float(input("Learning Rate =  "))
print("########################################################")

#Using Bipolar Sigmoidal Function
print("#                                                      #")
print("#     Initializing Bipolar Sigmoidal Function...       #")
print("#                                                      #")
print("########################################################")
print("  ")
print("  ")



#******************************************************************************************************************#

#  1. Feed Forward Phase
####################################################################################

#  Z1 & Z2
z1= (x1*w11)+(x1*w21)+bz1
z2= (x2*w12)+(x2*w22)+bz2

#  Function of Z1 & Z2
fz1 = (2/(1+ pow((2.718281828), -(1*z1)) ))-1
fz2 = (2/(1+ pow((2.718281828), -(1*z2)) ))-1

# Y - Output
y= (fz1*v1)+(fz2*v2)+by

#  Function of Y
fy = (2/(1+ pow((2.718281828), -(1*y)) ))-1

####################################################################################




#******************************************************************************************************************#

# 2. Back Propogation Algorithm
#                 |
#                 |__> From Output Layer to Hidden Layer
####################################################################################

#  Inverse Function of Y
f_y = (2*pow((2.718281828), -(1*y)) ) / (pow(1+pow((2.718281828), -(1*y)), 2))

#  Delta Y
Del_Y = (t-fy)*(f_y)

#  New Delta weights & base from Output Layer
Del_v1 = (alpha)*(Del_Y)*(fz1)
Del_v2 = (alpha)*(Del_Y)*(fz2)
Del_by = (alpha)*(Del_Y)

####################################################################################



#******************************************************************************************************************#

# 3. Back Propogation Algorithm
#                 |
#                 |__> From Hidden Layer to Input 
####################################################################################


#  Inverse Function of Z1 & Z2
f_z1 = (2*pow((2.718281828), -(1*z1)) ) / (pow(1+pow((2.718281828), -(1*z1)), 2))
f_z2 = (2*pow((2.718281828), -(1*z2)) ) / (pow(1+pow((2.718281828), -(1*z2)), 2))

#  Delta Z1 & Z2 from the new Output(i.e Del_Y)
Del_z1 = (Del_Y)*(v1)
Del_z2 = (Del_Y)*(v2)

#  Delta X1 & X2
Del_x1 = (Del_z1)*f_z1
Del_x2 = (Del_z2)*f_z2

#  New Delta weights from Hidden Layer
#
# From Hidden Layer Z1
Del_w11 = (alpha)*(Del_x1)*(x1)
Del_w12 = (alpha)*(Del_x2)*(x1)
#
# From Hidden Layer Z1
Del_w21 = (alpha)*(Del_x1)*(x2)
Del_w22 = (alpha)*(Del_x2)*(x2)

#  New Delta base from Hidden Layer
Del_bz1 = (alpha)*(Del_x1)
Del_bz2 = (alpha)*(Del_x2)

####################################################################################






#******************************************************************************************************************#

# 4. Updating All Weights and Base values
#
####################################################################################

#All Weights:
#
New_w11 = w11 + Del_w11
New_w12 = w12 + Del_w12
New_w21 = w21 + Del_w21
New_w22 = w22 + Del_w22
#
New_v1 = v1 + Del_v1
New_v2 = v2 + Del_v2

#All Base:
New_bz1 = bz1 + Del_bz1
New_bz2 = bz2 + Del_bz2
New_by = by + Del_by

####################################################################################




#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#                                                                                                                                                            #
#                                                 Finally printing the New Values                                                           #
#                                                                                                                                                           #
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

print("#")
print("#")
print("#")
print("#")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$                                Final Answers                                  $")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(" ")
print(" ")
print("  Weights  ")
print("--------------")
print(" ")
print("New_W11   =  %f" %New_w11)
print("New_W12   =  %f" %New_w12)
print("New_W21   =  %f" %New_w21)
print("New_W22   =  %f" %New_w22)
print(" ")
print(" ")
print("New_V1   =  %f" %New_v1)
print("New_V2   =  %f" %New_v2)
print("  Base  ")
print("----------")
print(" ")
print("New_bz1   =  %f" %New_bz1)
print("New_bz2   =  %f" %New_bz2)
print("New_bY   =  %f" %New_by)
print(" ")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")








