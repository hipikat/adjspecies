=================
adjective/species
=================

The ``adjspecies`` Python module generates random names formed from
an animal and a descriptor.

Installation
============

.. code:: bash

    $ pip install -U adjspecies

Usage
=====

From the command line
---------------------

.. code:: bash

    $ python adjspecies.py -h
    usage: adjspecies.py [-h] [--maxlen MAXLEN] [--sep SEPARATOR] [--count COUNT]
                         [--prevent-stutter]
    
    Print the name of a random adjective/species, more or less…
    
    optional arguments:
      -h, --help         show this help message and exit
      --maxlen MAXLEN    Maximum length for the name, excluding any separator.
                         (default=8)
      --sep SEPARATOR    Separator between the adjective and species words.
                         (default='')
      --count COUNT      Number of adjective/species combinations to print.
      --prevent-stutter  Prevent the same letter from appearing on an
                         adjective/species boundary. (default=True)

    $ python adjspecies.py --count 4
    sillyfox
    redpig
    pinkdoge
    lynxpaw
    
In Python code
--------------

.. code:: python

    >>> import adjspecies
    >>> help(adjspecies.random_adjspecies)
    Help on function random_adjspecies in module adjspecies:
    
    random_adjspecies(sep='', maxlen=8, prevent_stutter=True)
        Return a random adjective/species, separated by `sep`. The keyword
        arguments `maxlen` and `prevent_stutter` are the same as for
        `random_adjspecies_pair`, but note that the maximum length argument is
        not affected by the separator.
    
    >>> adjspecies.random_adjspecies('.', 7)
    'wolf.toy'

About
=====

While writing a deployment system targetting DigitalOcean_ Droplets,
the author found the largest bottleneck was finding names for the transient
test servers.

The adjective/species contrivance comes from the furry culture in general
and more directly from the site `[adjective][species]`_. It provides a
wide namespace of easy-to-remember randomness.

Everything up until the initial commit was an exercise in yak shaving and
procrastinating getting out of bed.

.. _DigitalOcean: https://www.digitalocean.com/
.. _[adjective][species]: http://adjectivespecies.com/


Credits
=======

The `adjspecies` module is written and maintained by `Adam Wright`_,
who plays a cheetah on Twitter under the guise of `@chipikat`_, a Python
developer called `@pypikat`_ and a human being named `@hipikat`_.

.. _Adam Wright: http://hipikat.org/
.. _@chipikat: https://twitter.com/chipikat
.. _@pypikat: https://twitter.com/pypikat
.. _@hipikat: https://twitter.com/hipikat
