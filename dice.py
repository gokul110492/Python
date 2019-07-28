import sys
import random
import time

print
player_count = str(raw_input ("Number of Players: "))
i=0
player = []
def dice (m):
	if m == 1:
		print (""" 
				  _______
				|         |
				|         |
				|    *    | 
				|         | 
				|_________|  """)

	elif m == 2:
		print  ("""
			 _________
			|         |
			|     *   |
			|         | 
			|   *     | 
			|_________|  """)
      
	elif m == 3:
		print ("""
			 _________
			|         |
			|      *  |  
			|    *    | 
			|  *      | 
			|_________|  """) 
			
	elif m == 4:
		print ("""
			 _________
			|         |
			|  *   *  |  
			|         | 
			|  *   *  | 
			|_________|  """) 
	elif m == 5:
		print (""" 
			 _________
			|         |
			|  *   *  |  
			|    *    | 
			|  *   *  | 
			|_________|  """)
   
	elif m == 6:
		print ("""   
			 _________
			|         |
			|  *   *  |  
			|  *   *  | 
			|  *   *  | 
			|_________|  """)
while i<int(player_count):
	player_name = str(raw_input ("Enter player name please: "))
	player.append(player_name.upper())
	i=i+1
roll_again = "yes"
while roll_again == "yes": 
	if roll_again == "no":
		exit(0)
	k=0
	while k<int(player_count):
		t = random.randint(1, 6)
		print
		print ("{} Turn".format(player[k]))
		print
		time.sleep(1)
		print ("Rolling the die...")
		time.sleep (2)
		dice(t)
		k+=1
	roll_again = str(raw_input("Roll the die again?"))