## Makefile to create environment, build JupyterBook, and clean for this repository 

.ONESHELL:
SHELL = /bin/bash

## create_environment : creates an environment
.PHONY : envs
envs : 
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml
	conda activate projenv
	conda install ipykernel
	python -m ipykernel install --user --name maketobacco --display-name "IPython - projenv"


## html : builds jupyterbook
.PHONY : html
html:
	jb build .

## clean : removes output and _build directories
.PHONY : clean
clean : 
	rm -f output/*
	rm -r _build/*