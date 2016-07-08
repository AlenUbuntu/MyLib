# -*- coding: utf-8 -*-
import re

class fuzzyfinder:
    def __init__(self,collection):
        '''
        collection (iterable): A collection of strings which will be filtered
                               based on the input `text`.
        '''
        self.collection = collection

    def search(self,text):
        """
        Args:
            text (str): A partial string which is typically entered by a user.
            
        Returns:
            suggestions (generator): A generator object that produces a list of
                                     suggestions narrowed down from `collections`
                                     using the `text` input.
        """
        suggestions = []
        text = str(text) if not isinstance(text, str) else text
        pat = '.*?'.join(map(re.escape, text))
        regex = re.compile(pat)
        for item in self.collection:
            r = regex.search(item)
            if r:
                suggestions.append((len(r.group()), r.start(), item))

        return (z for _, _, z in sorted(suggestions))

#suggestions = fuzzyfinder(['abcd', 'defabca', 'aagbec', 'xyz', 'qux'])
#print(list(suggestions.search('abc')))
