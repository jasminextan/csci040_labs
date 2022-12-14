'''
Overview:

To celebrate Halloween, you will practice HTML and file/string operations by editing the book Dracula to make it even more scary.

Instructions:
The copyright on the book Dracula has expired, and the book is now in the public domain. Project Gutenberg (https://gutenberg.org) is a website that makes all public domain books easily downloadable. Dracula is located at http://www.gutenberg.org/files/345/345-h/345-h.htm . Visit this webpage and save it to your computer in a file called dracula.html (use: right click -> save as).
Create a python file called dracula.py file that:
Reads in the text from dracula.html.
Replaces all occurrences of the word "Dracula" with "Izbicki".
All occurrence of the word Izbicki should be in bold so that they are easy to see.
Recall that the HTML to make a string of text bold is <strong></strong>. Also note that the title of the book is "D R A C U L A" and this should also change to "I Z B I C K I", and that occurrences of "DRACULA" should be replaced by "IZBICKI" maintaining the same capitalization scheme.
Replaces all occurrences of the word "count" with the word "professor". Thus, all occurrences of the phrase "Count Dracula" will be replaced by the phrase "Professor Izbicki".
Note that the word "count" is sometimes capitalized and sometimes lowercase. You should be able to replace both of these words with the correct case. This replacement will sometimes lead to ungrammatical sentences like transforming Count me in into Professor me in, but that's okay for this assignment.
Note that the string "count" sometimes appears inside of a different word, and when this happens, you should not perform the replacement. So for example: words like "country" and "accounting" should not be changed to "professorry" and "acprofessoring".
Replaces all occurrences of the phrase "Bram Stoker" with your name.
Saves the resulting story to a file called izbicki.html.
Note that your final saved file should still have all the html code that makes it a valid webpage.
Upload both your dracula.py code and izbicki.html output file to Sakai.
'''

with open('dracula.html', encoding='utf8') as f:
    e = f.read()

final_text = e.replace('dracula', '<strong>izbicki</strong>')
final_text = final_text.replace('Dracula', '<strong>Izbicki</strong>')
final_text = final_text.replace('DRACULA', '<strong>IZBICKI</strong>')
final_text = final_text.replace('D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A', '<strong>I&nbsp;Z&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I</strong>')


final_text = final_text.replace('count', 'professor')
final_text = final_text.replace('Count', 'Professor')
final_text = final_text.replace('Bram', 'Jasmine')
final_text = final_text.replace('Stoker', 'Tan')

with open('izbicki.html', 'w', encoding='utf8') as f:
    f.write(final_text)