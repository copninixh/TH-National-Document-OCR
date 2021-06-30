# TH National Document OCR (THND OCR) Main Repo
Tesseract OCR Tools for read Thai National Document using TH Sarabun National Font for training and finetune.
Read README.md and follow to part I and II to see my step to developing.

Part I : https://github.com/copninich/TH-National-Document-OCR-Part-I
Part II : https://github.com/copninich/TH-National-Document-OCR-Part-II

## 0. Information
### 0.1 Tools 
- Tesseact : https://github.com/tesseract-ocr/tesseract
### 0.2 Dataset
- PyThaiNLP (Prachathai) : https://github.com/PyThaiNLP/prachathai-67k
- PyThaiNLP (ThaiGov V2 Corpus) : https://github.com/PyThaiNLP/thaigov-v2-corpus
- PyThaiNLP (ThaiGov Archive corpus) : https://github.com/PyThaiNLP/thaigov-archive-corpus
- Thaisum : https://github.com/nakhunchumpolsathien/ThaiSum 
- TR-TPBS : https://github.com/nakhunchumpolsathien/TR-TPBS
### 0.3 Project information
- Ai Builders
- Kampanart Chaimooltan

## 01.Performance testing 
Using Character Errorate and leght string (OCR & Correct Text) and output result testing (.csv file)

## 02.Generate dataset
Using PIL library and using TH Sarabun formart font 72 px to create dataset.

## 03.Calculate error rate (Manual)
Using Character Errorate and leght string (OCR & Correct Text)

## 04.Testing train and fine tune tesserct (default langdata_lstm)
Requirements langdata_lstm , tesseract , tessdata_best , 

## 05.Train and fine tune
Custom tha_training_text with my own dataset more than 1 million sentences

## 06.My model
Coming soon

## 07.Website for testing
Coming soon


