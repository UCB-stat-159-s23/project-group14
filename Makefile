## Makefile to create environment, run all notebooks, create jupyter book, and clean up 

.ONESHELL:
SHELL = /bin/bash

## create_environment : creates an environment
.PHONY : envs
envs : 
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml
	conda activate projenv
	conda install ipykernel
	python -m ipykernel install --user --name projenv --display-name "IPython - projenv"


## all : runs all notebooks
.PHONY : all
all:
	jupyter run sales-of-cigarette-each-state.ipynb
	jupyter run MapPlot.ipynb
	jupyter run LinearRegression.ipynb
	jupyter run main.ipynb


## build : builds jupyter book
.PHONY : html
html:
	jb build .
	
	
## clean : removes outputs, figures, and _build directories

.PHONY : clean
clean :
	rm -r _build/*
	rm -f output/*