import re,csv
import collections

class spellCorrector:
    def __init__(self, filepath=None,alphabet=None,url=None):
        if not alphabet:
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if not filepath:
            filepath = r'/home/alan/Dropbox/2016 summer/database design/Project/Project Code/MyLib/Data/big.txt'

        words = self.words(open(filepath).read())
        if url: self.addKeyWords(url,words)
        self.NWORDS = self.train(words)
        self.alphabet = alphabet

    def words(self,text):
        return re.findall('[a-z]+',text.lower())

    def train(self,features):
        model = collections.defaultdict(lambda:1)
        for f in features:
            model[f] += 1
        return model

    def edits1(self,word):
        splits = [(word[:i],word[i:]) for i in range(len(word)+1)]
        deletes = [a + b[1:] for (a,b) in splits if b]
        transposes = [a+b[1]+b[0]+b[2:] for (a,b) in splits if len(b)>1]
        replaces = [a+c+b[1:] for (a,b) in splits for c in self.alphabet if b]
        inserts = [a+c+b for (a,b) in splits for c in self.alphabet]
        return set(deletes + transposes + replaces + inserts)

    def known_edits2(self,word):
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.NWORDS)

    def known(self,words):
        return set(w for w in words if w in self.NWORDS)

    def known_suffix(self,word):
        if word.endswith('ly'):
            tmp = word[:len(word)-1]
            prefix_can = self.known([tmp]) or self.known(self.edits1(tmp)) or self.known_edits2(tmp) or [tmp]
            prefix = max(prefix_can,key = self.NWORDS.get)
            result = prefix + 'ly'
            return set([result,])
        elif word.endswith('ed') or word.endswith('d'):
            tmp = word[:len(word)-2]
            prefix_can = self.known([tmp]) or self.known(self.edits1(tmp)) or self.known_edits2(tmp)
            if not prefix_can:
                tmp = word[:len(word)-1]
                prefix_can = self.known([tmp]) or self.known(self.edits1(tmp)) or self.known_edits2(tmp)
            prefix_can = prefix_can or [tmp]
            prefix = max(prefix_can,key = self.NWORDS.get)
            result = prefix + (lambda: 'd' if prefix.endswith('e') else 'ed')()
            return set([result,])
        elif word.endswith('s'):
            tmp = word[:len(word)-1]
            prefix_can = self.known([tmp]) or self.known(self.edits1(tmp)) or self.known_edits2(tmp) or [tmp]
            prefix = max(prefix_can,key = self.NWORDS.get)
            result = prefix + 's'
            return set([result,])
        elif word.endswith('es'):
            tmp = word[:len(word)-2]
            prefix_can = self.known([tmp]) or self.known(self.edits1(tmp)) or self.known_edits2(tmp) or [tmp]
            prefix = max(prefix_can,key = self.NWORDS.get)
            result = prefix + 'es'
            return set([result,])
        return {}


    def correct(self,word):
        correct0 = self.known([word])
        correct1 = self.known(self.edits1(word))
        correct2 = self.known_edits2(word)
        correct3 = self.known_suffix(word)

        candidates = correct0 or correct3 or correct1 or correct2 or [word]

        recom_set = []
        bol = False
        if correct3: bol = True
        for i in range(5):
            if candidates:
                tmp = max(candidates,key = self.NWORDS.get)
                if tmp not in recom_set: recom_set.append(tmp)
                candidates.remove(tmp)
            else:
                if bol: candidates = candidates or correct1 or correct2 or [word]
                else: break
        return recom_set

    def addKeyWords(self,url,words):
        self.KEYWORDS=[]
        for row in open(url):
                tmp = row.rstrip('\n')
                words.append(tmp)
                self.KEYWORDS.append(tmp)





#wc = spellCorrector()
#print(wc.correct('Classical'))
