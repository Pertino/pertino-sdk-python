Welcome to Pertino Python SDK
=============================

To use
######
	include file here

To Build
########
.. code::
	ant env
	ant init
	ant package

To run unit tests
#################
	ant test

To run acceptance test
######################

	Create a file with your Pertino credentials (see acceptance/conftest.py for format/name)

	ant acceptance
	
	
testing reST blocks


.. code-block::

  @a = "using code-block"
  puts @a


.. code-block:: ruby

  @a = "using code-block ruby"
  puts @a


.. code::

  @a = "using code"
  puts @a


.. code:: ruby

  @a = "using code ruby"
  puts @a


::

  @a = "using literal block (no syntax sugar)"
  puts @a


- http://sphinx.pocoo.org/markup/code.html#line-numbers
- http://sphinx.pocoo.org/rest.html#source-code
- http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#literal-blocks