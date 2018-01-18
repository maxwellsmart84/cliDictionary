# import dataGetter -- this should be the thing that gets data aka request-promise or something
import json
from difflib import get_close_matches

def get_dict():
    requestdata = "thing to get the stuff up there"
    dictionary = json.load(requestdata)
    return dictionary

__dictionary__ = get_dict()

def input_dialog():
    userinput = input('Enter a word for a defintion:')
    stringword = "%s" % userinput
    definition = get_definition(stringword)
    return definition

def get_definition(userinput):
    word = userinput.lower()
    if word in __dictionary__:
        return __dictionary__[word]
    elif len(get_close_matches(word, __dictionary__.keys())) > 0:
        return handle_matches(word, __dictionary__)
    else:
        print('Sorry we could not define that word')
        return input_dialog()

def handle_matches(matchInput, dictionary):
    matches = get_close_matches(matchInput, __dictionary__.keys())
    matchlen = len(matches)
    if matchlen != 0:
        newinput = input('Did you mean %s ? Enter Y or N') % matches[0]
          return newinput
        if newinput == 'n':
          matches.pop(0)
          return newinput
        else:
            return matches[0]
    else:
      print('Sorry we did could not find a match')
      return input_dialog()

