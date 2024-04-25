import gradio as gr
from pythainlp.tokenize import word_tokenize

def tokenize(text):
    text_tokenized = word_tokenize(text, engine='newmm')
    text_tokenized = " | ".join(text_tokenized)
    return text_tokenized

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Thai Word Tokenization
    Start typing below to tokenize Thai word with [newmm](https://github.com/wisesight/newmm-tokenizer).
    """
    )

    inp = gr.Textbox(placeholder="Some Sentence", label='Input')
    out = gr.Textbox(label='Output')

    btn = gr.Button("Tokenize")

    btn.click(fn=tokenize, inputs=inp, outputs=out)
    
    gr.Markdown(
    """
    Repo: [https://github.com/huak95/thai-tokenizer-gradio](https://github.com/huak95/thai-tokenizer-gradio)
    """
    )

if __name__  == "__main__":
    demo.launch(
        server_port=7860
    )