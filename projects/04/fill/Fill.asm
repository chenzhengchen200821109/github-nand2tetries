// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.
(LOOP)
	@KBD
	D=M
	@WHITE
	D;JEQ
	@BLACK
	D;JNE
	@LOOP
	0;JMP
	@i
	M=0

(WHITE)
	@i
	D=M
	@SCREEN
	D=D+A        // D=i+16384
	@24575
	D=D-A
	@LOOP
	D;JGT
	@i
	D=M          // D=i
	@SCREEN
	A=D+A
	M=0
	@i
	M=M+1    // i=i+1
	@WHITE
	0;JMP

(BLACK)
	@i
	D=M
	@SCREEN
	D=D+A        // D=i+16384
	@24575
	D=D-A
	@LOOP
	D;JGT
	@i
	D=M          // D=i
	@SCREEN
	A=D+A
	M=1
	@i
	M=M+1    // i=i+1
	@BLACK
	0;JMP
