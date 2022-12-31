import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# function name: least_sq
# inputs: file_name- name of the csv file
# output: m(slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY! return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!!!!
# assumptions: The csv file will always have headers in the order of: x, y
def least_sq(file_name):
	df_xy = pd.read_csv(file_name)
	np_x = df_xy['x'].to_numpy()
	np_y = df_xy['y'].to_numpy()
	np_x2 = np.square(np_x)
	np_xy = np.multiply(np_x,np_y)
	sumX= 0
	sumY = 0
	sumX2 = 0
	sumXY = 0
	n = len(np_x)
	for i in np_x:
		sumX+=i
	for i in np_y:
		sumY+=i
	for i in np_x2:
		sumX2+=i
	for i in np_xy:
		sumXY+=i
	m = ((n)*(sumXY)-sumX*sumY)/((n)*(sumX2)-(sumX)**2)
	b = (sumY-m*sumX)/n
	return (round(m,4),round(b,4))




# function name: mat_least_sq
# inputs: file_name- name of the csv file
# output: m (slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY! return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!
# assumptions: The csv file will always have headers in the order of: x, y
def mat_least_sq(file_name):
	df_xy = pd.read_csv(file_name)
	np_x = df_xy['x'].to_numpy()
	np_y = df_xy['y'].to_numpy()
	ones_vec = np.ones(len(np_x))

	x = (np.column_stack((np_x,ones_vec)))
	x2 = np.linalg.inv(np.dot(x.T, x))
	y = np.dot(x.T,np_y)
	xy = np.dot(x2,y)
	m =(xy[0])
	b = (xy[1])

	return (round(m,4),round(b,4))



# function name: plot_reg
# inputs: mat - file_name- name of the csv file
		# using_matrix: True if you are plotting the linear equation from mat_least_Sq
		# 				False if you are plotting the linear equation from least_sq
# output: NA
# task: given file_name, compute the linear equation using least_sq or mat_least_sq and graph results
	#	your graph should have the following: labeled x and y axes, title, legend
# assumptions: The csv file will always have headers in the order of: x, y
def plot_reg(file_name, using_matrix):
	df_xy = pd.read_csv(file_name)
	np_x=df_xy['x'].to_numpy()
	np_y= df_xy['y'].to_numpy()
	plt.scatter(np_x, np_y, label = "data points")
	plt.xlabel("x")
	plt.ylabel('y')

	max_value = np.max(np_x)

	if using_matrix == True:
		m,b = mat_least_sq(file_name)
		x = np.linspace(-50,max_value,100)
		y = m*x+b

		plt.plot(x, y, '-r',label=f"y={m}x+{b}")
		plt.title("Using Matrix least squares")


	if using_matrix == False:
		m, b = least_sq(file_name)
		x = np.linspace(-50,max_value,100)
		y = m * x + b
		plt.plot(x, y, '-r',label=f"y={m}x+{b}")
		plt.title("Using Algebra least squares")
	plt.legend()
	plt.show()










######## TEST CASES ########
#csv_file = "data2.csv"

#m1, b1 = least_sq(csv_file)
#print("Slope using algebraic least squares:", m1)
#print("y-intercept using algebraic least squares:", b1)
#print()

#m2, b2 = mat_least_sq(csv_file)
#print("Slope using linear algebra least squares:", m2)
#print("y-intercept using linear algebra least squares:", b2)

#plot_reg(csv_file, True)

#plot_reg(csv_file, False)


