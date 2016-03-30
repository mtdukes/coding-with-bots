## Lesson 1: The basics

#### Defining our tools

[__Python__ is a high-level coding language](https://www.python.org/). There are many languages (Ruby, Javascript, PHP), but Python is nice because you can use it to quickly build projects large and small. It has a massive community that builds and maintains __libraries__ of code that extends python's core functionality. You can run python code as executable files or in the Python shell.

The __command line__, accessible in Mac through Terminal or PC through PowerShell, is an interface designed to execute code without a graphical user interface. It's extremely powerful and can be used to chew through complex tasks much faster than through traditional point-and-click software.

__[Sublime](https://www.sublimetext.com/)__ is a text-editor with nice capabalilites like __syntax highlighting__ which can give you clues about the formatting of your code specific to the language you're using. We'll be using Sublime for this workshop, but feel free to explore other text editor options.

__[Github](https://github.com/)__ is a Web-based service built on git, an industry standard system used to manage code and software. It's centered around the idea of __version control__, allowing multiple collaborators to contribute to a code base. Project managers can accept or reject these changes, branch the code in different directions or revert to old versions in case of disaster.

An __API__, or application programming interface, is a system that allows you to easily interact with a third-party's data (or your own, if it's an in-house API). They are typically designed so you can programatically query for specific types of data through requests structured like URLs. For this workshop, we'll be using a Python library that makes using the Twitter API really easy.

A __server__ is just a computer that's going to do whatever we say. It might be remote, like ones we use through [Amazon Web Services](http://aws.amazon.com/), or it could be local on our own machine. Running a remote server for code is nice because it doesn't require you to keep your personal or work machine on all the time.

__Got all that?__

![Brent's got it.](https://raw.githubusercontent.com/mtdukes/coding-with-bots/master/img/brent-yeah.gif)

#### Basic command line

At its core, the command line allows you to navigate the file structure of your computer, creating, moving and deleting like you would with a regular interface. Here's some basic stuff (Note: the dollar sign just demonstrates the prompt, so don't include it in the command.)

Show me the present working directory
```bash
$ pwd
```

Show me the files and folders in the current directory
```bash
$ ls
```

Change the current directory to "Documents"
```bash
$ cd ~/Documents
```

Make a new directory called "code-workshop"
```bash
$ mkdir code-workshop
```

Clear the interface!
```bash
$ clear
```

Use the up and down arrows to scroll through previous commands.

![Brent's got it.](https://raw.githubusercontent.com/mtdukes/coding-with-bots/master/img/deep-end.gif)

#### Let's get Pythoning!

Now that we've made a shiny new directory, let's do some stuff with it.

```bash
mkvirtualenv code-workshop
```

Now we're working in a virtual environment, which keeps everything nice and tidy on our machine so we don't break stuff.

Fire up the Python shell

```bash
python
```

Python can do math, so try it out!
```python
10 + 10
```

Python can do variable assignment!
```python
x = 10
y = 'millennials amirite?'
print x, y
```

Python can do logical tests!
```python
if x > 10:
	print "X is more than 10!"
elif x == 11:
	print "X is 11!"
else:
	print "idk is it 10?"
```

Python can do loops!
```python
for x in range(1,10):
	print x
```
```python
x = 1
while x < 15:
	print "x is",x
	x += 1
```

#### Python data types

Python has five basic types of data: __numbers__, __strings__, __lists__, __tuples__ and __dictionaries__. We won't cover them all extensively, [so here's some good background](http://www.tutorialspoint.com/python/python_variable_types.htm).

__Numbers__ are more complicated than they sound, because computers treat numbers differently. Try:

```python
1/2
```

And:
```python
1.0/2
```

__Strings__ are text objects that have a number of built-in functions. Think of them literally as a string of characters. You can find the length...

```python
myVar = "I am so cool!"
len(myVar)
```

or add or subtract values.
```python
newVar = myVar[0:8] + "NOT" + myVar[7:]
print newVar
```

__Lists__ are really common, and essentially consist of a collection of values that can be numbers, strings, even other lists!

```python
myList = [1,2,3,4,'YAY',6,['7','LISTCEPTION']]
print myList
print myList[1]
print myList[6]
print myList[6][1]
```

You can also loop through lists.

```python
list_to_test = [1,2,3,4,5]
for x in list_to_test:
	if x != 3:
		print x,"is not 3"
	else:
		print x,"is 3"
```

__Dictionaries__ are neat, because they're like lists based on the concept of "key-value pairs." Think of it like an object with certain assignable attributes.

```python
my_truck = {'make':'Nissan','cab_type':'crew','color':'silver','model':'Frontier'}
print my_truck
print 'Tyler bought a',my_truck['make']+' '+my_truck['model']+'. It is',my_truck['color']+'.'
```

You can also use __methods__ specific to the dictionary object, like:
```python
print my_truck.keys()
print my_truck.values()
```

![Brent's got it.](https://raw.githubusercontent.com/mtdukes/coding-with-bots/master/img/explosions.gif)

### Running Python scripts

Even these small bits of code can be extremely powerful, so let's try combining them into a __python script__ and do some real damage. Exit the shell.

```python
exit()
```

Then right click and [download the following file](https://github.com/mtdukes/coding-with-bots/blob/master/code_samples/hello-world.py) into your project folder. Then open the following file in Sublime.

To run the file, enter the following command:

```bash
python hello-world.py
```

Stuck? Have a question about how to do something in Python? Google it! There are so many Python users out there, you're bound to find a good answer.

![Brent's got it.](https://raw.githubusercontent.com/mtdukes/coding-with-bots/master/img/dont-tell-me.gif)

Remember: The best coders know when to ask others for help!

#### Further reading

- [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/)
- [Learn Python the Hard Way](http://learnpythonthehardway.org/)
- [Google's Python class](https://developers.google.com/edu/python/)
- [Learning Python](http://shop.oreilly.com/product/0636920028154.do)

### >>> [Next lesson](./lessonTwo.md)