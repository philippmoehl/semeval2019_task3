# Contextual Emotion Detection in Text (FastBert) 
> We use the excellent combination of Huggingface transformers and fast.ai with 


![FastBert.jpg](data/fastbert.jpg)

[SemEval-2019 Task 3](https://www.aclweb.org/anthology/S19-2005.pdf) description: 

"Lack of facial expressions and voice modulations make detecting emotions in text a challenging problem. For instance, as humans, on reading "Why don't you ever text me!" we can either interpret it as a sad or angry emotion and the same ambiguity exists for machines. However, the context of dialogue can prove helpful in detection of the emotion. In this task, given a textual dialogue i.e. an utterance along with two previous turns of context, the goal was to infer the underlying emotion of the utterance by choosing from four emotion classes - Happy, Sad, Angry and Others. To facilitate the participation in this task, textual dialogues from user interaction with a conversational agent were taken and annotated for emotion classes after several data processing steps."

### Install

Setting up the virtual environment first:

`$ pip install virtualenv`

`$ virtualenv venv`

`$ source venv/bin/activate`

`(venv) $ pip install ipykernel`

`(venv) $ ipython kernel install --user --name=projectname`

Then install github repository and requirements:

`$ git clone https://github.com/PhilippMaxx/semeval2019_task3`

`$ cd semeval2019_task3`

`$ pip install requirements.txt`

Then start jupyter notebook:

`$ jupyter notebook`

### How to use

You can run everything inside of the notebooks.

1. For customization work for fast.ai and Bert only open the notebook 00_fastbert.ipynb
2. For the SemEval-2019 Task 3 work open the notebook 01_task3.ipynb

### Documentation
automatically created by nbdev: [Documentation](https://PhilippMaxx.github.io/semeval2019_task3/)

### Notebooks

Jupyter notebooks explaining the customizationand the task:
* 00_fastbert.ipynb
* 01_task3.ipynb
