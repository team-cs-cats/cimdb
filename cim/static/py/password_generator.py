import random, string

def new_password(size=8):

	chars = string.ascii_letters + string.digits + string.punctuation

	password = []

	[password.append(random.choice(chars)) for char in range(size)]

	return ''.join(password)


if __name__ == '__main__':

	print(new_password())
