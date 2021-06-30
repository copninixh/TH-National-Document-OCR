# TH National Document OCR (THND OCR) 
Tesseract OCR Tools for read Thai National Document using TH Sarabun National Font for training and finetune.
Read README.md to see my step to developing.

Part I : https://github.com/copninich/TH-National-Document-OCR-Part-I

Part II: https://github.com/copninich/TH-National-Document-OCR-Part-II


Medium : https://copninich.medium.com/thnd-ocr-the-series-version-%E0%B8%A1%E0%B9%89%E0%B8%A7%E0%B8%99%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B8%A2%E0%B8%A7%E0%B8%88%E0%B8%9A%E0%B8%9A%E0%B8%9A%E0%B8%9A-%E0%B8%AD%E0%B8%B0%E0%B9%80%E0%B8%AB%E0%B9%89%E0%B8%A2%E0%B8%A2-5a673cc8a686


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


## 03.Testing train and fine tune tesserct (default langdata_lstm)
Requirements langdata_lstm , tesseract 4 , tessdata_best

Load file to your folder and extract : https://drive.google.com/drive/folders/1ABo7ooO62Tb03RR_VvkdshRVG9vz23sl?usp=sharing

## 04.Train and fine tune
Requirements langdata_lstm , tesseract 4 , tessdata_best

Custom tha_training_text with my own dataset more than 60k sentences

Load file to your folder and extract : https://drive.google.com/drive/folders/1ABo7ooO62Tb03RR_VvkdshRVG9vz23sl?usp=sharing

## 05.Performance testing
report_performace_final.csv




