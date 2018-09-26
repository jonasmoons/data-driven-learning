# Data science fundamentals cheatsheet

## Common string methods
| Method | Description | Example |
| ------ | ----------- | ------- |
| `lower()` | Lowercases the string | `"HELLO".lower()` |
| `upper()` | Uppercases the string | `"hello".upper()` |
| `replace()` | Searches for a string in a string and replaces that | `"I like pie".replace("pie", "cookies"`) |
| `find()` | Gives the position of a string in another string | `"Jantje".find("je")` |
| `strip()` | Removes all whitespace before the beginning and end of a string | `"    hello  ".strip()` |
| `in` | Not a method, but an operator to check if a string is in another string | `"Jan" in "Jantje"` |


## Comparisons
All of these evaluate to `True`

| Operator | Description | Example |
| -------- | ----------- | ------- |
| `==` | Is the same | `42 == 42` |
| `!=` | Is not the same | `"Tinus" != "Barrie"` |
| `<`  | Is lesser than | `30 < 40` |
| `<=` | Is lesser or equals than | `30 <= 30` |
| `>`  | Is greater than | `40 > 30` |
| `>=` | Is greater or equals than | `40 >= 40` |
| `in` | String is in other string | `"Jan" in "Jantje"` |
| `not in` | String is not in other string | `"Piet" not in "Jantje"` |
| `and` | Two comparisons are both true | `("Jan" in "Jantje") and ("Piet" in "Pietje")` |
| `or` | One of either is true | `("Jan" in "Jantje") or ("Piet" in "Jantje")` |

## Terminal commands
| command | use | example |
| ------- | --- | ------- |
| `ls` | List files in current directory | `ls` |
| | List files as a list | `ls -l` |
| `cd` | Change to directory | `cd Desktop` |
|  | Up one level in directory structure | `cd ..` |
| `mkdir` | Make a directory | `md pythoncode` |
| `pwd` | Print working directory | `pwd` |
| `touch` | Create a new empty file | `touch test.py` |
| `cat` | Print the contents of a file | `cat test.py` |
| `cp` | Copy one or more files | `cp test.py test2.py` |
| `mv` | Rename or move a file | `mv test2.py test3.py` |
| `rm` | Delete a file | `rm test3.py` |
| | Delete a directory | `rm -r pythoncode` |
| `python` | Run a python program | `python mycode.py` |

### Terminal tips
* Try the TAB key to autocomplete your commands
* Use up and down arrow keys for previous / next commands
* Use CTRL-C to stop something
* Use CTRL-D to exit the Python interpreter
* A caret (`^`) stands for Control, e.g. ^X means 'Press CTRL and then X'

## Git commands
| command | use | example |
| ------- | --- | ------- |
| `git` | Prints most used `git` commands | `git` |
| `git init` | Create a new repository | `git init` |
| `git add` | Add a file to the repository | `git add test.py` |
| | Add all files in directory to repository | `git add .` |
| `git commit` | Commit changes to repository | `git commit -m "Your message here"` |
| `git clone` | Create a working copy of a repository | `git clone git@github.com:hay/hu-dsf.git` |
| `git status` | List changes in your working directory | `git status` |
| `git log` | List what happened in your repository | `git log` |