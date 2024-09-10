# Braden Leach
# Sep 10 2024
# f-String Adventure Story

'''
Directions:

1. Update the comment block at the top of this script.

2. Use the Python `input( )` function to prompt (ask) the user for three pieces of information:

     - the hero's first name
     - the setting of the story (e.g., forest, desert, cave system)
     - the object the hero finds while on his/her adventure

3. Assign each piece of information collected to a variable with a short, specific name.

4. Declare (create) a variable named `story` and assign to it the `f-string` that is your adventure story

5. Use the `print( )` function to display your adventure story on the screen.

6. Execute (run) your script in Visual Studio Code and correct any errors.
'''
#variables
first_name = input('Enter your name hero!: (example: Richard)\n')
setting = input('Enter your setting of the story!: (example: Forest)\n')
object = input('Enter what the hero finds on there adventure!: (example: Sword)\n')
story = (f"{first_name}\n{setting}\n{object}\n")
#printed
print(f'Your name is: {first_name} and your setting you chose was{setting}. Along the journey you happen to find a {object}.')




