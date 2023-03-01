PROGRAM_NAME=demo

.PHONY: all run clean

all: $(PROGRAM_NAME)

%: %.c 
	gcc -Wall -Wextra -g $^ -o $@ -l hiredis

run: all 
	./$(PROGRAM_NAME)

clean: 
	rm -rf $(PROGRAM_NAME)