class fox:

	global f 
	f = open('MDisc.log', 'r+')
	kind = 'canine'

	def __init__(self):
		return None
	def q(self, text):
		print(text)
		return None
	def use(self, file_name):
		global f
		f.close()
		f = open(file_name, 'r+')
		return None
	def list(self):
		global f
		print(f.read())
		return None
