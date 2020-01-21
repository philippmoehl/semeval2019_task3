# coding=utf-8
"""Helper functions. """

import re


def emo_transf(emo):
    """transforms emotion expression to general format"""
    return '_'.join(emo.split())


def all_caps(text: str) -> str:
    """annotates all cap characters in a text expression"""
    words = re.findall(
        r'(\b(?:[A-Z]+[A-Z]*|[A-Z]*[A-Z]+)\b(?:\s+(?:[A-Z]+[A-Z]*|[A-Z]*[A-Z]+)\b)*)', text
    )
    upper = [word for word in words if len(word) > 1]
    if len(upper) == 0:
        return text
    if len(upper) > 1:
        return 'scream ' + text.lower().strip()
    return text.replace(upper[0], 'scream ' + upper[0]).lower().strip()


def word_reps(text: str) -> str:
    """Cut word repetitions at 3 times in `t`."""
    def _replace_wrep(expr):
        sngl_expr, _ = expr.groups()
        return 3 * f' {sngl_expr} '
    re_wrep = re.compile(r'(\b\w+\W+)(\1{3,})')
    replaced = re_wrep.sub(_replace_wrep, ' ' + text + ' ')
    return ' '.join(replaced.split())


def emoji_clean(text: str) -> str:
    """clean emoticon expressions from - """
    tokens = []
    for token in text.split():
        if len(token) > 3 and '-' in token:
            token = token.replace('-', '_')
        tokens.append(token)
    return ' '.join(tokens)


def emoji_reps(text: str) -> str:
    """annotate repeated emoticons"""
    return re.sub(r'\b(([a-z]+(?:_[a-z]+)+))( \1\b)+', 'repeated ' + r'\1', text)


def emoji_remove_underscope(text: str) -> str:
    """cleans text from underscops in emoji expressions and <> in annotations"""
    tokens = []
    for token in text.split():
        if len(token) > 3 and '_' in token:
            token = token.replace('_', ' ')

        if token[0] == '<' and token[-1] == '>':
            token = token[1:-1]

        tokens.append(token)
    return ' '.join(tokens)

