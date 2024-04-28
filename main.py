import streamlit as st
from PyPDF2 import PdfReader  

def main():
    st.sidebar.title("🙂💬 Text summarization")
    st.sidebar.markdown('''## About''')
    st.sidebar.markdown('''This app is an LLm chatbot ''')
    st.sidebar.markdown(''' --[about us](https://emojicopy.com/)''')
    st.sidebar.markdown('''--[contact us](https://emojicopy.com/) ''')

    st.sidebar.write('made by 🖕🫦')
    
    st.header("Text Summarization 💬")
    st.write("Choose the input method:")

    input_method = st.radio("Input Method:", ("Text", "PDF"))

    if input_method == "Text":
        user_input = st.text_area("Enter your text here")
    else:
        pdf_file = st.file_uploader("Upload PDF", type=['pdf'])
        if pdf_file is not None:
            pdf_reader = PdfReader(pdf_file)
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()
            user_input = pdf_text
        else:
            user_input = None

    if st.button("Summarize"):
        if user_input:
            summary = extractive_summarization(user_input)
            if summary:
                st.write("Summary:")
                st.write(summary)
            else:
                st.warning("Sorry, I can't summarize this text.")
        else:
            st.warning("Please enter some text or upload a PDF.")

def extractive_summarization(text):
    sentences = text.split(".")
    
    word_freq = {}
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    sentence_scores = {}
    for sentence in sentences:
        score = sum([word_freq[word] for word in sentence.split()])
        sentence_scores[sentence] = score
    
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
    
    summary = ". ".join(top_sentences)
    if len(summary) > 0:
        return summary
    else:
        return None

if __name__=='__main__':
    main()