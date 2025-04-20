# Ask a Virtual Assitant: Why does yaml have functions called load and safe_load?
  # yaml load can read any yaml even stuff that could be dangerous if it ontains embedded python objects or sytstem commands
  # yaml safe_load reads only safe, basic yaml types like dictionaries, lists, strings and numbers

  #for example someone could embed this {"rm -rf /"} in the code, and if it was loaded with just load, it would erase your
  #whole hard drive, but it wouldnt do it with safe_load