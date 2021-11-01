from time import sleep
import time

# this function takes a number if seconds (int), coonverts that to weeks, days, hours, 
# minutes, seconds and 
# writes that to a file
def sec(s):

	seconds = s
	minutes = seconds // 60
	hours = minutes // 60
	days = hours // 24
	weeks = days // 7
	with open ('battery.txt', 'a') as file:
        	data = f'{weeks}w:{days%7}d:{hours%24}h:{minutes%60}m:{seconds%60}s\n'
        	file.write(str(data))



interval = 1 # interval in seconds
start_time = time.time() #finsd the start time 

while True:  
    uptime = (time.time() - start_time) #calculate the uptime
    sec(int(uptime)) #call the function and pass the up time in seconds
    sleep(interval)	#wait this long before doin the proccess again	

#print (f'{weeks}w:{days%7}d:{hours%24}h:{minutes%60}m:{seconds%60}s')