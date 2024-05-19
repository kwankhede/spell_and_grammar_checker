# Grammar and Spelling Correction App

## Overview

This project implements a grammar correction app using the `transformers` library for natural language processing (NLP). The app corrects grammar mistakes in text input and provides a comparison between the original and corrected text with highlighted differences.

## Project Components

1. **Correction Pipeline**: The app initializes a grammar correction pipeline using the T5 model (`vennify/t5-base-grammar-correction`) from Hugging Face Transformers. This pipeline corrects grammar mistakes in the input text.

2. **Text Comparison**: The app provides a function to compare the original text with the corrected text and highlight the differences using HTML formatting.

3. **User Interface**: The main function `correct_and_compare(text)` takes input text, corrects its grammar, and displays the original and corrected text with highlighted differences using HTML display in Jupyter Notebook.

## How to Use

1. **Clone Repository**: Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/yourusername/grammar-correction-app.git
