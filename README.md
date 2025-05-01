# Patristics on Natural Language Processing - Exploring *I Clement* with spaCy and odyCy


## Overview and Purpose

This notebook is an exploration of how to apply Natural Language Processing (NLP) pipelines in order to analyse the Ancient-Greek text of the First Epistle of Clement (Κλήμεντος πρὸς Κορινθίους), and find what's hard to find.

To orchestrate NLP pipelines to Ancient-Greek texts, we use [OdyCy](https://centre-for-humanities-computing.github.io/odyCy/), a Natural Language Processing library in Python for Ancient Greek, capable of part-of-speech tagging, morphological analysis, dependency parsing, lemmatization, and more.  It is based on the popular [spaCy](https://spacy.io/) framework, which makes odyCy easy to use, scalable, reliable, and modular.

## Show me what you've found

=> [1 Clement counts 150 unique Ancient-Greek verbs.](https://github.com/ronanguilloux/I-Clement-on-spacy/blob/main/1-Clement-Verbs.ipynb)

## The Material in use

For this analysis, we used the [original Greek text of Clement I](https://ccel.org/ccel/lake/fathers2/fathers2.ii.i.html).
The `data` folder contains an excerpt and the full version as well.  

## The NLP pipelines available

Just like any other spaCy pipeline, odyCy is a modular set of components run in succession. The different components add different attributes to tokens or spans, which will constitute the output document object.

[Learn more about odyCy/spaCY pipeline architecture here](https://centre-for-humanities-computing.github.io/odyCy/architecture.html)

## How to get started

1. clone repository with:
```bash
git clone https://github.com/ronanguilloux/Patristics-I-Clement-on-spacy.git
```
2. Install dependencies with:
```bash
pip install -r requirements.txt
```
3. Run the jupyter notebook
```bash
jupyter notebook
````

On macOS it'll open your browser and serve Jupyter locally on your machine, at http://localhost:8888.

## Notebook Usage

JupyterLab is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning.

[Learn more about Jupyter here](https://jupyter.org/)

## Example Output

See below for an example image output for the Tokens dependency parse visualization.

![displaCy-output](./displaCy-output.png "Tokens dependency parse visualization")
