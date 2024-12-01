import pickle

import gradio as gr

# pickle.load(open("model.pkl", "rb"))

model_pipe = pickle.load(open("model.pkl", "rb"))
# model_pipe.predict(['Subject: enron / hpl actuals for july 11 , 2000\r\nteco tap 10 . 000 / enron ; 75 . 000 / hpl iferc\r\nls hpl lsk ic 30 . 000 / enron'])


def predict(name):
    return model_pipe.predict([text])[0]


with gr.Blocks() as demo:
    gr.Markdown("Start typing below and than click **Run** to see the output")
    with gr.Row():
        inp = gr.Textbox(placeholder = "Email")
        out = gr.Textbox()
    btn = gr.Button("Run")
    btn.click(fn=predict, inputs=inp, outputs=out)

demo.launch()
