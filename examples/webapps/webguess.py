# Next line disabled pylint warnings about bottle.request.params:
# pylint: disable=E1135,E1136

import bottle
import random
import traceback

def pickSecretNumber():
    """Returns random number between 1 and 10"""    
    return random.randrange(1, 11)

def checkGuess(guess:int, secretNum:int) -> str:
    """Prints a hint showing relation of `guess` to `secretNum`"""    
    if guess < secretNum:
        return "Your guess is too low."
    elif guess > secretNum:
        return "Your guess is too high."
    else:
        return "You got it!!"
    
@bottle.route('/')
def welcome():  
    return HTML_FORM.format("")

@bottle.route('/checkguess')
def checkguess():
    print("Starting checkguess")
    if 'guess' in bottle.request.params:
            
        try:
            guess = int(bottle.request.params['guess'])
        except ValueError:
            traceback.print_exc()
            return HTML_FORM.format("You entered an invalid number.")
        name = bottle.request.params['name']
        hint = checkGuess(guess, secretNum)

        if name != "":
            name += ", "
        print("Ending checkguess")
        if guess != secretNum:
            return HTML_FORM.format(name + hint)
        else:
            return HTML_WIN_RESPONSE
    else:
        return """Please <a href="/">use the form</a> to access this application."""

secretNum = pickSecretNumber()

HTML_WIN_RESPONSE = """<html><body>
        <h1>Welcome to Secret Guess Challenge!</h1>
        You got it!
        </body></html>"""

HTML_FORM = """
<html>
<body>
<h1>Welcome to the Challenge!</h1>

<form action="/checkguess">
Enter your guess (1-10): 
<input type='text' name='guess' ><br>
Enter your name: <input type='text' name='name'>
<input type='submit' value='Submit Guess'>
</form>
{}
</body>
</html>
"""

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)
