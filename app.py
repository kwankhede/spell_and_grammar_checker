import streamlit as st
from transformers import pipeline
from difflib import SequenceMatcher

# Initialize the grammar correction pipeline
pipe = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")

def highlight_differences(original, corrected):
    original_words = original.split()
    corrected_words = corrected.split()
    
    # Use SequenceMatcher to get the opcodes for differences
    matcher = SequenceMatcher(None, original_words, corrected_words)
    highlighted_text = []
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'replace':
            highlighted_text.extend([f'<span style="color: red; text-decoration: line-through;">{word}</span>' for word in original_words[i1:i2]])
            highlighted_text.extend([f'<span style="color: green;">{word}</span>' for word in corrected_words[j1:j2]])
        elif tag == 'delete':
            highlighted_text.extend([f'<span style="color: red; text-decoration: line-through;">{word}</span>' for word in original_words[i1:i2]])
        elif tag == 'insert':
            highlighted_text.extend([f'<span style="color: green;">{word}</span>' for word in corrected_words[j1:j2]])
        elif tag == 'equal':
            highlighted_text.extend(original_words[i1:i2])
    
    return ' '.join(highlighted_text)

def correct_and_compare(text):
    # Split text into sentences for processing
    sentences = text.split('. ')
    corrected_sentences = []
    
    # Correct each sentence individually
    for sentence in sentences:
        if sentence:
            corrected_sentence = pipe(sentence, max_new_tokens=50)[0]['generated_text']
            corrected_sentences.append(corrected_sentence)
    
    corrected_text = '. '.join(corrected_sentences).replace(' .', '.')
    
    # Remove redundant periods
    corrected_text = corrected_text.replace('..', '.')
    
    # Highlight differences
    highlighted = highlight_differences(text, corrected_text)
    
    return text, corrected_text, highlighted

# Streamlit app interface
st.title("Grammar Correction App")

input_text = st.text_area("Enter Text", "Type your text here...")

if st.button("Correct Grammar"):
    original_text, corrected_text, highlighted_text = correct_and_compare(input_text)
    
    st.markdown("### Original Text:")
    st.write(original_text)
    
    st.markdown("### Corrected Text:")
    st.write(corrected_text)
    
    st.markdown("### Comparison:")
    st.markdown(highlighted_text, unsafe_allow_html=True)
