'''
This lab has three tasks.

TASK 1:
Implement the `generate_comment` function below.

TASK 2:
Redefine the `madlibs` and `replacements` variables so that the generated comments are what you want your reddit bot to say.
You must have at least 6 different madlibs.
Each madlib should be 2-5 sentences long and have at least 5 [REPLACEMENT] [WORDS].

TASK 3:
Use your `generate_comment` function to post at least 100 messages to the `Practice posting messages here :)` submission, located at:
<https://old.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/>
You should have at least 10 top level comments and at least 10 replies to comments (but it's okay if they're all replies to the same comment).

SUBMISSION:
Upload your bot's name and your `madlib.py` file to sakai.
'''

madlibs = [
    "[BEEF] is a [GREAT] protien to make [SOUP] with. I love [EATING] well [COOKED] [MEALS], such as [BAKED BEANS]."
    "I have been trying to learn how to eat healthier, such as incorporating more [BEEF] into my diet. Sometimes I think about [EATING] [BAKED BEANS], but then I ask myself is this a healthy [MEAL]? Who knows, I'll just stay and enjoy my [BEEF]."
    "Learning to cook is hard; the last time I [COOKED] [BEEF], I ended up with a [MEAL] that looked more like [BAKED BEANS]. Ugh! I just want to make a good [SOUP]."
    "I love the way that Bardot [COOKED] my [BAKED BEANS]. They also make a [GREAT] [BEEF] [SOUP]."
    "If I had a choice, I would choose one [MEAL] of [LAMB CHOPS] over ten [MEALS] of [BAKED BEANS]. I believe in quality, [GREAT] food over quantity, every time."
    "Do you prefer [BAKED BEANS] or [LAMB CHOPS]? I'm deciding what [MEAL] to cook for our potluck; I loved the [BEEF] [SOUP] that Steven [COOKED] last time."
    ]

replacements = {
    'BEEF' : ['LAMB', 'MUTTON', 'PORK', 'BACON', 'STEAK','CHICKEN','CHICKPEAS'],
    'GREAT' : ['WONDERFUL','FANTASTIC','DOPE','DELICIOUS','TASTY','KILLER','GOOD'],
    'SOUP' : ['STEW','APPETIZER','SAUCE','CHOWDER','BROTH','BISQUE','GOULASH','BOUILLON'],
    'EATING' : ['CHOWING','CONSUMING','DEVOURING','INGESTING','MUNCHING'],
    'COOKED' : ['PREPARED','MADE','PUT TOGETHER','ASSEMBLED','FIXED'],
    'MEALS' : ['SNACKS','BITES','NIBBLES','DISHES'],
    'MEAL' : ['SNACK','BITE','NIBBLE','DISH'],
    'LAMB CHOPS' : ['CURED HAM', 'EGGS BENEDICT', 'GOAT CHEESE SKEWERS','CURLY FRIES'],
    'BAKED BEANS' : ['GRILLED CHEESE','HAMBURGER','PEPPERONI PIZZA','SWEET POTATO FRIES','HAM AND CHEESE PANINI'],
    }


def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly selected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    Instead, you should ensure that the madlibs that you create will all be grammatically correct when this substitution procedure is followed.
    '''