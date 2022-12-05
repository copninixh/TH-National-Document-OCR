# Thai National Document Optical Character Recognition (THND OCR) 
[![DOI](https://zenodo.org/badge/379371970.svg)](https://zenodo.org/badge/latestdoi/379371970)

#### Tesseract OCR tools for read Thai National Document used TH Sarabun National Font trained and fine-tuned. Read README.md to see about my process.

- Part I : https://github.com/copninich/TH-National-Document-OCR-Part-I

- Part II : https://github.com/copninich/TH-National-Document-OCR-Part-II

- Medium : https://medium.com/@copninich/5a673cc8a686


## 0. Information
### 0.1 Tool
- Tesseract : https://github.com/tesseract-ocr/tesseract
### 0.2 Datasets
- PyThaiNLP (Prachathai) : https://github.com/PyThaiNLP/prachathai-67k
- PyThaiNLP (ThaiGov V2 Corpus) : https://github.com/PyThaiNLP/thaigov-v2-corpus
- PyThaiNLP (ThaiGov Archive corpus) : https://github.com/PyThaiNLP/thaigov-archive-corpus
- Thaisum : https://github.com/nakhunchumpolsathien/ThaiSum 
- TR-TPBS : https://github.com/nakhunchumpolsathien/TR-TPBS
### 0.3 Project information
- Ai Builders 2021
- Kampanart Chaimooltan

## 01.Performance tested
I used Character Errorate and leght string (OCR & Correct Text) and output result testing (.csv file)

## 02.Generated datasets
I used PIL library. in addtion, I used TH Sarabun formart font 72 px to create datasets.

Link : https://www.kaggle.com/copninich/thaienglish-character-in-th-sarabun-font

## 03.Tested trained and fine-tuned Tesseract (default langdata_lstm)
Requirements 
1. langdata_lstm
2. tesseract v.4
3. tessdata_best

Load file to your folder and extract : https://drive.google.com/drive/folders/1ABo7ooO62Tb03RR_VvkdshRVG9vz23sl?usp=sharing

## 04.Trained and fine-tuned
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/102C8_iY5TtgnHSpeaAnFatcOfoMOAHgU?usp=sharing)

Run script `script_basic.ipynb` or `script_config_error.ipynb`

Requirements 
1. langdata_lstm
2. tesseract v.4
3. tessdata_best

Custom `tha.training_text` with my own datasets more than 1.9 M sentences

<!-- Load file to your folder and extract : https://drive.google.com/drive/folders/1ABo7ooO62Tb03RR_VvkdshRVG9vz23sl?usp=sharing -->

## 05.Performance tested
`report_performace_final.csv`
