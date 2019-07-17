"""Assess a betting strategy. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Copyright 2018, Georgia Institute of Technology (Georgia Tech) 			  		 			     			  	   		   	  			  	
Atlanta, Georgia 30332 			  		 			     			  	   		   	  			  	
All Rights Reserved 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Template code for CS 4646/7646 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Georgia Tech asserts copyright ownership of this template and all derivative 			  		 			     			  	   		   	  			  	
works, including solutions to the projects assigned in this course. Students 			  		 			     			  	   		   	  			  	
and other users of this template code are advised not to share it with others 			  		 			     			  	   		   	  			  	
or to make it available on publicly viewable websites including repositories 			  		 			     			  	   		   	  			  	
such as github and gitlab.  This copyright statement should not be removed 			  		 			     			  	   		   	  			  	
or edited. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
We do grant permission to share solutions privately with non-students such 			  		 			     			  	   		   	  			  	
as potential employers. However, sharing with other current or future 			  		 			     			  	   		   	  			  	
students of CS 7646 is prohibited and subject to being investigated as a 			  		 			     			  	   		   	  			  	
GT honor code violation. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
-----do not edit anything above this line--- 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Student Name: Tucker Balch (replace with your name) 			  		 			     			  	   		   	  			  	
GT User ID: tb34 (replace with your User ID) 			  		 			     			  	   		   	  			  	
GT ID: 900897987 (replace with your GT ID) 			  		 			     			  	   		   	  			  	
""" 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
import numpy as np 			  		 			     			  	   		   	  			  	
import matplotlib.pyplot as plt 			  		 			     			  	   		   	  			  	
def author(): 			  		 			     			  	   		   	  			  	
        return 'tb34' # replace tb34 with your Georgia Tech username. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
def gtid(): 			  		 			     			  	   		   	  			  	
	return 900897987 # replace with your GT ID number 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
def get_spin_result(win_prob): 			  		 			     			  	   		   	  			  	
	result = False 			  		 			     			  	   		   	  			  	
	if np.random.random() <= win_prob: 			  		 			     			  	   		   	  			  	
		result = True 			  		 			     			  	   		   	  			  	
	return result 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
def test_code(length): 			  		 			     			  	   		   	  			  	
	win_prob = 9.0/19.0 # set appropriately to the probability of a win 			  		 			     			  	   		   	  			  	
	#np.random.seed(gtid()) # do this only once 
	plt.figure()
	plt.axis([0,300,-256,100])
	wins = np.zeros((length, 1000))
	for j in range(length):
		winnings = np.zeros(1000)
		ewin = 0
		i = 0
		while ewin < 80:
			won = False
			bet = 1
			while not won:
				won = get_spin_result(win_prob)
				i = i+1
				if won == True:
					ewin = ewin + bet
					winnings[i] = ewin
				else:
					ewin = ewin - bet
					winnings[i] = ewin
					bet = bet * 2
		winnings[i+1:] = 80
		wins[j, :] = winnings
		# add your code here to implement the experiments
	if length == 10:	
		for j in range(10):
			plt.plot(range(300), wins[j , 0:300])
		plt.title("10 different runs of betting mechanism")
		plt.show()
	else:
		mean_win = np.zeros(1000)
		std_win = np.zeros(1000)
		median_win = np.median(wins, axis = 1) #Case for median
		mean_win = wins.mean(axis = 1) #Case foe mean
		std_win = wins.std(axis=1)
		#Plug in reguired arrays
		plt.plot(range(300), mean_win[:300], color='r')
		plt.plot(range(300), mean_win[:300] + std_win[:300], color='b')
		plt.plot(range(300), mean_win[:300] - std_win[:300], color='b')
		plt.title("1000 runs - mean and std")
		plt.show()
def experiment2(length):
	win_prob = 9.0/19.0
	wallet = 256
	plt.figure()
	plt.axis([0,300,-256,100])
	wins = np.zeros((length, 1000))
	for j in range(length):
		winnings = np.zeros(1000)
		ewin = 0
		i = 0
		while winnings[i] > -256 and i<999:
			won = False
			bet = 1
			while not won and i<999:
				won = get_spin_result(win_prob)
				i = i+1
				if won == True:
					ewin = ewin + bet
					winnings[i] = ewin
				else:
					ewin = ewin - bet
					winnings[i] = ewin
					bet = bet * 2
					if bet>wallet+winnings[i]:
						bet = wallet+winnings[i]
		winnings[i+1:] = -256
		wins[j, :] = winnings
		# add your code here to implement the experiments
	mean_win = np.zeros(1000)
	std_win = np.zeros(1000)
	mean_win = wins.mean(axis = 1) #Case foe mean
	std_win = wins.std(axis=1)
	#Plug in reguired arrays
	plt.plot(range(300), mean_win[:300], color='r')
	plt.plot(range(300), mean_win[:300] + std_win[:300], color='b')
	plt.plot(range(300), mean_win[:300] - std_win[:300], color='b')
	plt.title("1000 runs - mean and std")
	plt.show()
if __name__ == "__main__":
	#test_code(10) - fro simple simulator
	test_code(1000)
	experiment2(1000)
