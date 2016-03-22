# Coding with bots

This half-day workshop will explore coding basics through the creation of customized Twitter bots with Python. Topics will include use of the command line, installation and basics of the Python programming language, use of the Twitter developer console, practical Github for projects and an introduction to servers.

## Lesson 0: Setting up

Please read this carefully and follow the instructions before the workshop Wednesday. You’ll need to have a few things set up on your machine properly before moving forward. If you’re using a work machine, you will likely have to get IT to use their administrative access to install these items.

 
#### Step 1 (for Mac): Check Python version

All Macs should come pre-installed with Python, the coding language we’ll be using for the workshop. Open Terminal and use the following command to check which version of Python you’re using (press return to execute the line of code).

```bash
python –V
```

You should be running a version of Python 2.7.X. On my machine, for example, I’m running 2.7.10.

You’ll need to tell your machine where to install new packages, so we’ll use a built-in text editor called nano to do that. Enter the following command:

```bash
nano ~/.bash_profile
```

Then paste the following line into the empty text field displayed in Terminal.

```bash
export PATH=/usr/local/lib/python2.7/site-packages:$PATH
```

Save the file by typing ```control+X```, ```Y``` in response to “Save modified buffer?” and ```Return``` to confirm the file name. This will take you back to the command line. Update your Terminal window with the following command:

```bash
source ~/.bash_profile
```

#### Step 1 (for PC): Install Python

Install Python version 2.7 by downloading and installing [the file at the following link](https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi). This will also install pip, which is [like an app store for Python code](http://blog.apps.npr.org/2013/06/06/how-to-setup-a-developers-environment.html).

Run a Powershell window and type the following command (you can paste by right clicking in the Powershell window). This command makes it easier to run Python without specifying its exact location on your machine.

```bash
[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")
```

Restart your Powershell window. You should now be able to enter the following command, which starts the Python shell.

```bash
python
```

Exit the Python shell with:

```python
exit()
```

#### Step 1.1 (for Mac): Install pip
Pip is, [to quote much smarter developers](http://blog.apps.npr.org/2013/06/06/how-to-setup-a-developers-environment.html), like an app store for Python code. It will help you install new tools you need to code projects more efficiently and expand your own code’s capabilities.

Open Terminal and enter the following command. Press ```Return``` to run (you must have admin privileges on your machine):

```bash
sudo easy_install pip
```

#### Step 2 (for Mac): Installing Virtual Environments

Using virtual environments allows you to cordon off all the various packages and libraries you install and get around requirements to run the system as an administrator. To install this software, you will need admin privileges on your machine.

Open Terminal and enter the following command. Press ```Return``` to run:

```bash
pip install virtualenv
```

Next, we’ll install an additional piece of software that will make working with virtual environments a little easier. Open Terminal and enter the following commands, one by one. Press “Return” to run each of them:

```bash
pip install virtualenvwrapper
```

Then, edit your bash profile again using nano:

```bash
nano ~/.bash_profile
```

Then paste the following line into the file, below the one you entered earlier:

```bash
source /usr/local/bin/virtualenvwrapper.sh
```

Save the file by typing ```control+X```, ```Y``` in response to “Save modified buffer?” and ```Return``` to confirm the file name. This will take you back to the command line. Update your Terminal window with the following command:

```bash
source ~/.bash_profile
```

Now, you will be able to create a new virtual environment with:

```bash
mkvirtualenv foo
```

Work on it with:

```bash
workon foo
```

Deactivate with:

```bash
deactivate
```

For more information and follow-up reading, see the virtual environments entry in [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

#### Step 2 (for PC): Installing Virtual Environments

Using virtual environments allows you to cordon off all the various packages and libraries you install and get around requirements to run the system as an administrator.

Open Powershell and enter the following command. Press ```Return``` to run:

```bash
pip install virtualenv
```

Next, we’ll install an additional piece of software that will make working with virtual environments a little easier. Open Terminal and enter the following commands, one by one. Press “Return” to run each of them:

```bash
pip install virtualenvwrapper-win
```

We'll need to slightly tweak the [execution policies on the system](https://virtualenv.pypa.io/en/latest/userguide.html), so as an administrator, get someone in IT to run the following:

```bash
Set-ExecutionPolicy -Scope LocalMachine RemoteSigned
```

Now, you will be able to create a new virtual environment with:

```bash
virtualenv .\foo
```

Activate it with:

```bash
.\foo\scripts\activate
```

Deactivate with:

```bash
deactivate
```

#### Step 3: Installing Git and GitHub

Git is a version control system you can use to manage your code projects. It powers an easy-to-use online repository system called GitHub, which allows you to track your code contributions and collaborate with others.

Install Git using the installer [here for Mac](https://git-scm.com/download/mac) or [here for PC](https://git-scm.com/download/win) and follow the prompts (you will probably need admin access to do this).

Now, [sign up for GitHub](https://github.com/join).

Now, [follow the instructions on generating SSH keys](https://help.github.com/articles/generating-an-ssh-key/) and adding them to your GitHub account (don't install the desktop client). This will prevent you from having to use passwords to log in to your account from the Terminal or Powershell, allowing you to quickly upload code contributions to your GitHub projects. Start with “Checking for existing SSH keys,” and make sure you select the instructions for Mac or PC (you will probably need admin access to do this).

#### Installing Sublime Text
There are lots of text editors out there, and you’re free to use whichever one you’re comfortable with. I [suggest installing Sublime](https://www.sublimetext.com/) Text (you’ll need admin privileges).

## Lesson 1: Python basics

TK

## Lesson 2: Practical Github

TK

## Lesson 3: Becoming a Twitter developer

TK

## Lesson 4: Working with Python libraries

TK

## Lesson 5: Deploying your app

TK

