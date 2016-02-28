#

class Parser():

	def __init__(self):
		""" """
		self.lines = None
		self.commandlist = list()

	def commandLines(self, filename):
		""" """
		file_obj = open( filename, "r" )
		self.lines = file_obj.readlines()

		for line in self.lines:
			element = line.rstrip('\n').lstrip().split('//')[0]
			element_m = element.split('\r')[0]
			if element_m == '':
				pass
			else:
				self.commandlist.append( element_m )
		return self.commandlist

	def typeCommand(self, commandline):
		""" """
		first_field = commandline.split(' ')[0]
		""" """
		if first_field in [ 'add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not' ]:
			return 'C_ARITHMETIC'
		elif( first_field == 'push' ):
			return 'C_PUSH'
		elif( first_field == 'pop' ):
			return 'C_POP'
		elif( first_field == 'label' ):
			return 'C_LABEL'
		elif( first_field == 'goto' ):
			return 'C_GOTO'
		elif( first_field == 'if-goto' ):
			return 'C_IFGOTO'
		elif( first_field == 'function' ):
			return 'C_FUNCTION'
		elif( first_field == 'return' ):
			return 'C_RETURN'
		elif( first_field == 'call' ):
			return 'C_CALL'
		else:
			return False
		

	def arg1(self, commandline ):
		""" """
		try:
			argument1 = commandline.split(' ')[1]
 			return argument1
 		except IndexError:
 			pass

	def arg2( self, commandline ):
		""" """
		try:
			argument2 = commandline.split(' ')[2]
			return argument2
		except IndexError:
			pass


