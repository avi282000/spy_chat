#spy_users
import random
usr_nm_num=random.randint(1,999999)
class spy_cred:
	num_spies=0
	def __init__(self,fname,lname,age,rate):
		self.f=fname
		self.l=lname
		self.age=age
		self.usr_nm=fname.lower() + "." + lname[0:3].lower() + str(usr_nm_num) 
		self.rate=rate
		self.st="Busy"
		spy_cred.num_spies+=1
	def usr_name(self):
		return ("{0}".format(self.usr_nm))
	def prof(self):
		return ("Name: {0},{1}\n\nAge: {2}\n\nRating: {3}\n\nStatus: {4}".format(self.l,self.f,self.age,self.rate,self.st))
	def rate(self):
		return ("{0}".format(self.rate))

avi=spy_cred("Avi","Vashisht",18,"4")
avi.usr_nm=("avi.vas213866")
dheeraj=spy_cred("Dheeraj","Shrivastava",18,"4")
dheeraj.usr_nm=("dheeraj.shr413977")
#print(dheeraj.usr_nm)
mason=spy_cred("Alex","Mason",32,"5")
mason.usr_nm=("alex.mas139198")
#print(mason.usr_nm)
clay=spy_cred("Lincoln","Clay",28,"5")
clay.usr_nm=("lincoln.cla257910")
#print(clay.usr_nm)
woods=spy_cred("Frank","Woods",34,"5")
woods.usr_nm=("frank.woo831771")
#print(woods.usr_nm)
john=spy_cred("John","Donnovan",29,"*5")
john.usr_nm=("john.don784370")
#print(john.usr_nm)