#include <stdio.h>
#include <unistd.h>

void lWheel(int repeats){
	// chars to use for loading animation
	const char lChars[] = {'/', '-', '\\', '|'};
	int numRepeats = repeats;
	for(int i=0; i<numRepeats; i++){
		for(int j=0; j<4; j++){
			printf("Loading... %c\r", lChars[j]);
			// flush the output buffer. printf usually does this automatically, but
			// without declaring it manually, it will not be completed before the sleep
			// is started, meaning nothing will be printed to the screen.
			fflush(stdout); 
			// sleep so we can admire the characters on screen
			sleep(1);
		}
	}
}

void textReplace(){
	// store an array of strings by instead creating an array of pointers that point to
	// different char arrays (strings)
	const char *words[5];
	words[0] = "test";
	words[1] = "hello";
	words[2] = "3";
	words[3] = "something long, really long";
	words[4] = "5";

	for(int i=0; i<5; i++){
		// move cursor to the left (start of line) and clear the line so it can be
		// cleanly overwritten by the next output
		printf("\033[1000D\033[0K%s", words[i]);
		// manually flush the output buffer to ensure text is shown; the sleep
		// statement can interfere with printf's automatic buffer flush
		fflush(stdout);
		sleep(1);
		// move cursor to the left, so the next output fully overwrites line
		printf("\033[1000D");
	}
}

void paraReplace(){
	printf("Some text after this will be deleted:\n#####\n#####\n#####\n#####\n#####\n");
	// manually flush the output buffer to ensure text is shown; the sleep
	// statement can interfere with printf's automatic buffer flush
	fflush(stdout);
	sleep(1);
	// move cursor to the beginning of the line that is 5 lines up
	printf("\033[5F");
	fflush(stdout);
	sleep(1);
	// clear everything after the cursor position
	printf("\033[0J");
	fflush(stdout);
	sleep(1);
}

int main(){
	lWheel(3);
	textReplace();
	paraReplace();
	paraReplace();
}