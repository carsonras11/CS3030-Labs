import subprocess

def unsafe_run(user_input):
	subprocess.run(f"echo {user_input}", shell=True)

	# Its unsafe becasue shell=true lets the shell read the input directly and allows them to see and run commands without correct authorization
	# "; rm -rf /", it could be ran as another command
	# "; cat /etc/passwd" it could show crucial computer information that an attacker could use

def safe_run(user_input):
	subprocess.run(["echo", user_input])

	# Safer because the input is passed as one argument rather than multiple, and the shell doesnt run commands in the input itself which also helps with security

