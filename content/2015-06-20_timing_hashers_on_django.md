title: Timing hashers with Django
date: 2015-06-20 15:43


I've always been interested in the various password hashers available to Django developers, and the recent [disclosure of master password hashes](https://blog.lastpass.com/2015/06/lastpass-security-notice.html/) for LastPass pushed me over the edge.  Now I really wanted to understand how to best protect user password hashes on any Django sites I work on where this might be a concern.

Out of the box, Django supports a [wide range](https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#how-django-stores-passwords) of hashers, but only a few should you [really be using](https://www.nccgroup.trust/us/about-us/newsroom-and-events/blog/2015/march/enough-with-the-salts-updates-on-secure-password-schemes/) — ideally, PBKDF2 with SHA256 (Django default), bcrypt, or scrypt.

Other than whether your platform supports these, the next thing to be concerned about is tuning their work factors to make them as high as possible, without making your users wait long for the hashing on login.  To test this out, I timed them in iPython using ‘[magic functions](http://ipython.org/ipython-doc/dev/interactive/tutorial.html#magic-functions)’.

Here is a test for PBKDF2:

```python

from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.utils.crypto import get_random_string

ph = PBKDF2PasswordHasher()
password = 'this is my password'
salt = get_random_string()

%timeit ph.encode(password, salt, iterations=24000)  # Django default iterations
%timeit ph.encode(password, salt, iterations=100000)  # Something better

```

Here is a test for bcrypt:

```python

import bcrypt
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher

bh = BCryptSHA256PasswordHasher()
password = 'this is my password'

%timeit bh.encode(password, bcrypt.gensalt())  # Default work factor of 12

```

When running these on a single core, 512MB of RAM [Digital Ocean droplet](https://www.digitalocean.com/?refcode=ba6bbd1262c3) I get these results:

|Hash|Time|
|---|---|
|PBKDF2 - 12,000|121 ms|
|PBKDF2 - 100,000|487 ms|
|bcrypt - 12|395 ms|

The takeaway here is that 100,000 iterations will make your user wait another 366 ms - probably not all that bad.  Complete conjecture, but I would bet this is already one of the longest waits in the login process.  Your results certainly will vary so you'll want to confirm the result you are interested in.

As an aside, I haven't tried [scrypt](https://en.wikipedia.org/wiki/Scrypt) since it isn't really supported out of the box with Django.  In theory, that would be the best one to switch to from PBKDF2 as it puts up substantial barriers to massive cracking array scenarios.  Some [libraries](https://pypi.python.org/pypi/scrypt) and [django apps](https://pypi.python.org/pypi/django-scrypt) exist, but they don't inspire a lot of confidence in an area where they really ought to.

In the end, it's probably easiest to just increase the number of iterations of PBKDF2 to a length that is as high as your users will be patient with, since [some](http://www.unlimitednovelty.com/2012/03/dont-use-bcrypt.html) don't seem to like bcrypt very much.

With these changes, keep in mind that this could open you to DOS attacks if you don't have any throttling on your login page.  Something like [fail2ban](https://en.wikipedia.org/wiki/Fail2ban) can help you throttle an IP that is repeatedly failing the login process.  Also don't forget to increase this over time, like [Django does](https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#increasing-the-work-factor).
