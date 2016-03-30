## Lesson 5: Deploying your app

Just for the sake of our own sanity, we normally develop and run code on our local machines, which are faster and wholly within our control.

But if you've got a job or an app that runs regularly, or even constantly, you might ousource that computing powers to __remote servers__. [Amazon Web Service](http://aws.amazon.com/) is one good option, and its servers actually power some of the world's largest websites and apps.

Running code on a server is different than writing code in HTML and CSS. With HTML, CSS and even JavaScript, the code you write and upload to a server just sits there until a user downloads it with their browser, which does all the work intepreting and running the code to display a page. For this reason, code like JavaScript is called __client-side__ scripting.

In our case, we want an external computer to execute our code, just like we're executing our own code with the command ```python tweetgen-template``` -- that's __server-side scripting__.

#### Signing up for AWS

One of the big advantages about AWS is that it's pretty affordable, especially for small projects. [After you sign up](http://aws.amazon.com/), you can choose what products you'd like to use and you'll get charged accordingly.

Typically, you'll use a service called EC2 to "spin up" a server instance. [Follow the directions for how to do that on Amazon's site](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html), which has more detail on how to set up security and other features.

One thing to take note of is where you store your key pair, which is essentially your password for logging onto the server remotely. This will allow you to do all the things on the server via your command line that we did in previous lessons.

#### Accessing the server

```bash
ssh -i KEYLOCATION.pem -l ubuntu -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no IP.ADDRESS.OF.SERVER
```

#### Uploading your code

```bash
pip install -r requirements.txt
```

#### Setting up a cron job