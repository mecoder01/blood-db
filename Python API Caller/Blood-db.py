#/!python
#!/usr/bin/python

import requests
import sys
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print ("""
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@#(&@@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@(((((@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@%(((((((@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@((((((((((%@@@@@@@@@@@@@@@@@@
     @@@@@@@@@(((((((((((((@@@@@@@@@@@@@@@@@
     @@@@@@@@(((((((((((((((@@@@@@@@@@@@@@@@
     @@@@@@%(((((((((((((((((@@#((%@@@@@@@@@
     @@@@@%((((((((((((((((((@((((((@@@@@@@@
     @@@@(((((((((((((((((((%((((((((@@@@@@@
     @@@%(((((((((((((((((%&((((((((((%@@@@@
     @@@(((((((((((((((((@%((((((((((((@@@@@
     @@#((((((((((((((((@%((((((((((((((&@@@
     @@(. /((((((((((((@%((((((((((((((((@@@
     @@%(  ((((((((((((@((((((((((((((((((@@
     @@@(  .(((((((((((@( *((((((((((((((%@@
     @@@@(.  ((((((((((%@( ((((((((((((((@@@
     @@@@@%(    ,(((((((%@(   (((((((((%@@@@
     @@@@@@@@(((.  *(((((((@@%(((((((@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__________________________________________________

\t"""+bcolors.OKBLUE+bcolors.BOLD+"""\thttps://blood-db.com"""+bcolors.ENDC+"""
__________________________________________________""")

def main():

	assert __file__ == sys.argv[0]

	try:
		bloodType = sys.argv[1]
		location = sys.argv[2]

	except IndexError:
		print (bcolors.OKBLUE+"""\n Usages :"""+bcolors.ENDC+""" *.py <bloodType> <location>
\n\t  """+bcolors.OKBLUE+"""Example:"""+bcolors.ENDC+""" *.py O- Kathmandu\n""")
		sys.exit(2)

	req = requests.get("https://api.blood-db.com/blood/list?bloodType={}&location={}".format(bloodType, location),
						   headers={"Accept":"application/json",
						   "Authorization":"Basic <You API Key Here>" #Your API Key
						  })
	output = req.text
	data = json.loads(output)

	if("success': 0" in str(data)):
		print("""\n\t\tSomething Went Wrong!!!
__________________________________________________""")

	else:

		for loop in data['result']:
			print ("\n Name\t\t\t:", loop['name'],bcolors.BOLD+bcolors.FAIL+"("+loop['blood_group']+")"+bcolors.ENDC)
			print (" Address\t\t:", loop['current_address'])
			print (" Contact No\t\t:", bcolors.BOLD+bcolors.OKBLUE+loop['phone_number']+bcolors.ENDC)
			print (" Want To Donate?\t:", bcolors.BOLD+bcolors.FAIL+loop['wantdonate']+bcolors.ENDC)
			print (" Gender\t\t\t:", loop['gender'])
			print ("__________________________________________________")
	
	print ('''
\t  Powered By '''+bcolors.BOLD+bcolors.OKBLUE+'''"TheNittam & TheTeam"'''+bcolors.ENDC+'''
__________________________________________________''')

if __name__ == '__main__':
	main()
