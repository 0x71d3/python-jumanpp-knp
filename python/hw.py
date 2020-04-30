import gzip
import re

def read_corpus(file_name):
    corpus = []
    with gzip.open(file_name) as f:
        for line_byte in f:
            line = line_byte.decode()
            if not re.match(r'<PAGE URL=.*>|</PAGE>', line):
                corpus.append(line.rstrip("\n"))
    return corpus

def build_model(corpus):
    freq = {}
    freq_any = 0
    for text in corpus:
        word_list = text.split()
        for i in range(len(word_list) - 1):
            unigram = word_list[i]
            bigram = tuple(word_list[i:i+2])
            if unigram not in freq:
                freq[unigram] = 0
            freq[unigram] += 1
            if bigram not in freq:
                freq[bigram] = 0
            freq[bigram] += 1
            freq_any += 1
        unigram = word_list[-1]
        if unigram not in freq:
            freq[unigram] = 0
        freq[unigram] += 1
        freq_any += 1
    return freq, freq_any

def estimate_prob(sentence, freq, freq_any):
    word_list = sentence.split()
    prob = 1.0
    unigram = word_list[0]
    prob *= freq[unigram] / freq_any
    for i in range(len(word_list) - 1):
        unigram = word_list[i]
        bigram = tuple(word_list[i:i+2])
        prob *= freq[bigram] / freq[unigram]
    return prob

file_name = "doc0000000000.txt.gz"
corpus = read_corpus(file_name)

freq, freq_any = build_model(corpus)

sentence = "The man is in the house."
prob = estimate_prob(sentence, freq, freq_any)
print(prob)