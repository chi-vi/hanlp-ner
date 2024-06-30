#!/usr/bin/python3

import os, re, gc, json, hanlp, torch
from flask import Flask, request

TASKS = {}

def load_task(kind):
    if kind in TASKS:
        return TASKS[kind]

    if kind == '3':
        mtl_task = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ERNIE_GRAM_ZH)
        del mtl_task['tok/coarse']

    elif kind == '2':
        mtl_task = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)
        del mtl_task['tok/coarse']

    else:
        mtl_task = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)
        del mtl_task['tok/coarse']

    del mtl_task['con']
    del mtl_task['dep']
    del mtl_task['sdp']
    del mtl_task['srl']
    del mtl_task['ner/pku']
    del mtl_task['ner/ontonotes']
    del mtl_task['pos/pku']
    del mtl_task['pos/863']

    TASKS[kind] = mtl_task
    return mtl_task

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route("/mtl/<kind>", methods=['POST'])
def parse_text(kind):
    inp_data = request.get_data(as_text=True).splitlines()
    mtl_data = load_task(kind)(inp_data)

    torch.cuda.empty_cache()
    gc.collect()

    return mtl_data.to_json()

@app.route("/tok/<kind>", methods=['POST'])
def parse_toks(kind):
    inp_data = request.get_data(as_text=True).splitlines()
    mtl_data = load_task(kind)(inp_data)

    torch.cuda.empty_cache()
    gc.collect()

    return mtl_data.to_json()

## start app
if __name__ == '__main__':
    from waitress import serve
    serve(app, port=5555)
