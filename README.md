# PS3 Top Games (via [MetaCritic](http://www.metacritic.com))

You will be needing [Python](https://www.python.org/), [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/) and [Flask](http://flask.pocoo.org/) to run this python script.

Make sure you have Python 3 installed

If you do not have Python 3 installed I recommend you use [pyenv](https://github.com/yyuu/pyenv)

### Linux/Mac OS X
```
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

This command instructs pyenv to download, build, and install python 3.4.3

```
pyenv install 3.4.3
```

Run this within the directory you will be saving the python script it will define the version of python the scripts in that directory should run.

```
pyenv local 3.4.3
```

### Windows
Visit the [python website](https://www.python.org/) and download the python3 installer.

#### Last install step
Run this commend to install the required libraries:

```
pip install beautifulsoup4 flask
```
### Ready?
You should now by able to run the script by typing in:

```
python ps3top_live.py
```
-OR-

```
python3 ps3top_live.py
```

#### Usable routes
Index: http://127.0.01:5000/

Games List: http://127.0.0.1:5000/games

Specific Game: http://127.0.0.1:5000/games/TITLE_OF_GAME *(this title can be copied and pasted in the url)*
