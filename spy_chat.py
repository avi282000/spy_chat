#Spy_chat
from os import system,name          #For defining the "clear screen" function
from PIL import Image
def genData(data):					#For converting the data into 8-Bit binary form using the ASCII value of its characters
	newd=[]							
	for i in data:
		newd.append(format(ord(i),"08b"))			#Just a list of all the binary codes of the given data
	return newd
def modpix(pix,data):
	data_list=genData(data)
	len_data=len(datalist)
	imdata=iter(pix)
	for i in range(lendata):
		pix=[value for value in imdata.__next__()[:3]+imdata.__next__()[:3]+imdata.__next__()[:3]]
		for j in range(0,8):
			if(data_list[i][j]=="0") and (pix[j]%2!=0):
				if(pix[j]%2!=0):
					pix[j]-=1
			elif(data_list[i][j]=="1") and (pix[j]%2==0):
				pix[j]-=1
			if(i==len_data-1):
				if(pix[-1]%2==0):
					pix[-1]-=1
				else:
					if(pix[-1]%2!=0):
						pix[-1]-=1
				pix=tuple(pix)
				yield pix[0:3]
				yield pix[3:6]
				yield pix[6:9]

def encode_enc(newimg,data):
	w=newimg.size[0]
	(x,y)=(0,0)
	for pixel in modPix(newimg.genData(),data):
		newimg.putpixel((x,y),pixel)
		if(x==w-1):
			x=0
			y+=1
		else:
			x+=1

def encode():
	img=input("Enter the image's name (extension included): ")
	image=Image.open(img,"r")
	msg=input("Enter the message: ")
	if(len(msg)==0):
		raise ValueError("No message found!")
	newimg=image.copy()
	encode_enc(newimg,msg)
	new_img_name=input("Enter the name of the new image (extension included): ")
	newimg.save(new_img_name,str(new_img_name.split(".")[1].upper()))

def decode():
	img=input("Enter the image's name(extension included): ")
	image=Image.open(img,"r")
	data=""
	imgdata=iter(image.getdata())
	while(True):
		pixels=[value for value in imgdata.__next__()[:3]+imgdata.__next__()[:3]+imgdata.__next__()[:3]]
		bin_str=""
		for i in pixels[:8]:
			if(i%2==0):
				bin_str+="0"
			else:
				bin_str+="1"
		data+=chr(int(binstr,2))
		if(pixels[-1]%2!=0):
			print("Decoded word:")
			return data

def clear():
	if name=="nt":
		_=system("cls")
	else:
		_=system("clear")

import random					#For the randint at the end of the user name
from time import sleep			#For keeping thedisplay "awake" for a few seconds before clearing the screen
import users					#The module containg the pre-defined usernames and, most importantly, the spy_cred class
class stat:						#The status class 
	def __init__(self,stat):
		self.stat=stat
	def status(self):
		return ("Status: " + "{0}".format(self.stat))
bsy=stat("Busy")
wrk=stat("Working")
undcvr=stat("Undercover")
bckp=stat("Need Backup")
cmhm=stat("Coming Home")
drp=stat("Requesting a drop")
dl=stat("Dealing")

#class upd_user:												..............................................Just a remmanant
#	def __init__(self,fname,lname,age,rate,stat):
#		self.f=fname
#		self.l=lname
#		self.ag=age
#		self.rate=rate
#		self.st=stat
#	def prof():
#		if self.st=="":
#			return ("{0}\n{1}\n{2}\n{3}".format(self.f,self.l,self.ag,self.rate,"Busy"))
#		else:
#			return ("{0}\n{1}\n{2}\n{3}".format(self.f,self.l,self.ag,self.rate,self.st))


name=users.spy_cred("oiugytcfxdcfytugihkbvjgjkn","ertfyguhiokplnvghjbks",8794653210,"*")	#Just a placeholder for line no. 
print("Greetings fellow traveller!")		
phrase=input("Enter the phrase here:")			#The phrase
if phrase=="peaceThroughpower":
	user=input("Do you wish to start a new jorney with us or are you a known aquiantance of us already? (Answer '1' or '2',respectively,for either):")

	if user=="1":													#Creating a new user
		print("We are certainly pleased!")
		first_name=input("Enter your first name here:")
		last_name=input("Enter your last name here:")
		usr_age=input("Enter your age here:")
		rating=input("What is your rating?	")
		if rating=="1":
			print("You need to work hard!")
		elif rating=="2":
			print("You're at the edge! Work harder!!")
		elif rating=="3":
			print("Keep going!")
		elif rating=="4":
			print("Good! But I've seen better!")
		elif rating=="5":
			print("You're one of the best!Better watch your back!We do not wish to lose your skills.")
		else:
			print("INTRUDER! YOU SHALL BE PUNISHED FOR SUCH ACT OF COWARDICE!")
			quit()                          
		if usr_age.isdigit()==False:		      #Checking the user's age

			while usr_age.isdigit()==False:
				print("We feel disrespected by such act of humour!")
				sleep(4)
				clear()
				first_name=input("Enter your first name here:")
				last_name=input("Enter your last name here:")
				usr_age=input("Enter your age here:")
				rating=input("What is your rating?	")
				if rating=="1":
					print("You need to work hard!")
				elif rating=="2":
					print("You're at the edge! Work harder!!")
				elif rating=="3":
					print("Keep going!")
				elif rating=="4":
					print("Good! But I've seen better!")
				elif rating=="5":
					print("You're one of the best!Better watch your back!We do not wish to lose your skills.")
				else:
					print("INTRUDER! YOU SHALL BE PUNISHED FOR SUCH ACT OF COWARDICE!")
					quit()
		else:
			if int(usr_age)<12 or int(usr_age)>50:
				print("We do not hire employees of such age group.The program will now terminate in 3 seconds.")
				sleep(3)
				clear()
				quit()
			

			else:
				pass
		sleep(3)
		clear()
		print("Confirmation required.\nFirst name={0}\nLast name={1}\nAge={2}".format(first_name,last_name,usr_age))
		conf=input("Is the above mentioned information correct?\nType 'y' for Yes or 'n' for No:")
		if conf.capitalize()=="Y":
			name=users.spy_cred(first_name,last_name,usr_age,rating)
			clear()
			print("Splendid!\nYour username is {0}.This information will disappear in 10 seconds.".format(name.usr_nm))
			sleep(10)
			clear()
		elif conf.capitalize()=="N":
			while conf.capitalize()=="N":
				first_name=input("Enter your first name here:")
				last_name=input("Enter your last name here:")
				usr_age=input("Enter your age here:")
				rating=input("What is your rating?	")
				if rating=="1":
					print("You need to work hard!")
				elif rating=="2":
					print("You're at the edge! Work harder!!")
				elif rating=="3":
					print("Keep going!")
				elif rating=="4":
					print("Good! But I've seen better!")
				elif rating=="5":
					print("You're one of the best!Better watch your back!We do not wish to lose your skills.")
				else:
					print("INTRUDER! YOU SHALL BE PUNISHED FOR SUCH ACT OF COWARDICE!")
					quit()
				sleep(3)
				clear()
				print("Confirmation required.\nFirst name={0}\nLast name={1}\nAge={2}".format(first_name,last_name,usr_age))
				conf=input("Is the above mentioned information correct?\nType 'y' for Yes or 'n' for No:")
			name=users.spy_cred(first_name,last_name,usr_age,rating)
			clear()
			print("Splendid!\nYour username is {0}.This information will disappear in 10 seconds.".format(name.usr_nm))		
			sleep(10)
			clear()
		else:
			print("That is disrespectful!")
			hack=1
			while hack!=2:
				conf=input("Is the above mentioned information correct?\nType 'y' for Yes or 'n' for No:")
				if conf.upper()=="Y" or conf.upper()=="N":
					hack+=1
				else:
					pass
		name=users.spy_cred(first_name,last_name,usr_age,rating)

		aldy_usr=input("Enter your username here:")																	#The Salutation and the special message
		if aldy_usr=="avi.vas213866":
			print("Welcome back Agent Vashisht! We have been expecting your presence.....")
			name=avi
		elif aldy_usr=="dheeraj.shr413977":
			print("Welcome back Agent Shrivastava! We have been expecting your presence.....")
			name=dheeraj
		elif aldy_usr=="alex.mas139198":
			print("Welcome back Agent Mason! We have been expecting your presence.....")
			name=mason
		elif aldy_usr=="lincoln.cla257910":
			print("Welcome back Agent Clay! We have been expecting your presence.....")
			name=clay
		elif aldy_usr=="frank.woo831771":
			print("Welcome back Agent Woods! We have been expecting your presence.....")
			name=woods
		elif aldy_usr=="john.don784370":
			print("Welcome back Agent Donnovan! We have been expecting your presence.....")
			name=john
		elif aldy_usr==name.usr_nm:
			print("Welcome to our family, Agent {0}.You have made a brave decision joining us.\n By doing so, you, hereby, take this job as your last\n For if you go through it you shall not be remembered in the society for anything remarkable,but ,for the feats you perform, the world shall be forever greatful to you,\n And for you fail the job, your fate shall remain forever unknown to the world.\n There is NO TURNING BACK NOW!!".format(first_name.capitalize()))		
		else:
			print("USERNAME INVALID! THE PROGRAM WILL NOW TERMINATE!")

		code=input("The enlightenment here:")		#A code for proceeding further
		if code.upper()=="TIBERIUM":
			pass
		else:
			print("MARK MY WORDS INTRUDER, YOU WILL ANSWER FOR THIS ACT!!")
			sleep(3)
			clear()
			quit()

		print("Here's your identity:\n{0}".format(name.prof()))		#Displaying the credentials of the user
		sleep(10)
		clear()
		inp=input("Now that you have passed through the phase, what do you wish to do?\n1)Add a status update on your own.\n2)Choose from and existing list of status.\nType the option code here:")
		if inp=="1":							#The manual status update
			status=input("Type it here:")
			clear()
			print("Here's your updated information:\n{0}".format(name.prof()))
		elif inp=="2":							#The pre-defined status
			stat=input("Here's a list of status:\nBusy\nWorking\nUndercover\nNeed Backup\nComing Home\nRequesting a drop\nDealing")
			if stat=="1":
				clear()
				print(bsy.status())
			elif stat=="2":
				clear()
				print(wrk.status())
			elif stat=="3":
				clear()
				print(undcvr.status())
			elif stat=="4":
				clear()
				print(bckp.status())
			elif stat=="5":
				clear()
				print(cmhm.status())
			elif stat=="6":
				clear()
				print(drp.status())
			elif stat=="7":
				clear()
				print(dl.status())
			else:
				while stat!="1" or stat!="2" or stat!="3" or stat!="4" or stat!="5" or stat!="6" or stat!="7":
					stat=input("Type it again:")
				if stat=="1":
					clear()
					print(bsy.status())
				elif stat=="2":
					clear()
					print(wrk.status())
				elif stat=="3":
					clear()
					print(undcvr.status())
				elif stat=="4":
					clear()
					print(bckp.status())
				elif stat=="5":
					clear()
					print(cmhm.status())
				elif stat=="6":
					clear()
					print(drp.status())
				elif stat=="7":
					clear()
					print(dl.status())
				else:
					pass
				print("Here's your updated information:\n{0}".format(name.prof()))

		else:
				print("SUCH ACT OF COWARDICE WILL BE PUNISHED!")
				sleep(3)
				clear()
				quit()
		name.st=stat
		sleep(3)
		print("Updated!:\n{0}".format(name.prof()))
		sleep(10)
		clear()
		rqst=input("Do you wish to add an employee as your friend? (y/n) ")
		if rqst.upper()=="Y":
			frnd_fname=input("Type in the first name of your friend: ")
			frnd_lname=input("Type in the last name of your friend: ")
			frnd_age=input("Type in the age of your friend: ")
			frnd_rate=input("Type in the rating of your friend: ")
			if int(frnd_rate)<int(name.rate()):
				print("You cannot add a friend inferior than you! The program will terminate!")
			else:
				pass
			if frnd_fname.lower()=="avi" and frnd_lname.lower()=="vashisht" and frnd_age=="18" and frnd_rate=="4":
				print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
			elif frnd_fname.lower()=="dheeraj" and frnd_lname.lower()=="shrivastava" and frnd_age=="18" and frnd_rate=="4":
				print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
			elif frnd_fname.lower()=="alex" and frnd_lname.lower()=="mason" and frnd_age=="32" and frnd_rate=="5":
				print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
			elif frnd_fname.lower()=="lincoln" and frnd_lname.lower()=="clay" and frnd_age=="28" and frnd_rate=="5":
				print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
			elif frnd_fname.lower()=="frank" and frnd_lname.lower()=="woods" and frnd_age=="34" and frnd_rate=="5":
				print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
			elif frnd_fname.lower()=="john" and frnd_lname.lower()=="donnovan" and frnd_age=="29" and frnd_rate=="5":
				print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
			else:
				print("There is no such employee in our directory.The program will terminate in 3 seconds")
				sleep(3)
				clear()
				quit()
	elif user=="2":
		aldy_usr=input("Enter your username here:")
		if aldy_usr=="avi.vas213866":
			print("Welcome back Agent Vashisht! We have been expecting your presence.....")
			name=avi
		elif aldy_usr=="dheeraj.shr413977":
			print("Welcome back Agent Shrivastava! We have been expecting your presence.....")
			name=dheeraj
		elif aldy_usr=="alex.mas139198":
			print("Welcome back Agent Mason! We have been expecting your presence.....")
			name=mason
		elif aldy_usr=="lincoln.cla257910":
			print("Welcome back Agent Clay! We have been expecting your presence.....")
			name=clay
		elif aldy_usr=="frank.woo831771":
			print("Welcome back Agent Woods! We have been expecting your presence.....")
			name=woods
		elif aldy_usr=="john.don784370":
			print("Welcome back Agent Donnovan! We have been expecting your presence.....")
			name=john
		elif aldy_usr==name.usr_nm:
			print("Welcome to our family, Agent {0}.You have made a brave decision joining us.\n By doing so, you, hereby, take this job as your last\n For if you go through it you shall not be remembered in the society for anything remarkable,but ,for the feats you perform, the world shall be forever greatful to you,\n And for you fail the job, your fate shall remain forever unknown to the world.\n There is NO TURNING BACK NOW!!".format(first_name.capitalize()))		
		
		else:
			print("USERNAME INVALID! THE PROGRAM WILL NOW TERMINATE!")
			quit()
		code=input("The enlightenment here:")
		if code.upper()=="TIBERIUM":
			pass
		else:
			print("MARK MY WORDS INTRUDER, YOU WILL ANSWER FOR THIS ACT!!")
			sleep(3)
			clear()
			quit()

		print("Here's your identity:\n{0}".format(name.prof()))
		sleep(10)
		clear()
		inp=input("Now that you have passed through the phase, what do you wish to do?\n1)Add a status update on your own.\n2)Choose from and existing list of status.\nType the option code here:")
		status=input("Type it here:")
		clear()
	elif inp=="2":
			stat=input("Here's a list of status:\nBusy\nWorking\nUndercover\nNeed Backup\nComing Home\nRequesting a drop\nDealing")
			if stat=="#":
				clear()
				print(bsy.status())
			elif stat=="##":
				clear()
				print(wrk.status())
			elif stat=="###":
				clear()
				print(undcvr.status())
			elif stat=="####":
				clear()
				print(bckp.status())
			elif stat=="#####":
				clear()
				print(cmhm.status())
			elif stat=="######":
				clear()
				print(drp.status())
			elif stat=="#######":
				clear()
				print(dl.status())
			else:
				while stat!="#" or stat!="##" or stat!="###" or stat!="####" or stat!="#####" or stat!="######" or stat!="#######":
					stat=input("Type it again:")
	else:
			print("SUCH ACT OF COWARDICE WILL BE PUNISHED!")
			sleep(3)
			clear()
			quit()
	name.st=stat
	sleep(3)
	print("Updated!:\n{0}".format(name.prof()))
	sleep(10)
	clear()
	rqst=input("Do you wish to add an employee as your friend? (y/n) ")
	if rqst.upper()=="Y":
		frnd_fname=input("Type in the first name of your friend: ")
		frnd_lname=input("Type in the last name of your friend: ")
		frnd_age=input("Type in the age of your friend: ")
		frnd_rate=input("Type in the rating of your friend: ")
		if int(frnd_rate)<int(name.rate()):
			print("You cannot add a friend inferior than you! The program will terminate!")
		else:
			pass
		if frnd_fname.lower()=="avi" and frnd_lname.lower()=="vashisht" and frnd_age=="18" and frnd_rate=="4":
			print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
		elif frnd_fname.lower()=="dheeraj" and frnd_lname.lower()=="shrivastava" and frnd_age=="18" and frnd_rate=="4":
			print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
		elif frnd_fname.lower()=="lincoln" and frnd_lname.lower()=="clay" and frnd_age=="28" and frnd_rate=="5":
			print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
		elif frnd_fname.lower()=="frank" and frnd_lname.lower()=="woods" and frnd_age=="34" and frnd_rate=="5":
			print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
		elif frnd_fname.lower()=="john" and frnd_lname.lower()=="donnovan" and frnd_age=="29" and frnd_rate=="5":
			print("Success! {0} is now your new friend!".format(frnd_fname.lower().capitalize()))
		else:
				print("There is no such employee in our directory.The program will terminate in 3 seconds")
				sleep(3)
				clear()
				quit()
		msg_rqst=input("Do you wish to send a message to your new friend or read a message he has sent to you? (It will be secure) (Type in 1 or 2,for each option,respectively) ")
		if msg_rqst.upper()=="Y":
			encode()
		elif msg_rqst.upper()=="N":
			decode()
	else:

		print("Goodbye!")
		quit()		
else:
	clear() 
