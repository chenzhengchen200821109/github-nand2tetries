#
from Parser import Parser

class CodeWriter():

	def __init__(self, filename):
		""" """
		newfilename = filename.split('.')[0] + '.asm'
		self.new_file = open( newfilename, 'w' )
		self.dict = { 'local':'LCL', 'argument':'ARG', 'this':'THIS', 'that':'TAHT' }
		"Initialization of RAM[0] SP segment"
		init_code_sp = '@256\nD=A\n@SP\nM=D\n\n'
		self.new_file.write( init_code_sp )

		"Initialization of RAM[1] LCL segment"
		init_code_lcl = '@300\nD=A\n@LCL\nM=D\n\n'
		self.new_file.write( init_code_lcl )

		"Initialization of RAM[2] ARG segment"
		init_code_arg = '@400\nD=A\n@ARG\nM=D\n\n'
		self.new_file.write( init_code_arg )

		"Initialization of RAM[3] THIS segment"
		init_code_this = '@3000\nD=A\n@THIS\nM=D\n\n'
		self.new_file.write( init_code_this )

		"Initialization of RAM[4] THAT segment"
		init_code_that = '@3010\nD=A\n@THAT\nM=D\n\n'
		self.new_file.write( init_code_that )

		self.codeflag1 = 0
		self.codeflag2 = 0

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
				value = int( Parser().arg2( commandline ) ) + 16 
				prefix_code = '@' + str( value ) + '\n'
				posix_code = 'D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
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
				value = int( Parser().arg2( commandline ) ) + 16
				prefix_code = '@SP\nM=M-1\nA=M\nD=M\n@' + str( value ) + '\nM=D\n'
				self.new_file.write( prefix_code )

	def Close(self):
		""" """
		self.new_file.close( )



