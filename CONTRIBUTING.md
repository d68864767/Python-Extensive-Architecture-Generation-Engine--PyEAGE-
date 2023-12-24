# Contributing to Python Extensive Architecture Generation Engine (PyEAGE)

First off, thank you for considering contributing to PyEAGE. It's people like you that make PyEAGE such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make sure to open an Issue on our GitHub repository. We appreciate all the help we can get, even if it's just a typo.

## Fork & create a branch

If this is something you think you can fix, then fork PyEAGE and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```shell
git checkout -b 325-add-japanese-localisation
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.

## Get the code

The first thing you'll need to do is get our code onto your machine. Firstly you'll need to fork the repository and then clone your fork.

```shell
git clone https://github.com/your-username/PyEAGE.git
```

## Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with the latest PyEAGE master branch:

```shell
git remote add upstream https://github.com/original-owner-username/PyEAGE.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master and push it!

```shell
git checkout 325-add-japanese-localisation
git rebase master
git push --set-upstream origin 325-add-japanese-localisation
```

Go to the PyEAGE repository and press the "Compare & pull request" button.

## Wait for the review

Now the request is created, please wait for the review. We will get back to you as soon as we can.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/). By participating in this project you agree to abide by its terms.

## License

By contributing your code, you agree to license your contribution under the [MIT License](LICENSE).

Thank you for your contribution, you're awesome!
