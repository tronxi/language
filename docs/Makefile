SHELL := /bin/bash 

build: 
	pdflatex -shell-escape presentation.tex
clean:
	mkdir ../tmp
	mv presentation.tex ../tmp
	mv Makefile ../tmp
	rm -r *
	mv ../tmp/Makefile .
	mv ../tmp/presentation.tex .
	rm -r ../tmp