#
from Parser import Parser
from CodeWriter import CodeWriter
import sys

def main():
	"output file setup"
	filename = sys.argv[1]
	output = CodeWriter( filename )

	"input file setup"
	input = Parser( )
	commandlines = input.commandLines( filename )
	for line in commandlines:
		if input.typeCommand( line ) == 'C_ARITHMETIC':
			output.writeArithmetic( line )
			output.Write()
		elif input.typeCommand( line ) in [ 'C_PUSH', 'C_POP' ]:
			output.writePushPop( line )
			output.Write()
	output.Close()

main()