# Text Compression Algorithm

This project implements a custom text compression algorithm using a combination of the **Burrows-Wheeler Transform (BWT)**, **Move-to-Front (MTF) Encoding**, and **Lempel-Ziv-Welch (LZW) Compression**. The algorithm is designed to compress large text files efficiently while maintaining a reasonable balance between compression ratio and speed.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Compressing a File](#compressing-a-file)
  - [Decompressing a File](#decompressing-a-file)

## Introduction
This project demonstrates the use of several well-known compression techniques. It transforms the input text using Burrows-Wheeler Transform (BWT) to improve the predictability of the data, followed by Move-to-Front Encoding (MTF), which captures character locality, and finally compresses the data using the Lempel-Ziv-Welch (LZW) algorithm.

## Features
- **Burrows-Wheeler Transform (BWT)**: Rearranges data into clusters of similar characters.
- **Move-to-Front (MTF) Encoding**: Reduces redundancy by encoding repeated characters.
- **Lempel-Ziv-Welch (LZW) Compression**: Applies dictionary-based compression to encode patterns efficiently.
- Compresses text files of varying sizes, from small documents to large literary works.
- Decompression is fully supported, allowing for the restoration of original text files.

## Requirements
```bash
pip install -r requirements.txt
```

## Usage

### Compressing a File
To compress a text file, use the following command:
```bash
python compress.py -i <path to input file>.txt -o <path to output file>.bin
```
- `-i`: Path to the input text file.
- `-o`: Path to the output binary file for compressed data.

### Decompressing a File
To decompress a binary file back to text:
```bash
python decompress.py -i <path to input file>.bin -o <path to output file>.txt
```
- `-i`: Path to the input binary file (compressed data).
- `-o`: Path to the output text file.
