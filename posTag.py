import pickle
from math import log

#Part 1: Create Trellis

def create_column(pcol, A, B, word):
    col = {} 
    for ptag in pcol: #for each POS tag in the previous column of the trellis
        for tag in A[ptag]: #for each POS tag that can possibly be preceded by ptag
            if word in B[tag]: #if the current word in the sentence be a particular POS
                if tag not in col: #if the particular POS has not been added to the column yet
                    col[tag] = [None, None] #initialize dummy 
                score = pcol[ptag][0] + log(A[ptag][tag]) + log(B[tag][word]) #calculate the (log) delta
                if col[tag][0] < score:
                    col[tag] = [score, ptag]
    return col

def create_trellis(A, B, words):
    trellis = []
    first_col = {'<s>': [log(1), None]}
    trellis.append(first_col)
    for i in range(1, len(words)):
        col = create_column(trellis[-1], A, B, words[i])
        trellis.append(col)
    return trellis

#Part 2: Find Best Path

def trace_back(trellis):
    crumbs = ['</s>']
    for i in range(len(trellis) - 1, 0, -1):
        crumb = trellis[i][crumbs[-1]][1]
        crumbs.append(crumb)
    crumbs.reverse()
    return crumbs

def tag(A, B, sent):
    words = ['<s>'] + sent.split() + ['</s>']
    tags = create_trellis(A, B, words)
    return trace_back(tags)

if __name__ == '__main__':

    A = pickle.load(open('A.pickle'))
    B = pickle.load(open('B.pickle'))

    tagged = []
    
    f = open('brown.test')
    for line in f:
        sent = line.strip()
        tags = tag(A, B, sent)[1:-1]
        output = ''
        words = sent.split()
        for i in range(len(words)):
            output += words[i] + '_#_' + tags[i] + ' '
        tagged.append(output)
    f.close()

    corr = 0.0 #correctly tags words
    total = 0.0 #total words
    i = 0

    f = open('brown.test.answers')
    for line in f:
        test_words = tagged[i].split()
        ans_words = line.split()
        for j in range(len(ans_words)):
            test_word, test_tag = test_words[j].split('_#_')
            ans_word, ans_tag = ans_words[j].split('_#_')
            if test_tag == ans_tag:
                corr += 1
            total +=1
        i += 1
    f.close()

    print 'Accuracy: %.2f%%' % ((corr/total) * 100)
