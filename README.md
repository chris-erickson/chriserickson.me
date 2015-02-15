# [chriserickson.me](http://chriserickson.me)

## Writing Content

## Deploying Content

## Build Instructions

You will need to have [Python 2](http://python.org), [virtualenv](http://www.virtualenv.org/en/latest/) and [Node.js](http://nodejs.org/) installed in your system.

``` shell
# Create a virtualenv
mkvirtualenv chriserickson.me
# Activate virtualenv
source chriserickson.me/bin/activate
# Clone the git repo
git clone git://github.com/alefteris/thanoslefteris.com.git chriserickson.me
cd chriserickson.me
# Install Python Requirements
pip install -r requirements.txt
# Install Bower static files
bower install
# Development build
pelican -s pelicanconf.py
# or Production build
pelican -s publishconf.py
```
