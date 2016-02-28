# Reads an assembly language command, parser it, and provides convenient access to the command's
# components.

class Parser():

	def __init__(self, argv):
		""" Opens the input file/stream and gets ready to parser it """
		self.file = open(argv, "r")
		self.currentcommand = None
		self.lines = self.file.readlines()
		self.commandlist = list()

	def hasMoreCommands(self):
		""" Are there more commands in the input """
		self.currentcommand = self.file.readline().rstrip('\n')
		if( self.currentcommand == " " ):
			return False
		else:
			return True

	def advance(self):
		if( self.hasMoreCommands() == True):
			return self.currentcommand
		else:
			return ''

	def commandLines(self):
		for line in self.lines:
			element = line.rstrip('\n').lstrip().rstrip('\r').split(' ')[0]
			self.commandlist.append( element )
		return self.commandlist



class ParserComd():

	def __init__(self, command):
		self.command = command

	def commandType(self):
		""" Returns the type of the current command """
		command_field = list( self.command )
		if '@' in command_field:
			return 'A_command'
		elif '=' in command_field:
			return 'C_command_a'
		elif ';' in command_field:
			return 'C_command_b'
		elif '(' in command_field and ')' in command_field:
			return 'L_command'
		else:
			return 'L_command'

	def symbol(self):
		""" Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). """
		if( self.commandType( ) == 'A_command' ):
			return self.command.split( '@' )[1]
		elif( self.commandType( self.command ) == 'L_command' ):
			return ''

	def dest(self):
		""" Returns the dest nmemonic in the current C_command_a. """
		if( self.commandType( ) == 'C_command_a' ):
			return self.command.split('=')[0]
		else:
			return ''

	def comp(self):
		""" Returns the comp nmemonic in the current C_command_b. """
		if( self.commandType( ) == 'C_command_b' ):
			return self.command.split(';')[0]
		elif( self.commandType( ) == 'C_command_a' ):
			return self.command.split('=')[1]
		else:
			return ''

	def jump(self):
		""" Returns the jump nmemonic in the current C_command. """
		if( self.commandType( ) == 'C_command_b' ):
			return self.command.split(';')[1]
		else:
			return ''








