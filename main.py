from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def stemSentence(sentence):
    port = PorterStemmer()
    port.stem(sentence)
    token_word = word_tokenize(sentence)
    # token_word
    stem_Sentence = []
    for i in token_word:
        stem_Sentence.append(port.stem(i))
        stem_Sentence.append(" ")
        return "".join(stem_Sentence)


doc1 = open("doc1.txt", 'r').readline()
doc2 = open("doc2.txt", 'r').readline()
list = (doc1)
final1 = []
for i in list:
    t = i.split('.')
    for k in t:
        final1.append(k)

for i in range(0, final1.count('\n')):
    final1.remove('\n')

list = (doc2)
final2 = []
for i in list:
    t = i.split('.')
    for i in t:
        final2.append(i)

for i in range(0, final2.count('\n')):
    final2.remove('\n')


def remove_common_words_stemming(main, generic):
    finaler = []
    for i in main:
        query = i
        stopwords = generic
        querywords = query.split()
        resultwords = [word for word in querywords if word.lower() not in stopwords]
        result = ''.join(resultwords)
        finaler.append(stemSentence(result))

    return finaler


common_word_list = ['do', 'she', 'they', 'we', 'are', 'is', 'a', 'an', 'in', 'as', 'of']
doc1 = remove_common_words_stemming(final1, common_word_list)
doc2 = remove_common_words_stemming(final2, common_word_list)


def BoyerMorreHorspool(pattern, text):
    m = len(pattern)
    n = len(text)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1;
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1;
            i -= 1
        if j == -1: return i + 1
        k += skip[ord(text[k])]
    return -1


count = 0
doc2_joined = ",".join(map(str, doc2))
for i in doc1:
    checkvar = 0
    checkvar = (BoyerMorreHorspool(str(i), doc2_joined))
    if checkvar > -1:
        count += 1

print("The matches are: ", count)
rate_plag = (2 * count) / (len(doc1) + len(doc2))
print('\nThe rate of plagarisim ' + str(rate_plag))
