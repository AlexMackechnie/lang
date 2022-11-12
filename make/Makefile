# Makefile
# https://opensource.com/article/18/8/what-how-makefile

# Makefile Format
#
# target: prerequisities
# 	recipe

# By default, `make` assumes a target to be a file itself.
# A target defined here is something you are telling `make` is "always out of date".
# Make interprets all targets as to mean "execute such-and-such recipe to create the file named <target-name>". 
#
# If you have a file named <target-name>, and the prerequisities (targets, again are assumed to be files) are not
# newer than the file <target-name>, then it will just say `make <target-name> is up to date` and do nothing.
.PHONY: all say_hello say_hello_again generate clean

# The first target in the Makefile will be executed with just `make`.
# Unless DEFAULT_GOAL is specified.
say_hello:
	@echo "Hello, World!"

say_hello_again: say_hello
	@echo "Hello, World! Again"

generate:
	@echo "Creating empty text files."
	touch file-{0..3}.txt

clean:
	@echo "Cleaning up files."
	rm *.txt

all: say_hello generate
	
# This overrides the default goal to be generate, so that `generate` is called with just `make`.
# This can only run one target at a time, so typically we have `all` defined here
# and the `all` target then has prerequisities.
.DEFAULT_GOAL := all
