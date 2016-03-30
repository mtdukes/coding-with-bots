## Lesson 4: Working with Python libraries

The Python community is massive, and they've created a seemingly endless supply of libraries to extend the language in a ton of useful directions.

Some libraries, like datetime, come pre-installed with Python, but have to be imported. Others have to be installed, but luckily, that's incredibly easy with pip, which you should have installed in [Step 0](../readme.md).

![Brent's got it.](https://raw.githubusercontent.com/mtdukes/coding-with-bots/master/img/trump-eagle.gif)

#### Harnessing Tweepy

For this workshop, we're going to install the [Tweepy library](http://docs.tweepy.org/en/v3.5.0/), which provides access to the Twitter API through Python scripts.

```bash
pip install tweepy
```

This will install Tweepy and a few other __dependencies__, libraries Tweepy uses to run. It's libraries all the way down!

What's great about working with pip and virtual environments is that you can easily track all the libraries your programs use to run. The command below takes everything you've installed in the virtual environment and saves the specifics to a file called "requirements.txt".

```bash
pip freeze > requirements.txt 
```

That will come in handy later.

#### Building out the template

In the "code_samples" folder of your local directory, open the ```tweetgen-template.py``` in Sublime.

To run the file, enter the following command:

```bash
python tweetgen-template.py
```

Try adding some of your own code to customize the app!

![Brent's got it.](https://raw.githubusercontent.com/mtdukes/coding-with-bots/master/img/were-waiting.gif)

#### Further reading and inspiration

- [Kantaro](https://github.com/mtdukes/kantaro)
- [@WhatsOnWRAL](https://github.com/mtdukes/whatson)
- [Darius Kazemi // Tiny Subversions](http://tinysubversions.com/)

### >>> [Next lesson](./lessonFive.md)