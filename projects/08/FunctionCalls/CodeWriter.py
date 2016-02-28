#
from Parser import Parser

class CodeWriter():

	def __init__(self, objectfilename, filename):
		""" """
		newfilename = objectfilename+ '.asm'
		self.new_file = open( newfilename, 'a+' )

		self.static_symbol = filename.split('.')[0]

		self.dict = { 'local':'LCL', 'argument':'ARG', 'this':'THIS', 'that':'TAHT' }
		"Initialization of RAM[0] SP segment"

		init_code_sp = '@261\nD=A\n@SP\nM=D\n\n'
		self.new_file.write( init_code_sp )

		"Initialization of RAM[1] LCL segment"

		#init_code_lcl = '@261\nD=A\n@LCL\nM=D\n\n'
		#self.new_file.write( init_code_lcl )

		"Initialization of RAM[2] ARG segment"

		#init_code_arg = '@256\nD=A\n@ARG\nM=D\n\n'
		#self.new_file.write( init_code_arg )

		"Set argument[0] = 1234"
		#init_code_arg_10 = '@1234\nD=A\n@256\nM=D\n\n'
		#self.new_file.write( init_code_arg_10 )
		"Set argument[1] = 37" 
		#init_code_arg_11 = '@1\nD=-A\n@257\nM=D\n\n'
		#self.new_file.write( init_code_arg_11)
		#init_code_arg_12 = '@1\nD=-A\n@258\nM=D\n\n'
		#self.new_file.write( init_code_arg_12)
		#init_code_arg_13 = '@1\nD=-A\n@259\nM=D\n\n'
		#self.new_file.write( init_code_arg_13)
		#init_code_arg_14 = '@1\nD=-A\n@260\nM=D\n\n'
		#self.new_file.write( init_code_arg_14)
		#init_code_arg_15 = '@3010\nD=A\n@315\nM=D\n\n'
		#self.new_file.write( init_code_arg_15)
		#init_code_arg_16 = '@4010\nD=A\n@316\nM=D\n\n'
		#self.new_file.write( init_code_arg_16)

		"Initialization of RAM[3] THIS segment"
		#init_code_this = '@3000\nD=A\n@THIS\nM=D\n\n'
		#self.new_file.write( init_code_this )

		"Initialization of RAM[4] THAT segment"
		#init_code_that = '@4000\nD=A\n@THAT\nM=D\n\n'
		#self.new_file.write( init_code_that )

		self.codeflag1 = 0
		self.codeflag2 = 0

		self.callflag = 0

		#self.func_stack = _ListStack()
		self.label_stack = _ListStack()




	def Write(self):
		self.new_file.write('\n')

	def writeArithmetic(self, commandline):
		""" """
		if( Parser().typeCommand( commandline ) == 'C_ARITHMETIC' ):
			first_field = commandline.split(' ')[0]
			if( first_field == 'add' ):
				""
				asm_code = '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M+D\n@SP\nM=M+1\n'
				self.new_file.write( asm_code )
			elif( first_field == 'sub' ):
				asm_code = '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n'
				self.new_file.write( asm_code )
			elif( first_field == 'neg' ):
				asm_code = '@SP\nM=M-1\nA=M\nD=M\nM=-D\n@SP\nM=M+1\n'
				self.new_file.write( asm_code )
			elif( first_field == 'eq' ):
				asm_code_1 = '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@RET_TRUE' + str(self.codeflag1) + '\nD;JEQ\nD=0\n@CONTINUE' +  str(self.codeflag2) + '\n0;JMP\n(RET_TRUE' + str(self.codeflag1) + ')\nD=-1\n'
				asm_code_2 = '(CONTINUE' + str(self.codeflag2) + ')\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				asm_code = asm_code_1+asm_code_2
				self.new_file.write( asm_code )
				self.codeflag1 += 1
				self.codeflag2 += 1
			elif( first_field == 'lt' ):
				asm_code_1 = '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@RET_TRUE' + str(self.codeflag1) + '\nD;JLT\nD=0\n@CONTINUE' + str(self.codeflag2) + '\n0;JMP\n(RET_TRUE' + str(self.codeflag1) + ')\nD=-1\n'
				asm_code_2 = '(CONTINUE' + str(self.codeflag2) + ')\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				asm_code = asm_code_1+asm_code_2
				self.new_file.write( asm_code )
				self.codeflag1 += 1
				self.codeflag2 += 1
			elif( first_field == 'gt' ):
				asm_code_1 = '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@RET_TRUE' + str(self.codeflag1) + '\nD;JGT\nD=0\n@CONTINUE' + str(self.codeflag2)+ '\n0;JMP\n(RET_TRUE' + str(self.codeflag1) + ')\nD=-1\n'
				asm_code_2 = '(CONTINUE' + str(self.codeflag2) + ')\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				asm_code = asm_code_1+asm_code_2
				self.new_file.write( asm_code )
				self.codeflag1 += 1
				self.codeflag2 += 1
			elif( first_field == 'and' ):
				asm_code = '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D&M\n@SP\nM=M+1\n'
				self.new_file.write( asm_code )
			elif( first_field == 'or' ):
				asm_code = '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D|M\n@SP\nM=M+1\n'
				self.new_file.write( asm_code )
			elif( first_field == 'not' ):
				asm_code = '@SP\nM=M-1\nA=M\nD=M\nM=!D\n@SP\nM=M+1\n'
				self.new_file.write( asm_code )

	def writePushPop(self, commandline):
		""" """
		if( Parser().typeCommand( commandline ) == 'C_PUSH' ):
			if( Parser().arg1( commandline ) == 'constant' ):
				value = Parser().arg2( commandline )
				prefix_code = '@' + value + '\n'
				posix_code = 'D=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				self.new_file.write( prefix_code+posix_code )
			elif( Parser().arg1( commandline ) in [ 'local', 'argument' ] ):
				index = Parser().arg2( commandline )
				prefix_code = '@' + self.dict[ Parser().arg1( commandline ) ] + '\n' + 'D=M\n' + '@' + index + '\n'
				posix_code = 'A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				self.new_file.write( prefix_code+posix_code )
			elif( Parser().arg1( commandline ) == 'temp' ):
				value = int( Parser().arg2( commandline ) ) + 5 
				prefix_code = '@' + str( value ) + '\n'
				posix_code = 'D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				self.new_file.write( prefix_code+posix_code )
			elif( Parser().arg1( commandline ) == 'this' ):
				value = Parser().arg2( commandline )   
				prefix_code = '@THIS\nD=M\n@' + value + '\nA=D+A\n'
				posix_code = 'D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				self.new_file.write( prefix_code+posix_code )
			elif( Parser().arg1( commandline ) == 'that' ):
				value = Parser().arg2( commandline )  
				prefix_code = '@THAT\nD=M\n@' + value + '\nA=D+A\n'
				posix_code = 'D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				self.new_file.write( prefix_code+posix_code )
			elif( Parser().arg1( commandline ) == 'pointer' ):
				p_value = Parser().arg2( commandline )
				if p_value == '0': 
					prefix_code = '@3\n'
					posix_code = 'D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
					self.new_file.write( prefix_code+posix_code )
				elif p_value == '1':
					prefix_code = '@4\n'
					posix_code = 'D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
					self.new_file.write( prefix_code+posix_code )
			elif( Parser().arg1( commandline ) == 'static' ):
				#value = int( Parser().arg2( commandline ) ) + 16
				static_symbol = self.static_symbol + '.' + Parser().arg2( commandline )
				prefix_code = '@' + static_symbol + '\nD=M\n'
				#value = Parser().arg2( commandline ) 
				#posix_code = '@' + value + '\nD=D+A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				posix_code = '@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				self.new_file.write( prefix_code+posix_code )
		elif( Parser().typeCommand( commandline ) == 'C_POP' ):
			if( Parser().arg1( commandline ) in [ 'local', 'argument' ] ):
				prefix_code = '@SP\nM=M-1\nA=M\nD=M\n@' + self.dict[ Parser().arg1( commandline ) ] + '\nA=M\n'
				index = int( Parser().arg2( commandline ) )
				while( index > 0 ):
					prefix_code = prefix_code + 'A=A+1\n'
					index = index - 1
				posix_code = 'M=D\n'
				self.new_file.write( prefix_code+posix_code )
			elif( Parser().arg1( commandline ) == 'temp' ):
				value = int( Parser().arg2( commandline ) ) + 5
				prefix_code = '@SP\nM=M-1\nA=M\nD=M\n@' + str( value ) + '\nM=D\n'
				self.new_file.write( prefix_code )
			elif( Parser().arg1( commandline ) == 'this' ):
				index = int (Parser().arg2( commandline )  )
				prefix_code = '@SP\nM=M-1\nA=M\nD=M\n@THIS\nA=M\n'
				while( index > 0 ):
					prefix_code = prefix_code + 'A=A+1\n'
					index = index - 1
				posix_code = 'M=D\n'
				self.new_file.write( prefix_code+posix_code )
			elif( Parser().arg1( commandline ) == 'that' ):
				index = int (Parser().arg2( commandline )  )
				prefix_code = '@SP\nM=M-1\nA=M\nD=M\n@THAT\nA=M\n'
				while( index > 0 ):
					prefix_code = prefix_code + 'A=A+1\n'
					index = index - 1
				posix_code = 'M=D\n'
				self.new_file.write( prefix_code+posix_code )
			elif( Parser().arg1( commandline ) == 'pointer' ):
				p_value = Parser().arg2( commandline )
				if p_value == '0':
					prefix_code = '@SP\nM=M-1\nA=M\nD=M\n@3\nM=D\n'
					self.new_file.write( prefix_code )
				elif p_value == '1':
					prefix_code = '@SP\nM=M-1\nA=M\nD=M\n@4\nM=D\n'
					self.new_file.write( prefix_code )
			elif( Parser().arg1( commandline ) == 'static' ):
				#value = int( Parser().arg2( commandline ) ) + 16
				static_symbol = self.static_symbol + '.' + Parser().arg2( commandline )
				prefix_code = '@SP\nM=M-1\nA=M\nD=M\n@' + static_symbol + '\n'
				self.new_file.write( prefix_code )
				#index = int( Parser().arg2( commandline ) )
				#count = 0
				#while count < index:
				#	self.new_file.write( 'A=A+1\n' )
				#	count += 1
				self.new_file.write( 'M=D\n')

	def Close(self):
		""" """
		self.new_file.close( )

	#def writeInit(self, commandline):
		"Writes assembly code that effects the VM initialization, also called bootstrap code"
		"SP=256"
		"call Sys.init"
		#if( Parser().typeCommand( commandline ) == 'C_FUNCTION' ):
		#	if( Parser().arg1( commandline ) == 'Sys.init' ):
		#		self.func_stack.push( 'Sys.init' )
		#		prefix_code = '(Sys.init)\n@256\nD=A\n@SP\nM=D\n@SP\nM=M+1\n'
		#		self.new_file.write( prefix_code )

	def writeLabel(self, commandline):
		"Writes assembly code that effects the label command"
		if( Parser().typeCommand( commandline) == 'C_LABEL' ):
			symbol = self.label_stack.peek() + '$' + Parser().arg1( commandline )
			prefix_code = '(' + symbol +')\n'
			self.new_file.write( prefix_code )
		else:
			pass

	def writeGoto(self, commandline):
		"Writes assembly code that effects the goto command"
		if( Parser().typeCommand( commandline ) == 'C_GOTO' ):
			symbol = self.label_stack.peek() + '$' + Parser().arg1( commandline )
			prefix_code = '@' + symbol +'\n0;JMP\n'
			self.new_file.write( prefix_code )
		else:
			pass

	def writeIfGoTo(self, commandline):
		"Writes assembly code that effects the if-goto command"
		if( Parser().typeCommand( commandline ) == 'C_IFGOTO' ):
			symbol= self.label_stack.peek() + '$' + Parser().arg1( commandline )
			prefix_code = '@SP\nM=M-1\nA=M\nD=M\n' + '@' + symbol +'\nD;JNE\n'
			self.new_file.write( prefix_code )
		else:
			pass

	def writeCall(self, commandline):
		"Writes assembly code that effects the call command"
		if( Parser().typeCommand( commandline ) == 'C_CALL' ):
			
			index = int( Parser().arg2( commandline ) )
			#count = 0
			#while count <= index:
			#	prefix_code = '@ARG'+ '\n' + 'D=M\n' + '@' + str( count ) + '\n'
			#	posix_code = 'A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
			#	self.new_file.write( prefix_code + posix_code )
			#	count += 1

			"push return_address"
			#symbol = self.func_stack.peek() + '$return_address' + str( self.callflag )
			symbol = 'return_address$' + str( self.callflag )

			prefix_code = '@' + symbol + '\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
			self.new_file.write( prefix_code )

			"push LCL"
			prefix_code = '@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
			self.new_file.write( prefix_code )

			"push ARG"
			prefix_code = '@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
			self.new_file.write( prefix_code )
			posix_code = 'ARG\nA=M\nM=D\n'

			"push THIS"
			prefix_code = '@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
			self.new_file.write( prefix_code )

			"push THAT"
			prefix_code = '@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
			self.new_file.write( prefix_code )

			"ARG = SP-n-5"
			n = index
			prefix_code = '@SP\nD=M\n@5\nD=D-A\n'
			self.new_file.write( prefix_code )
			self.new_file.write( '@' + str(n) + '\nD=D-A\n' )
			posix_code = '@ARG\nM=D\n'
			self.new_file.write( posix_code )

			"LCL = SP"
			prefix_code = '@SP\nD=M\n@LCL\nM=D\n'
			self.new_file.write( prefix_code )

			"goto f"
			func_nam = Parser().arg1( commandline )
			prefix_code = '@' + func_nam +'\n0;JMP\n'
			self.new_file.write( prefix_code )

			"(return-address)"
			#symbol = self.func_stack.peek() + '$return_address'  + str( self.callflag )
			symbol = 'return_address$' + str( self.callflag )
			prefix_code = '(' + symbol + ')\n'
			self.new_file.write( prefix_code )

			self.callflag += 1

	def writeReturn(self, commandline):
		"Writes assembly code that effects the return command"
		if Parser().typeCommand( commandline ) == 'C_RETURN':
			"FRAME = LCL"
			asm_code_1 = '@LCL\nD=M\n@R13\nM=D\n'
			self.new_file.write( asm_code_1 )
			"RET = *(FRAME - 5)"
			asm_code_2 = '@5\nD=D-A\nA=D\nD=M\n@R14\nM=D\n'
			self.new_file.write( asm_code_2 )
			"*ARG = pop()"
			asm_code_3 = '@SP\nM=M-1\n@SP\nA=M\nD=M\n@ARG\nA=M\nM=D\n'
			self.new_file.write( asm_code_3 )
			"SP = ARG + 1"
			asm_code_4 = '@ARG\nD=M\n@SP\nM=D+1\n'
			self.new_file.write( asm_code_4 )
			"THAT = *(FRAME - 1)"
			asm_code_5 = '@R13\nD=M\nD=D-1\nA=D\nD=M\n@THAT\nM=D\n'
			self.new_file.write( asm_code_5)
			"THIS = *(FRAME - 2)"
			asm_code_6 = '@R13\nD=M\nD=D-1\nD=D-1\nA=D\nD=M\n@THIS\nM=D\n'
			self.new_file.write( asm_code_6 )
			"ARG = *(FRAME - 3)"
			asm_code_7 = '@R13\nD=M\nD=D-1\nD=D-1\nD=D-1\nA=D\nD=M\n@ARG\nM=D\n'
			self.new_file.write( asm_code_7 )
			"LCL = *(FRAME - 4)"
			asm_code_8 = '@R13\nD=M\nD=D-1\nD=D-1\nD=D-1\nD=D-1\nA=D\nD=M\n@LCL\nM=D\n'
			self.new_file.write( asm_code_8)
			"goto RET, return address"
			prefix_code = '@R14\nA=M\n0;JMP\n'
			self.new_file.write( prefix_code )
			#self.func_stack.pop()
		else:
			pass
			

	def writeFunction(self, commandline):
		"Writes assembly code that effects the function command"
		if( Parser().typeCommand( commandline ) == 'C_FUNCTION' ):

			"Function label: ( function_name )"
			func_nam = Parser().arg1( commandline ) 
			#self.func_stack.push( func_nam )
			self.label_stack.push( func_nam )
			label = '(' + self.label_stack.peek() + ')\n'
			self.new_file.write( label )

			"repeat k times"
			k = int ( Parser().arg2( commandline ) )  
			for element in range( k ):
				prefix_code = '@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
				self.new_file.write( prefix_code )
				local_index = element + 1
				posix_code = '@SP\nM=M-1\nA=M\nD=M\n@LCL\nA=M\n'
				self.new_file.write( posix_code )
				while local_index  > 0:			
					self.new_file.write( 'A=A+1\n' )	
					local_index = local_index - 1
				self.new_file.write ( 'M=D\n' )
		else:
			pass




# Implementation of the stack ADT using a regular list
class _ListStack:

	"Returns an instance of class _ListStack "
	def __init__(self):
		self._item = list( )

	def isEmpty(self):
		return len( self ) == 0

	def __len__(self):
		return len( self._item )

	def peek(self):
		if self.isEmpty():
			return 'Null'
		else:
			return self._item[-1]

	def pop(self):
		if self.isEmpty():
			return 'Null'
		else:
			return self._item.pop( )

	def push(self, item):
		self._item.append( item )



