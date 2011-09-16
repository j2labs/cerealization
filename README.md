# Cerealization

Hey folks, this is just your every day, normal, do-it-yourself kinda home
serailization speed testing tool kit.  Just clone the repo, install any
necessary requirements and run just 1 (that's right, just 1!) command to
git-r-done.

So what we got here is a python script that runs multiple types of
serialization.  It knows how to do json in like five diffr'nt which ways.
And it knows how to do some pickled output too.  (Them suckers taste DELICIOUS).
But it also knows how to do tnetstring's too.

If you don't know about tnetstrings just send your internet location to
[tnetstring.org](http://tnetstring.org/) and give it a look or two.


## Act Now!

Now, I'm gonna tell you just how we do it in a moment...  But first! I want to
let you know about a limited time offer.

I'm just so excited about this!

Right now, for a limited time, I'm gonna give you not just one, but TWO (!)
serialization files.  The first one is the speed testing Python code, just like
we discussed, but the second code file adds some Node.js to the experience!

You too (!) can see that Python's ultrajson and Ryan Kelly and Zed Shaw's
tnetstring serialization is faster than Node.js.  GIT R DONE!


# Real Results!

Now, these results are for multiple Python techniques of serialization, but
keep an eye out for `ujson` and `tnetstring`.

    $ python cereal.py 
    Dumping:
      json: 5.98301100731
      simplejson: 6.78803396225
      cjson: 2.19402098656
      ujson: 0.719541072845
      cPickle: 6.73631691933
      tnetstrings: 20.1821420193
      tnetstring: 0.82697892189
    Loading:
      json: 8.23215007782
      simplejson: 3.65900611877
      cjson: 1.69663691521
      ujson: 1.13573312759
      cPickle: 3.0421769619
      tnetstrings: 29.0939230919
      tnetstring: 0.711443185806

Here is how Node.js did.  I threw in `eval()` but I think it'd be a mighty 
unwise kinda choice to actually use it.

    $ node cereal.js 
    Dumping:
      JSON: 2.023
    Loading:
      JSON: 1.885
      eval(): 24.516


# Gitting R Done At Home

You just gotta git this here repo on your computer or your laptop or what have
you and then...  Go on now.

    $ cd ~/Desktop/
    $ git clone https://github.com/j2labs/cerealization.git
    $ cd cerealization

OK.  Now for folks still following along with me at home, just install them
Python requirements like this here.  I recommend using a virtualenv if you got
'em.

    $ pip install -I -r ./py.reqs

And maybe you still gotta install Node.js.  Well, they can describe how that's
done better than myself: [Installing Node.js](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) 

Alright! Let's do this!

    $ python cereal.py
    ...

    $ node cereal.js
    ...
