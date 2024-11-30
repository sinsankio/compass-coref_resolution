from typing import Any

import neuralcoref
import spacy

from configs.coref_resolver import *

NLP: Any = None
COREF = None


def init_nlp() -> None:
    global NLP

    NLP = spacy.load(SPACY_MODEL_NAME)


def init_coref(conv_dict: dict) -> None:
    global COREF

    if COREF:
        NLP.remove_pipe(NLP_PIPE_NAME)
    COREF = neuralcoref.NeuralCoref(NLP.vocab, conv_dict=conv_dict)
    NLP.add_pipe(COREF, name=NLP_PIPE_NAME)


def coref_resolve(text: str, conv_dict: dict) -> dict:
    if not NLP:
        init_nlp()
    init_coref(conv_dict)
    return {"text": NLP(text)._.coref_resolved}
