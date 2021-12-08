SHELL := /bin/bash 

build: 
	pdflatex -shell-escape presentation.tex
clean:
	mkdir ../tmp
	mv presentation.tex ../tmp
	mv Makefile ../tmp
	mv images/ ../tmp
	rm -r *
	mv ../tmp/Makefile .
	mv ../tmp/presentation.tex .
	mv ../tmp/images/ .
	rm -r ../tmp