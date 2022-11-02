# You may earn 1 point of extra credit (and so get a 4/3 on the lab) if you use google translate to convert the phrase "python is awesome" into at least 100 other languages and upload these translations to sakai. Fortunately, there is a python interface to google translate, so you don't have to do this manually... I feel gross just thinking about doing this manually... you can just use a for loop!

# The python library is called deep_translator, and it provides interfaces to many different translation services. You can find the documentation at https://pythonrepo.com/repo/nidhaloff-deep-translator-python-miscellaneous, although you won't need to look in detail at the documentation to complete this assignment.

# You can install deep_translator library similarly to how you installed youtube-dl library, using the pip3 command. The command should look something like

# $ pip3 install deep_translator
# (Your command may look slightly different depending on your computer's settings.)

# Then you can translate from English to Spanish using the following commands in interactive python:

# >>> from deep_translator import GoogleTranslator
# >>> GoogleTranslator(source='en', target='es').translate("python is awesome")
# 'Python es asombroso'
# We can also get the list of all supported languages using the command

# >>> GoogleTranslator.get_supported_languages()
# ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu', 'Filipino', 'Hebrew']
# Now, to complete the assignment, all you have to do is loop over the list above, calling the translate function with target= each of the supported languages.

