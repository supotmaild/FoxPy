class fox:

	global f, line_num, p, procs, program_text 
	global s_multi, s_timer, s_timer_time
	f = open('fox_samp.dbf', 'r+')
	from multiprocessing import Process
	p = Process()
	kind = 'canine'
	line_num = 10
	procs = []
	program_text = []
	program_text.append(0)
	s_multi = True
	s_timer = False
	s_timer_time = 0.00
	def p_E_clear(self):
		import os
		os.system('cls')
		print('>>> ', end='')
		return None
	def p_W_use(self, file_name):
		global f
		f.close()
		f = open(file_name, 'r+')
		return None


	def __init__(self):
		return None
	def clear(self):
		from multiprocessing import Process
		p = Process(target=self.p_E_clear)
		procs.append(p)
		p.start()
		return None
	def list(self):
		global f
		print(f.read())
		return None
	def q(self, text):
		print(text)
		return None
	def run(self):
		import time
		self.set_timer_off()
		exec('x=fox()')
		j = ''
		for i in program_text:
			if type(i) is str:
				if i[-1] == ':':
					j = j + i
				elif (i[0] == ' ') or (ord(i[0]) == 9):
					j = j + i + ';'
				else:
					exec(j)
					j = ''
					exec(i)
		if s_timer:
			print('FoxPy Run Time ' + str(round(time.time()-s_timer_time,2)) + 'seconds')		
	def set_multi(self):
		global s_multi
		return s_multi
	def set_multi_off(self):
		global s_multi
		s_multi = False
		return None
	def set_multi_on(self):
		global s_multi
		s_multi = True
		return None
	def set_timer(self):
		global s_timer
		return s_timer
	def set_timer_off(self):
		global s_timer
		s_timer = False
		s_timer_time = 0.00
		return None
	def set_timer_on(self):
		import time
		global s_timer,s_timer_time
		s_timer = True
		s_timer_time = time.time()
		return None
	def use(self, file_name):
		from multiprocessing import Process
		p = Process(target=self.p_W_use(file_name))
		procs.append(p)
		p.start()
		return None
	def timer_time(self):
		import time
		global s_timer_time
		return time.time() - s_timer_time
	def zombie(self):
		global procs
		for p in procs:
			print('*', end='')
			p.join()
		procs = []
		print('')
		return None
