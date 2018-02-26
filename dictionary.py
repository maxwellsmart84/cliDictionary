# import dataGetter -- this should be the thing that gets data aka request-promise or something
import json
from difflib import get_close_matches

# load database and begin prompt
__dictionary__ = get_dictionary()
input_dialog()

def get_dictionary():
    requestdata = "thing to get the stuff up there"
    dictionary = json.load(requestdata)
    return dictionary

def input_dialog():
    userinput = input('Enter a word for a defintion:')
    stringword = "%s" % userinput
    definition = get_definition(stringword)
    return definition

def get_definition(userinput):
    word = userinput.lower()
    if word in __dictionary__:
        pretty_print_defintions(__dictionary__[word])
        return input_dialog()
    elif len(get_close_matches(word, __dictionary__.keys())) > 0:
        handle_matches(word, __dictionary__)
        return input_dialog()
    else:
        print('Sorry we could not define that word')
        return input_dialog()

def handle_matches(matchInput, dictionary):
    matches = get_close_matches(matchInput, __dictionary__.keys())
    matchlen = len(matches)
    if matchlen != 0:
        newinput = input('Did you mean %s ? Enter Y or N') % matches[0]
        newinput.lower()
        if newinput == 'n':
          matches.pop(0)
          return newinput
        elif newinput == 'y':
            defintions = dictionary[matches[0]
            return pretty_print_defintions(defintions)
        else:
          print('Please enter Y or N')
          return handle_matches(matchInput, dictionary)
    else:
      print('Sorry we did not find a match')
      return input_dialog()

def pretty_print_defintions(definition):
  if isinstance(definition, list):
      for item in definition:
          print(item)
  else:
      print(definition)