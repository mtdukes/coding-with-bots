## Lesson 3: Becoming a Twitter developer

Twitter provides [a powerful API](https://dev.twitter.com/) for accessing its platform and building cool stuff, but you have to have an account and be signed up as a developer.

To do that, begin by registering [a brand new Twitter account](https://twitter.com).

When your new account is created, make sure you're logged in and go to Twitter's developer site. At the bottom of the page, click on "Manage Your Apps."

Click "Create New App" button, fill out the required fields and agree to the terms and conditions to create your new app.

Under "Keys and Access Tokens" take note of the following:

- Consumer Key (API Key)
- Consumer Secret (API Secret)

You'll also need to generate two other codes:

- Access Token
- Access Token Secret

These essentially allow your app to access the Twitter API outside the browser.

In Sublime, start a new file and copy each of these codes to the new file, one per line. Save the file with the filename ".keys". Click "Use ." when the system prompts you. We're storing these in hidden files and ignoring them in GitHub so they won't accidentally get uploaded when we commit our code publicly.

Our app will still have access, which we'll talk about in the next step.

But for now, congratulations, you're a Twitter developer!

![Brent's got it.](https://raw.githubusercontent.com/mtdukes/coding-with-bots/master/img/now-what.gif)

### >>> [Next lesson](./lessonFour.md)