# coding=utf-8
""" Cleaning pipeline and data loader for SemEval 2019 task 3."""

from typing import List
import csv

from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.dicts.emoticons import emoticons

import emoji

from emot import EMOTICONS
from utils import *


EMOTICONS = {expr: emo_transf(emo) for expr, emo in EMOTICONS.items()}
EMOTICONS_EKPHRASIS = {expr: emo_transf(emo) for expr, emo in emoticons.items()}

TEXT_PROCESSOR = TextPreProcessor(
    # terms that will be normalized
    # optional: numbers, percent, money, time, date
    # user -- potential problem when twitter user
    # url, email, phone -- no relevant information for emotion
    # keep text as simple as possible
    normalize=['url', 'email', 'phone', 'user'],

    # terms that will be annotated - not in original data - test w/ and w/o
    annotate={"repeated", "emphasis", "elongated"},

    # fix HTML tokens
    fix_html=True,

    # corpus from which the word statistics are going to be used
    # for word segmentation
    segmenter="twitter",

    # corpus from which the word statistics are going to be used
    # for spell correction
    corrector="twitter",

    unpack_hashtags=True,  # perform word segmentation on hashtags
    unpack_contractions=True,  # Unpack contractions (can't -> can not)
    spell_correct_elong=True,  # spell correction for elongated words

    # select a tokenizer. You can use SocialTokenizer, or pass your own
    # the tokenizer, should take as input a string and return a list of tokens
    tokenizer=SocialTokenizer(lowercase=True).tokenize,

    # list of dictionaries, for replacing tokens extracted from the text,
    # with other expressions. You can pass more than one dictionaries.
    dicts=[EMOTICONS_EKPHRASIS, EMOTICONS]
)


def process_pipeline(text: str) -> str:
    """processing pipeline for data cleaning"""
    text = all_caps(text)
    text = ' '.join(TEXT_PROCESSOR.pre_process_doc(text))
    text = word_reps(text)
    text = emoji.demojize(text, delimiters=(' ', ' '))

    text = emoji_clean(text)  # handle - in underscore reps of emojis
    text = emoji_reps(text)
    text = emoji_remove_underscope(text)

    return text.lower().strip()


def data_load(file: str) -> List:
    """data loader for training and testing files"""
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter="\t")
        lines = []
        for line in reader:
            lines.append(line)

    return lines

