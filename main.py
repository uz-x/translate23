def googletr():
  from deep_translator import GoogleTranslator as gt
  import time
  langlist = "arabic armenian azerbaijani bengali bosnian bulgarian chinese czech filipino finnish french russian serbian spanish japanese swedish turkish ukrainian vietnamese welsh yiddish zulu english"
  langlist = langlist.split(" ")
  langtxt = "\n"

  for i in range(len(langlist)):
    language = langlist[i].capitalize()
    langtxt += "(" + str(i + 1) + ") " + language + " \n"
    
  text = input("Text: ")
  result = text
  cls()

  start = time.time()
  
  for i in range(1, len(langlist)):
    text = result
    lang = langlist[i]
    if lang == "chinese":
      lang = "chinese (traditional)"
    cls()
    print("Current: " + result)
    print("Translating to " + lang.capitalize() + "...")
    my_translator = gt(source='auto', target=lang)
    result = my_translator.translate(text=text)
    cls()

  end = time.time()
  t = end - start
  
  print("Translation: " + result)
  print("Stopwatch: " + str(t))

googletr()
