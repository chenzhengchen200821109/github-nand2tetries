#
from Parser import Parser
from CodeWriter import CodeWriter
import sys

def main():
	"output file setup"
	arg_length = len( sys.argv ) - 2
	if arg_length == 0:
		objectFileName = sys.argv[1].split('.')[0]
		filename = sys.argv[1]
		output = CodeWriter(objectFileName, filename)
		input = Parser( )
		commandlines = input.commandLines( filename )
		for line in commandlines:
			if input.typeCommand( line ) == 'C_ARITHMETIC':
				output.writeArithmetic( line )
				output.Write()
			elif input.typeCommand( line ) in [ 'C_PUSH', 'C_POP' ]:
				output.writePushPop( line )
				output.Write()
			elif input.typeCommand( line ) == 'C_LABEL':
				output.writeLabel( line )
				output.Write()
			elif input.typeCommand( line ) == 'C_GOTO':
				output.writeGoto( line )
				output.Write()
			elif input.typeCommand( line ) == 'C_IFGOTO':
				output.writeIfGoTo( line )
				output.Write()
			elif input.typeCommand( line ) == 'C_FUNCTION':
				#output.writeInit( line )
				output.writeFunction( line )
				output.Write()
			elif input.typeCommand( line ) == 'C_RETURN':
				output.writeReturn( line )
				output.Write()
			elif input.typeCommand( line ) == 'C_CALL':
				output.writeCall( line )
				output.Write()
	else:
		count = 0
		objectFileName = sys.argv[-1]
		while count < arg_length:
			"input file setup"
			filename = sys.argv[ count + 1 ]
			output = CodeWriter(objectFileName, filename)
			input = Parser( )
			commandlines = input.commandLines( filename )
			for line in commandlines:
				if input.typeCommand( line ) == 'C_ARITHMETIC':
					output.writeArithmetic( line )
					output.Write()
				elif input.typeCommand( line ) in [ 'C_PUSH', 'C_POP' ]:
					output.writePushPop( line )
					output.Write()
				elif input.typeCommand( line ) == 'C_LABEL':
					output.writeLabel( line )
					output.Write()
				elif input.typeCommand( line ) == 'C_GOTO':
					output.writeGoto( line )
					output.Write()
				elif input.typeCommand( line ) == 'C_IFGOTO':
					output.writeIfGoTo( line )
					output.Write()
				elif input.typeCommand( line ) == 'C_FUNCTION':
					#output.writeInit( line )
					output.writeFunction( line )
					output.Write()
				elif input.typeCommand( line ) == 'C_RETURN':
					output.writeReturn( line )
					output.Write()
				elif input.typeCommand( line ) == 'C_CALL':
					output.writeCall( line )
					output.Write()
			count += 1

	output.Close()

main()