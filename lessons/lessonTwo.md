## Lesson 2: Practical Github

GitHub provides a suite of tools for project management, collaboration and version control, but we'll just dip into the basics here.

A __repository__, or __repo__ is basically just a directory. It's often shorthand for the general storage location of a specific project.

By __forking__ a repo, we're making a copy for ourselves, which allows us to make our own changes or contribute to a project. In the top right corner of this repo, click __Fork__. This will make a copy of the repo on your own GitHub account.

But we don't have it on our local machines quite yet. That requires __cloning__.

To __clone__ a repo, we're just going to download it and store it locally, say if we just want to run some code on our own machines. Go to your fork and copy the clone URL.

```bash
git clone https://github.com/YOUR-USERNAME/coding-with-bots.git
```

Now, if you ```ls```, you should see a new directory called coding-with-bots, filled with all the files from this very repo. Get excited!

![Brent's got it.](https://raw.githubusercontent.com/mtdukes/coding-with-bots/master/img/andy-excite.gif)

#### Managing versions

But we also need to tell git that we want it to sync to the original repo, in case there are changes we need to get. In the coding-with-bots directory enter the following command to show the current remote repository for the fork on your local machine.

```bash
git remote -v
```

We're going to add to this list, by adding an __upstream__ repository.

```bash
git remote add upstream https://github.com/mtdukes/coding-with-bots.git
```

Now ```git remote -v``` again and you'll see the addition.

We're going to create a __branch__ of the main project, because you're going to code a custom bot and we want to keep our changes separate from the main branch.

```bash
git checkout -b YOURNAME-branch
```

You can switch back to the main branch at any time with:

```bash
git checkout master
```

Check your current branch with:

```bash
git status
```

![Brent's got it.](https://raw.githubusercontent.com/mtdukes/coding-with-bots/master/img/logical.gif)

#### The Git model

Git follows a production model for code meaning changes move like so:

untracked -> modified -> staged -> committed

Any changes you make are untracked (and you'll see this represented when you use the ```status``` command), and you can move them to staged with the following command:

```bash
git add FILE_NAME
```

You can also quickly add everything in your project with ```git add .```

Commit the changes with a commit message -- something short and descriptive about the change.

```bash
git commit -m "YOURNAME's first commit"
```

Push your changes to YOUR branch with:

```bash
git push origin YOURNAME-branch
```

When you go back to GitHub in your browser, you can submit a __pull request__ to the project manager, which will allow him or her to incorporate your changes into the main repository.

To make sure you've got the most updated version of the project, make sure you're in the master branch and use the __pull command.

```bash
git checkout master
git pull
```

This command becomes extremely useful later if we're deploying changes to a server.

Of course, this is all much more simple if you're [starting your own repo](https://help.github.com/articles/create-a-repo/), but things are better as part of a team, right?

![Brent's got it.](https://raw.githubusercontent.com/mtdukes/coding-with-bots/master/img/nasa_cheer.gif)

#### Further reading

- [GitHub for beginners](http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1#awesm=%7Eoxo1ZxMiZHjClD)
- [How to use GitHub and Terminal](https://18f.gsa.gov/2015/03/03/how-to-use-github-and-the-terminal-a-guide/)

### >>> [Next lesson](./lessonThree.md)