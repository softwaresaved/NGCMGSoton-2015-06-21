---
layout: page
title: Version Control with Git
subtitle: Collaborating
minutes: 55
---
> ## Learning Objectives {.objectives}
>
> *   Explain what remote repositories are and why they are useful.
> *   Explain what happens when a remote repository is cloned.
> *   Explain what happens when changes are pushed to or pulled from a remote repository.

We've seen how Version control can help us track the changes we make to our files, and to revisit any point in their history.

**(SLIDE 17 - Git Workflow - Local Repo)**

Version control really comes into its own
when we begin to collaborate with other people.

**(SLIDE 18 - Collaboration)**

###The missing link###
We already have most of the machinery we need to do this;
the only thing missing is to copy changes from one repository to another.

Systems like Git allow us to move work between any two repositories.

In practice,
though, it's easiest to use one copy as a central hub,
and to keep it on the web rather than on someone's laptop.

Many programmers use hosting services like GitHub or BitBucket
to hold those master copies;  we'll explore the pros and cons of these a bit later.  

###Exploring the collaborative process###

But first let's explore the collaborative process, with a contrived example - Collaborating with ourselves.

**(SLIDE 19 - Remote Repositories)**

Earlier on we created two directories - laptop and desktop.  So far we have been working in laptop.  Let's use GitHub to set up a remote repository and start **"collaborating"** with our desktop - this could of course be another dev 

###To GitHub###
Let's start by sharing the changes we've made to our current project with the world.
Log in to GitHub,
then click on the icon in the top right corner to create a new repository called `planets`:

![Creating a Repository on GitHub (Step 1)](img/github-create-repo-01.png)

Name your repository "planets" and then click "Create Repository":

![Creating a Repository on GitHub (Step 2)](img/github-create-repo-02.png)

As soon as the repository is created,
GitHub displays a page with a URL and some information on how to configure your local repository:

![Creating a Repository on GitHub (Step 3)](img/github-create-repo-03.png)

This effectively does the following on GitHub's servers:

~~~ {.bash}
$ mkdir planets
$ cd planets
$ git init
~~~

**(SLIDE 19 - Remote Repositories)**
**(SLIDE 20 - Remote Repositories)**

###Connecting the remote repository###

Our local repository still contains our earlier work on `mars.txt`,
but the remote repository on GitHub doesn't contain any files yet:

The next step is to connect the two repositories.

We do this by making the GitHub repository a [remote](reference.html#remote)
for the local repository.  A **remote** is a repository conected to another in such way that both can be kept in sync exchanging commits.

The home page of the repository on GitHub includes
the string we need to identify it:

![Where to Find Repository URL on GitHub](img/github-find-repo-string.png)

Copy that URL from the browser,
go into the local `planets` repository,
and run this command:

~~~ {.bash}
$ git remote add origin https://github.com/vlad/planets.git
~~~

The name `origin` is a local nickname for your remote repository:
we could use something else if we wanted to,
but `origin` is conventional.

Make sure to use the URL for your repository rather than Vlad's:
the only difference should be your username instead of `vlad`.

We can check that the command has worked by running `git remote -v`:

~~~ {.bash}
$ git remote -v
~~~
~~~ {.output}
origin   https://github.com/vlad/planets.git (push)
origin   https://github.com/vlad/planets.git (fetch)
~~~

###Push commits from local to remote###

Once the remote is set up, we can **push** the changes from our local repository
to the repository on GitHub:

~~~ {.bash}
$ git push origin master
~~~
~~~ {.output}
Counting objects: 9, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (9/9), 821 bytes, done.
Total 9 (delta 2), reused 0 (delta 0)
To https://github.com/vlad/planets
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
~~~
The push command takes two arguments, the remote name ('origin') and a branch name ('master').

We haven't yet discussed **branching** yet, and we won't have time to do so today.

But this is a feature common
to almost all version control systems and gives you the ability to diverge from the main line of development
and to continue to do work without messing with that main line.  The main (default) branch is the master.

At a later time you can re-integrate branches to the master.

Our local and remote repositories are now in sync.

###Testing Pull###

We can pull changes from the remote repository to the local one as well:

~~~ {.bash}
$ git pull origin master
~~~
~~~ {.output}
From https://github.com/vlad/planets
 * branch            master     -> FETCH_HEAD
Already up-to-date.
~~~

Pulling has no effect in this case
because the two repositories are already synchronized.
If someone else had pushed some changes to the repository on GitHub,
though, this command would download them to our local repository.

###Cloning the desktop###

Now lets look at collaboration.  In this case it's with ourselves - on laptop and desktop, 
but the principal, is the same.

~~~ {.bash}
$ cd ../../dtop
$ git clone https://github.com/vlad/planets.git
~~~

`git clone` creates a fresh local copy of a remote repository.

![After Creating Clone of Repository](img/github-collaboration.svg)

You can now start work on your desktop machine:

~~~ {.bash}
$ cd planets
$ nano pluto.txt
$ cat pluto.txt
~~~
~~~ {.output}
It is so a planet!
~~~
~~~ {.bash}
$ git add pluto.txt
$ git commit -m "Some notes about Pluto"
~~~
~~~ {.output}
 1 file changed, 1 insertion(+)
 create mode 100644 pluto.txt
~~~

then push the change to GitHub:

~~~ {.bash}
$ git push origin master
~~~
~~~ {.output}
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 306 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/vlad/planets.git
   9272da5..29aba7c  master -> master
~~~

Note that we didn't have to create a remote called `origin`:
Git does this automatically,
using that name,
when we clone a repository.
(This is why `origin` was a sensible choice earlier
when we were setting up remotes by hand.)

We can now download changes into the original repository on our machine:

~~~ {.bash}
cd ../../ltop
$ git pull origin master
~~~
~~~ {.output}
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0)
Unpacking objects: 100% (3/3), done.
From https://github.com/vlad/planets
 * branch            master     -> FETCH_HEAD
Updating 9272da5..29aba7c
Fast-forward
 pluto.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 pluto.txt
~~~

**(SLIDE 21 - Git Workflow Remote Repositories)**

###Wrap up###

So, we've seen how we can use remote git repos to collaborate (with ourselves).


For more for info see the Software Carpentry site:
**(SLIDE 22 - What next)**

That about wraps up what we can fit into this session, but you'll probably want to explore what happens when your commits conflict - **merging** and how to use development **branches**.



We'll leave questions until the Q&A session

