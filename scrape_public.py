import praw	
import csv

print("started successfully")

reddit = praw.Reddit(client_id='', client_secret='',
                     password='', user_agent='testscript by /u/haishiro',
                     username='')
					 
print(reddit.user.me())

pol = reddit.subreddit('politics')

for submission in pol.top('all',limit=1):
	comm = list(submission.comments)
	#for i in vars(comm):
	#	print(i)
	for c in comm:
		if c.score > 0:
			print(c.body)
	#TODO: MoreComments
	
	#with open('E:\\David\\Documents\\Northwestern\\W2018\\PRED 498\\Python Explore\\out.csv', 'w') as myfile:
	#	for item in vars(comm):
	#		myfile.write(item)