#! /usr/bin/python

from Code import Code
from Parser import Parser
from Parser import ParserComd
from SymbolTable import SymbolTable
import sys

def main():
	"output file is the file where output will be written to"
	filename = sys.argv[1].split('.')[0]
	outputfile = open( filename + ".hack", "a" )

	"input file is the file where input will come from"
	inputfile = Parser( sys.argv[1] )

	lines = inputfile.commandLines()

	for line in lines:
		if( ParserComd( line ).commandType() == 'A_command' ):
			symbol_line = ParserComd( line ).symbol( )
			symbol_a = SymbolTable( )
			symbol_a.addEntry( symbol_line )
			f = symbol_a.GetAddress( symbol_line )
			outputfile.write( f )
			outputfile.write( '\n' )

		elif( ParserComd( line ).commandType() == 'C_command_a' or ParserComd( line ).commandType() == 'C_command_b'):
			dest_line = ParserComd( line ).dest()
			comp_line = ParserComd( line ).comp()
			jump_line = ParserComd( line ).jump()
			cbinary = Code( dest_line, comp_line, jump_line ).cinstruction()
			outputfile.write( cbinary )
			outputfile.write( '\n' )
		elif( ParserComd( line ).commandType() == 'L_command' ):
			outputfile.write( 'This line is going to delete\n' )

	outputfile.close()

main()