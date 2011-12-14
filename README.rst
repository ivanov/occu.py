.. image:: http://pirsquared.org/images/occu.py.pi.jpg

This contains the code of the sign I used at the West Coast Port Shutdown in
Oakland. Here are some pictures:  `1`_ (`mirror 1`_), `2`_ (`mirror 2`_),
`3`_ (`mirror 3`_).

.. _1: http://twitpic.com/7siffc
.. _2: http://yfrog.com/nwsd4ehj
.. _3: http://oaklandnorth.net/2011/12/13/protesters-disrupt-early-morning-shift-at-port-of-oakland/
.. _mirror 1: http://pirsquared.org/images/occu.py.jpg
.. _mirror 2: http://pirsquared.org/images/occu.py2.jpg
.. _mirror 3: http://pirsquared.org/images/occu.py.pi.jpg

The poster contained this code ::

    #!/usr/bin/python
    from UCB import occupyCal
    from Oakland import Port

    for member in OccupyCal:
        member.marchTo(Port)

However, folks on  `Reddit`_ (rightfully) criticized it for not being PEP-8 compliant.

.. _Reddit: http://www.reddit.com/r/programming/comments/nardl/occupy

.. image:: http://pirsquared.org/images/occu.py.jpg
