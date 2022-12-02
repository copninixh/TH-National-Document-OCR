# Thai National Document Optical Character Recognition (THND OCR) 
[![DOI](https://zenodo.org/badge/379371970.svg)](https://zenodo.org/badge/latestdoi/379371970)

#### Tesseract OCR tools for read Thai National Document used TH Sarabun National Font trained and finetuned. Read README.md to see about my process.

- Part I : https://github.com/copninich/TH-National-Document-OCR-Part-I

- Part II : https://github.com/copninich/TH-National-Document-OCR-Part-II

- Medium : https://medium.com/@copninich/5a673cc8a686


## 0. Informations
### 0.1 Tool
- Tesseact : https://github.com/tesseract-ocr/tesseract
### 0.2 Datasets
- PyThaiNLP (Prachathai) : https://github.com/PyThaiNLP/prachathai-67k
- PyThaiNLP (ThaiGov V2 Corpus) : https://github.com/PyThaiNLP/thaigov-v2-corpus
- PyThaiNLP (ThaiGov Archive corpus) : https://github.com/PyThaiNLP/thaigov-archive-corpus
- Thaisum : https://github.com/nakhunchumpolsathien/ThaiSum 
- TR-TPBS : https://github.com/nakhunchumpolsathien/TR-TPBS
### 0.3 Project informations
- Ai Builders
- Kampanart Chaimooltan

## 01.Performance testing 
Using Character Errorate and leght string (OCR & Correct Text) and output result testing (.csv file)

## 02.Generate dataset
Using PIL library and using TH Sarabun formart font 72 px to create dataset.

Link : https://www.kaggle.com/copninich/thaienglish-character-in-th-sarabun-font

## 03.Testing train and fine tune tesserct (default langdata_lstm)
Requirements langdata_lstm , tesseract 4 , tessdata_best

Load file to your folder and extract : https://drive.google.com/drive/folders/1ABo7ooO62Tb03RR_VvkdshRVG9vz23sl?usp=sharing

## 04.Train and fine tune
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/102C8_iY5TtgnHSpeaAnFatcOfoMOAHgU?usp=sharing)

Run scrript script_basic.ipynb or script_config_error.ipynb
Requirements langdata_lstm , tesseract 4 , tessdata_best

Custom tha.training_text with my own dataset more than 1.9 M sentences

<!-- Load file to your folder and extract : https://drive.google.com/drive/folders/1ABo7ooO62Tb03RR_VvkdshRVG9vz23sl?usp=sharing -->

## 05.Performance testing
report_performace_final.csv




