def commit():
	message = raw_input("enter a git commit message: ")
	local('git add . && git comit -am "{}"'.format(message))

def push():
	local("git push origin master")

def prepare():
	commit()
	push()