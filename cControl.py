import sys, time

def lWheel(repeats):
	for i in range (0,repeats):
		# chars to use for loading animation
		for r in ['/', '-', '\\', '|']:
			# /r is a carriage return, go back to the line start for overwriting
			print("loading... " + r, end="\r")
			time.sleep(1)
	# clear the line after all done, to not leave finished wheel there
	print("\u001b[0K", end="")

def textReplace():
	for i in ["test", "hello", "3", "something long, really long", "5"]:

		sys.stdout.write("\u001b[1000D") # move all the way left
		sys.stdout.write("\u001b[0K")    # clear the line
		sys.stdout.write(i)

		# Flush the output buffer, stdout doesn't do it automatically like the print statement does.
		# Flushing exists to improve performance; writing to file is computationally expensive, so
		# instead of writing to file for every character, store characters in a buffer in memory and
		# write them as 1 large block instead. Takes less time overall than doing it for every character.
		# Flushing doesn't mean to delete, it means to transfer data from buffer to file, which in this
		# case means transferring the buffer text to the screen. Without flushing buffer manually for
		# stdout, nothing will appear on the screen, as the text is still filling the buffer instead.
		sys.stdout.flush()
		# sleep just so it's easier to see the code working, has no effect on operation
		time.sleep(1)

		# move cursor to the left and flush buffer, so when the program ends the terminal text can start
		# from the beginning of the line and overwrite the last output. Without this part, the terminal
		# will append its text to the end of the last output which may look messy.
		sys.stdout.write("\u001b[1000D")

def paraReplace_stdout():
	# outputting text and moving cursor back so everything after the cursor will be deleted
	sys.stdout.write("Some text after this will be deleted:")
	sys.stdout.write("\n#####\n#####\n#####\n#####\n#####\n")
	sys.stdout.flush()
	time.sleep(1)
	sys.stdout.write("\u001b[5F") # move cursor to beginning of 5 lines up
	sys.stdout.flush()
	time.sleep(1)
	sys.stdout.write("\u001b[0J") # clear everything after the cursor
	sys.stdout.flush()

def paraReplace_print():
	# using print statements that automatically flush buffer for us
	time.sleep(1)
	print("Some text after this will also be deleted:"+
		"\n#####\n#####\n#####\n#####\n#####", end="")
	time.sleep(1)
	print("\u001b[5F") # move cursor to beginning of 5 lines up
	time.sleep(1)
	print("\u001b[0J") # clear everything after the cursor

lWheel(3)
textReplace()
paraReplace_stdout()
paraReplace_print()