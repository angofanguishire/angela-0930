from h2o_wave import main, app, Q, ui
import requests
import json
import ast


@app('/demo')
async def serve(q: Q):

    endpoint = 'http://backend:8000/ner/'

    q.page['header1'] = ui.header_card(
    box='5 1 4 1',
    title='Named Entity Recognition Playground',
    subtitle='Time to analyze some text with SpaCy!',
    image='https://raw.githubusercontent.com/github/explore/8cf1837393d83900e767cc895dcc814d053e2ffe/topics/spacy/spacy.png',
    color='card'
)

    if q.args.show_inputs:

        path=endpoint+q.args.textbox_multiline
        output = requests.get(path)
        dict = ast.literal_eval(output.json())

        q.page['example'].items = [
            ui.text('Entered text:'),
            ui.text(f'{q.args.textbox_multiline}'),
            ui.button(name='show_form', label='Try again', primary=True),
        ]

        q.page['ner_result'] = ui.markdown_card(
            box='5 6 4 4', title="NER results:",
            content=f'{dict["result"]}',
        )

    else:
        q.page['example'] = ui.form_card(box='5 2 4 4', items=[
            ui.textbox(name='textbox_multiline', label='Short text to analyze with named entity recognition:', value= 'Enter an English text here.', multiline=True),
            ui.button(name='show_inputs', label='Process text', primary=True),
        ])

        q.page['ner_result'] = ui.markdown_card(
            box='5 6 4 4', title="NER results:",
            content="Analysis on the way...",
        )


    await q.page.save()