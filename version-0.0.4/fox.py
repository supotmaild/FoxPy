class fox:

	global f, field, file_start, p, procs
	global s_multi, s_timer, s_timer_time
	f = open('fox_samp.dbf', 'r+')
	from multiprocessing import Process
	p = Process()
	kind = 'canine'
	procs = []
	s_multi = True
	s_timer = False
	s_timer_time = 0.00

	def p_E_clear(self):
		import os
		os.system('cls')
		print('>>> ', end='')
		return None
	def p_W_use(self, file_name):
		import io
		global f,field,file_start
		f.close()
		f = open(file_name, 'rb+')
		raw = f.read(32)
		file_start = 32
		ff = chr(20)
		field = []
		space = '          '
		while ff != chr(13):
			field_name = ''.join(map(chr,f.read(11)))
			if ord(field_name[0]) == 13: break
			for i in range(len(field_name)):
				if field_name[i]==chr(0):
					field_name = field_name[0:i]+space[0:len(field_name)-i]
					break
			field.append(field_name)
			field_type = ''.join(map(chr,f.read(1)))
			field.append(field_type)
			other = f.read(4)
			oline = f.read(16)
			file_start = file_start + 32
			field_long = int(oline[0])
			field.append(field_long)
			field_decimal = int(oline[1])
			field.append(field_decimal)
			#print(field_name,end='')
			#print(field_type,end='')
			#print(' ',end='')
			#if field_type=='N':
			#	print(field_long,end='')
			#	print(',',end='')
			#	print(field_decimal)
			#else:
			#	print(field_long)
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
		global f , field, file_start
		space = ''
		for i in range(32):
			space = space+'        '
		f.seek(4)
		rec = f.read(4)
		recno = rec[0]+(rec[1]*256)+(rec[2]*256*256)+(rec[3]*256*256*256)
		f.seek(file_start+1)
		print(' RECNO ')
		for i in range(int(len(field)/4)):
			print(field[(i*4)],end='')
			print(' ',end='')
			if len(field[(i*4)])<field[(i*4)+2]:
				print(space[0:field[(i*4)+2]-len(field[(i*4)])],end='')
				print(' ',end='')
		print('')
		for j in range(recno):
			delete = ''.join(map(chr,f.read(1)))
			print(delete,end='')
			print(str(j+1).zfill(5),end='')
			print(' ',end='')
			for i in range(int(len(field)/4)):
				if len(field[(i*4)])>field[(i*4)+2]:
					print(space[0:len(field[(i*4)])-field[(i*4)+2]],end='')
				if field[(i*4)+1] == 'N' and field[(i*4)+3] > 0:
					field_long = field[(i*4)+2]+1+field[(i*4)+3]
				else:
					field_long = field[(i*4)+2]
				print(''.join(map(chr,f.read(field_long))),end='')
				print(' ',end='')
			print('')
		return None
	def list_struc(self):
		global field
		for i in range(int(len(field)/4)):
			print(field[(i*4)],end='')
			print(' ',end='')
			print(field[(i*4)+1],end='')
			print(' ',end='')
			if field[(i*4)+1]=='N':
				print(field[(i*4)+2],end='')
				print(',',end='')
				print(field[(i*4)+3])
			else:
				print(field[(i*4)+2])
	def modify_command(self, file_name):
		import tkinter as tk
		from tkinter import Menu
		from tkinter import messagebox
		import tkinter.scrolledtext as tkst
		import os.path
		if os.path.isfile(file_name):
			file = open(file_name, 'r')
			read_text = file.readlines()
			file_text = ''
			for line in read_text:
				file_text = file_text + line
			file.close()
		else:
			file_text = ''
		win = tk.Tk()
		win.title(file_name)
		frame1 = tk.Frame(
			master = win,
			bg = '#808000'
		)
		global editArea
		editArea = tkst.ScrolledText(
			master = frame1,
			wrap = tk.WORD,
			width = 20,
			height = 10
		)
		def save_command():
			global editArea
			file = open(file_name, 'w')
			data = editArea.get('1.0', 'end-1c')
			file.write(data)
			file.close()
		def not_save_exit_command():
			if messagebox.askokcancel("Quit", "(Not Save) Do you really want to quit?"):
				win.destroy()			
		def exit_command():
			global editArea
			file = open(file_name, 'w')
			data = editArea.get('1.0', 'end-1c')
			file.write(data)
			file.close()
			if messagebox.askokcancel("Quit", "Do you really want to quit?"):
				win.destroy()
		frame1.pack(fill='both', expand='yes')
		menu = Menu(win)
		win.config(menu=menu)
		filemenu = Menu(menu)
		menu.add_cascade(label='File', menu=filemenu)
		filemenu.add_command(label='Save', command=save_command)
		filemenu.add_command(label='Not Save and Exit', command=not_save_exit_command)
		filemenu.add_separator()
		filemenu.add_command(label='Save and Exit', command=exit_command)
		editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
		editArea.insert(tk.INSERT, file_text)
		win.mainloop()
	def modi_comm(self, file_name):
		self.modify_command(file_name)
	def q(self, text):
		print(text)
		return None
	def do(self, file_name):
		import time
		import os.path
		if os.path.isfile(file_name):
			file = open(file_name, 'r')
			program_text = file.readlines()
			file.close()
		else:
			print('No file')
			return None
		self.set_timer_off()
		exec('x=fox()')
		j = ''
		for i in program_text:
			if type(i) is str:
				j = j + i + '\n'
		if (j != ''):
			exec(j + '\n')
			j = ''
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
