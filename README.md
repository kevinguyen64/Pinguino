# Pinguino the Musical Penguin
#### Video Demo: https://youtu.be/FElD8aV4o74
#### Description:

"Pinguino the Musical Penguin" is a command line game where the user has to guess
what musical artist Pinguino is impersonating. The user has 5 "lives" or rather
chances to correctly guess the artist before it is ultimately revealed.

#### Purpose:

Who doesn't love a good guessing game? This game was created with the intentions of making
people think real hard and having fun with it! For me, one of my many passions was not only
playing music, but I also enjoy listening to music as well. This game has a database of 50
different artists, male and female, and of different generations. Artists of different genres
and of different amount of grammys to their names. I feel like this would be a really fun
game for those who are like me, an avid fan of music. My favorite animal is also the penguin,
so Pinguino the penguin came to be. The mission of the players, with the help of some animal
friends, are to guess which musical artist Pinguino is. I do hope you enjoy!

##### Modules and Libraries:

The modules and libraries utilized consist of:

-   **requests:**
        get() method was used to retrieve the response object from Apple Music's API.
-   **sys:**
        Used to retrieve user's name and check for number of command line args.
        exit() method was used if "artists.csv" did not exist or to indicate the end of the game.
-   **json:**
        dumps() method was only necessary to view the string version of the JSON object.
-   **random:**
        choice() method was used to retrieve a random element from the list of names acquired from the "artists.csv".
        randint() method was used to retrieve a random number to index into the list of songs.
-   **re:**
        search() method was used to differentiate between songs where the artist was either the main artist
        or a feature.
-   **csv:**
        DictReader() method was used to read the "artists.csv" and return an iterable object.
        Several functions of the program utilized this method to return values of certain keys.
-   **cowsay:**
        tux(), cow(), turtle(), fox(), kitty(), pig() were methods imported from cowsay library.
        Each method yielded an ASCII art of their respective animal saying a hint, with tux(),
        yielding the penguin, revealing who the mystery musical artist was.
-   **emoji:**
        The emojize() method was used to return the emojis of each of the respective animals
        from the cowsay library.
-   **os:**
        The system() method was used to "clear" the terminal window.
-   **pytest:**
        The raises() method was used to confirm that a SystemExit had occurred when the user correctly
        guessed the mystery artist, therefore ending the game.

The requirements.txt file contains all of the pip-installable libraries or modules needed for this program.
Every other module or library outside of those were already built into Python.

##### CSV:

    The only csv necesitated by the program is the "artists.csv" file.
    There are 50 musical artists, 25 males and 25 females, each with an individual birthdate,
    different musical genre backgrounds, and different amount of grammys earned.
    The csv file was created with the intention of utilizing the csv.DictReader() method
    where each of the keys would get their own functions that returned the value of the respective artist.

##### Individual Functions:

**def arguments():**

    This function was used to ensure that the user inputs their name.

    A minimum of 2 and a maximum of 3 command line arguments were allowed.
    The name of the file was always going to be the first argument.
    And the second and third argument were for if the user wanted to input
    both their first and last names or just their first name.

    If the user did not comply, sys.exit() method would print to them a
    message indicating whether it was too few or too many arguments and then
    kick them out of the program.

    However, if they did comply, and they only inputted one name, presumably
    their first name, then the function returned the one name.
    And if they inputted two names, then the function returned both names concatenated
    with a whitespace in between.


**def name():**

    This function utitlized the DictReader() method on "artists.csv" to return essentially a list of dictionaries.
    Each artist had their own dictionary and this function iterated over each dict, appending the "name" value to
    an empty list stored in the variable "names".

    Then the function returned the value obtained from calling random.choice() on the list, which itself returned
    a random name from the list of names.

    If for some reason the csv was compromised or no longer existed, a FileNotFoundError would have occurred prompting
    sys.exit() to log the user out of the program with the message: "CSV does not exist"


**def guess(g, name):**

    system("clear") method was called to clear the terminal of the intro or previous hint.

    This function took 2 parameters:
        "g" for the user's guess
        "name" for the name of the mystery artist

    If the user's guess matched the name of the mystery artist, then
    the program would end with an ASCII art of a penguin(Pinguino the penguin),
    telling the user they guessed correctly.

    If the user's guess did not match the name of the mystery artist, then the
    function would return an f-string telling the user that their guess was
    incorrect and that they would be given another hint.


**def gender(name):**

    This function took one parameter, that being the mystery artist's name or rather
    the return value of the name function.

    The DictReader() method was utilized to access the csv and return each artist as
    a dictionary.
    A "for loop" was used to iterate over each dictionary until the artist in question was
    matched and then their "gender" value was returned.

    If "artists.csv" was compromised, a FileNotFoundError would have occurred and the program
    would have ended.


**def birthdate(name):**

    This function took one parameter, that being the mystery artist's name or rather
    the return value of the name function.

    The DictReader() method was utilized to access the csv and return each artist as
    a dictionary.
    A "for loop" was used to iterate over each dictionary until the artist in question was
    matched and then their "birthdate" value was returned.

    If "artists.csv" was compromised, a FileNotFoundError would have occurred and the program
    would have ended.


**def genre(name):**

    This function took one parameter, that being the mystery artist's name or rather
    the return value of the name function.

    The DictReader() method was utilized to access the csv and return each artist as
    a dictionary.
    A "for loop" was used to iterate over each dictionary until the artist in question was
    matched and then their "genre" value was returned.

    If "artists.csv" was compromised, a FileNotFoundError would have occurred and the program
    would have ended.


**def grammys(name):**

    This function took one parameter, that being the mystery artist's name or rather
    the return value of the name function.

    The DictReader() method was utilized to access the csv and return each artist as
    a dictionary.
    A "for loop" was used to iterate over each dictionary until the artist in question was
    matched and then their "grammys" value was returned.

    If "artists.csv" was compromised, a FileNotFoundError would have occurred and the program
    would have ended.


**def song(name):**

    This function took one parameter, that being the mystery artist's name or rather
    the return value of the name function.

    The requests.get() method was used on the url of the Apple Music's API to retrieve a
    response object. The Apple Music's API was manually set to retrieve songs by the mystery artist
    with the limit of songs retrieved set to 50.

    This response object was then parsed into a JSON object using the json() method
    and stored in a variable called "o" ("o" for object).

    The json.dumps() method was used on "o" to return the string format of the JSON object, which is
    easily more readable. From here, the dictionaries and their values, some being nested dictionaries,
    were easier to interpret.

    The intended purpose of this function was to retrieve a random song by the mystery artist, whether
    they were the main artist or a feature of another. Therefore, the key that was important was the
    nested "trackName" key, where the value was the name of a song related to the mystery artist.

    The "results" key had a value that was a list of the dictionaries. Each dictionary was in reference to
    a song related to the mystery artist. Since the intentions of the program is to inquire about a new,
    random artist each time it runs, the random.int() method was used with a range of 0-49 to index into the list
    of dicts.

    From there, a random dictionary would be selected, and the "trackName" value would be returned, yielding
    a random song stored in the variable: "song_name".

    Because of issues with some songs on Apple Music's API containing only the name of the mystery artist in their song name.
    A "while loop" was implemented where the function would retrieve a new song related to the mystery artist if that had occurred.

    If "feat" was in the song name, then the problem with differentiating between whether the mystery artist was the main artist
    or a feature of a song was resolved using the re.search() method. The raw string was constructed to split into 2 groups,
    using the string "feat"(for feature) as the middle.

    If the mystery artist's name was in the second group, then they were the feature and a string was returned to the user
    indicating that as such.

    However, if their name wasn't in the second group, then it is presumed that they are the main artist of the song.
    Therefore, a string was returned to the user indicating that the song was theirs.


##### main():

    This function initially calls for the arguments() function to ensure that the user has inputted their names
    and then the return value was stored in a variable called "player".

    Then the number of lives(5) represented by the "🐧" emoji and is initialized in the variable "lives".

    The name() function is called and its return value, which is a random artist from the "artists.csv" file is
    stored in a variable called "n".

    Before the game starts with an introduction to the user and an explanation as to how to play the game,
    system("clear") method is used to clear the screen of the command-line arguments inputted previously.

    The user is then required to click the Enter key to begin the game. This is represented by an input return
    value of nothing (""). If the user does not only click the Enter key, but inputs something else, they are
    requested to click the Enter key again and again until they comply via a while loop. Once they comply,
    system("clear") method is called once again to clear the terminal window of the previous intro.

    The user is given 5 opportunities or rather guesses to guess the musical artist that Pinguino the penguin
    is impersonating. With each guess, they are reminded of how many lives they have remaining. Each wrong guess
    takes off one "🐧" emoji from the lives counter through the replace function, replacing each "🐧" with "".

    Each opportunity the user has to guess the mystery artist is accompanied with a hint. There will be 5 hints
    in total and each one will be provided by a different ASCII art animal using their respective methods. After
    each hint, the system("clear") method is also called to clear the terminal window of the previous hint and ASCII art.

    Cow: The first hint calls on the gender() function and provides the mystery artist's gender.

    Pig: The second hint calls on the birhtdate() function and provides the mystery artist's birthdate.

    Fox: The third hint calls on the genre() function and provides a musical genre that is associated with the mystery artist.

    Kitty: The fourth hint calls on the grammys() function and provides the amount of grammys the mystery artist has won.

    Turtle: The fifth hint calls on the song() function and provides a song associated with the mystery artist, whether they
            were the main artist or the feature on the song.

    After each hint is given, the user is asked to provide their guess as to who the mystery artist may be. The title()
    function is used on the user's input to capitalize the starting letter of each name and lower-case the rest to match
    the syntax of Apple Music's "artists" catalog.

    The user's guess and the name of the mystery artist are entered as the two parameters needed for the guess() function.
    If the user's guess matches the name of the mystery artist, then the tux() method is called and an ASCII art of a penguin
    will indicate to the user that their guess was correct. Otherwise, if the user's guess did not match the name of the
    mystery artist, then the user will be given another hint.

    If it's the last guess and the user guesses correctly, then they will be met with the same penguin telling them as such.
    However, if the user guesses wrong, then Pinguino the penguin reveals himself as the mystery artist and the game ends.


##### Test functions:

The following functions had their own test functions created in the file "test_project.py":

-   **guess():**

            This function had two test functions. One was to test for if the user's guess matched
            the mystert artist's name, and the other was to test if it didn't.
            If the user's guess was correct, then a system exit would have occurred.
            If it was wrong, the user would have been alerted and given another hint.

-   **gender():**

            This function had one test function, testing to see that the gender() function
            returned "Male" for a male artist and "Female" for a female artist.

-   **birthdate():**

            This function had one test function, testing to see that the birthdate() function
            returned the birthdate of the mystery artist in "month/day/year" format.

-   **genre():**

            This function had one test function, testing to see that the genre() function
            returned the musical genre associated with the mystery artist.

-   **grammys():**

            This function had one test function, testing to see that the grammys() function
            returned the number of grammys the mystery artist has won.
