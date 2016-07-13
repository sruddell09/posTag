# posTag
This is a part-of-speech tagger using a Hidden Markov Model, specifically, the Viterbi Algorithm, in Python.
This project comes with two pickled dictionaries: 
  A.pickle: contains the tag transition probabilities
    A[tag 1][tag 2] = P(tag 2|tag 1)
  B.pickle: contains the word likelihood
    B[tag][word] = P(word|tag)
This project also contains the files brown.test, which is a list of untagged sentences from the Brown Corpus and brown.test.answers, which is the tagged version of those sentences.

The Python file implements the Viterbi Algorithm + backtrace method on brown.test to find the most likely POS tags using the pickled dictionaries. It then compares the predicted POS tags with the actual answers in brown.test.answers, and calculates the accuracy, which ends up to be roughly 96.19%.

This project was originally created for my Introduction to Natural Language Processing class at San Jose State University.

Scott Ruddell
sruddell09@gmail.com
