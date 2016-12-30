# [chriserickson.me](http://chriserickson.me)

## Introduction
This is the source for [https://chriserickson.me](https://chriserickson.me).  It is built on the [Pelican static blogging engine](http://blog.getpelican.com/).

## Developing
All development can be done locally, without the use of a virtual machine (Vagrant, VirtualBox, VMWare, etc).  For a manual, but simple workflow, you can run any number of fabric commands:

```shell
$ fab rebuild  # Purge old files, rebuild
$ fab build    # Build any changed files
$ fab serve    # Fire up a basic webserver at http://localhost:5000
```

After running ```fab serve```, you will have a webserver running, that you will need to stop manually using <kbd>Ctrl</kbd>-<kbd>C</kbd>.  This needs to be stopped, and ```fab build``` run anytime you make changes.

For something a bit more useful, you can use the ```develop_server.sh``` script.  It has a few options as well:

```shell
$ ./develop_server.sh
# > usage: ./develop_server.sh (stop) (start) (restart) [port]
```

Typically you would run this with ```./develop_server.sh start 5000```.  This watches files for any changes, and should pick them up automatically.  This kicks off the server in the background, so when you're all done, you'll want to stop the server by running ```./develop_server.sh stop```.

### Getting Latest Submodules

```shell
# Source: http://stackoverflow.com/a/5828396/2057885
git submodule foreach git pull origin master
```

## Writing Content

### Contributing Content

Content can be contributed through a typical pull request cycle.  Write something compelling in a branch, create a pull request, then merge it.  Content should be written in [Markdown](http://daringfireball.net/projects/markdown/syntax).

### Directory Structure

- Posts: ```content```
- Pages: ```content/pages```
- Images: ```content/images```

### File Names

Document names are not important to the function of the site, but should be formulated in a helpful manner such as ```YYYY-MM-DD_The-title-of-the-post.md``` to allow for better sorting.

### Types of Content

#### Posts

Posts are used for what is usually considered 'blog' content.  They are typically displayed in a list, sorted by date.  They are kept in the ```content``` directory.  Meta data in the post document itself will be used to generate the site.

Here is an example post:

```Markdown
title: This new thing will knock your socks off
subtitle: What happened to your shoes?
date: 2014-01-30 3:50

Your interesting story starts now.
```

#### Linked Posts

This is a slight variant to a standard post.  Linked posts are used to feature and add to the conversation that was started elsewhere.  Examples of this might be to quote someone whom says important things, or provide direct commentary on the blog post of someone else.  These differ in format only by featuring a ```link``` in the metadata.

Here is an example linked post:

```Markdown
title: This new thing will knock your socks off
subtitle: What happened to your shoes?
date: 2014-01-30 3:50
link: https://www.apple.com

> Your mind is blown with this thing I said.

I think this person is wrong.
```

#### Pages

Pages are generally used for content that falls outside the chronological flow of a typical post.  Examples might include an About page, a page listing various contact methods or other special content.  These are kept in the ```content/pages``` directory.

Here is an example page:

```Markdown
title: About
date: 2014-01-30 3:50
modified: 2014-01-30 3:50

Your content starts here.
```

### Linking to Static Media ###

If you want to include images in a post, you need to use the following syntax (make sure to place the images in the right directory, as indicated above):

```Markdown
![The watch!]({filename}/images/watch.jpg)
```

## Deploying Content

``` shell
cd "/var/www/venvs/chriserickson.me/chriserickson.me"
source "/var/www/venvs/chriserickson.me/bin/activate"
git pull
pip install -r requirements.txt
yarn install
bower install
make publish
```

## Build Instructions

You will need to have [Python 2](http://python.org), [virtualenv](http://www.virtualenv.org/en/latest/) and [Node.js](http://nodejs.org/) installed in your system.

``` shell
# Create a virtualenv
mkvirtualenv chriserickson.me
# Activate virtualenv
source chriserickson.me/bin/activate
# Clone the git repo
git clone git@github.com:chris-erickson/chriserickson.me.git chriserickson.me
cd chriserickson.me
# Install Python Requirements
pip install -r requirements.txt
# Install Bower static files
bower install # May need ./node_modules/.bin/bower install if node_modules isn't in PATH
# Development build
pelican -s pelicanconf.py
# or Production build
pelican -s publishconf.py
```

## Preparing the Server

Configure a user:

``` shell
sudo useradd -d /home/pelican-blog -m pelican-blog
sudo passwd pelican-blog
```

Configure a virtual environment:

``` shell
cd /var/www/venvs/
virtualenv ./chriserickson.me
sudo chown -R pelican-blog:pelican-blog chriserickson.me
source chriserickson.me/bin/activate
```

Create an ssh key (for GitHub):

``` shell
sudo su - pelican-blog
ssh-keygen -t rsa -C "id_rsa"
```

Fetch the site files from GitHub:

``` shell
cd /var/www/venvs/chriserickson.me/
git clone https://github.com/chris-erickson/chriserickson.me
git pull && git submodule init && git submodule update && git submodule status
```

Install python dependencies:

``` shell
pip install -r requirements.txt
```

Install node dependencies:

``` shell
yarn install
```

Install Bower dependencies:

``` shell
# Depends on yarn install
bower install
```
