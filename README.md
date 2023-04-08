# NoHarm Gehn - a Language Model for Portuguese Electronic Health Notes generation

## Introduction

The NoHarm Gehn model (Generative Electronic Health Notes) was trained using Transfer Learning and Fine-tuning techniques on the GPT NeoX 20B model with 46GB of training data in Portuguese (corresponding to 38 million clinical notes from 70 hospitals). The model is able to receive instructions based on other clinical notes and generate contextualized discharge summaries for each patient.

This repositority shows how to train GPT2-Bio-PT with Brateca v1.1, a open source subset of 2.8 million NoHarm's clinical notes.

## GPT-2 

*Note: information copied/pasted from [Model: gpt2 >> GPT-2](https://huggingface.co/gpt2#gpt-2)*

Pretrained model on English language using a causal language modeling (CLM) objective. It was introduced in this [paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) and first released at this [page](https://openai.com/blog/better-language-models/) (February 14, 2019).

## Model description

*Note: information copied/pasted from [Model: gpt2 >> Model description](https://huggingface.co/gpt2#model-description)*

GPT-2 is a transformers model pretrained on a very large corpus of English data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely, it was trained to guess the next word in sentences.

More precisely, inputs are sequences of continuous text of a certain length and the targets are the same sequence, shifted one token (word or piece of word) to the right. The model uses internally a mask-mechanism to make sure the predictions for the token `i` only uses the inputs from `1` to `i` but not the future tokens.

This way, the model learns an inner representation of the English language that can then be used to extract features useful for downstream tasks. The model is best at what it was pretrained for however, which is generating texts from a prompt.
