* [Python language reference](https://docs.python.org/2/reference/index.html)
* [Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/) are excellent sources of broad-spectrum information and suggestions, in particular [PEP20, the Zen of Python](https://www.python.org/dev/peps/pep-0020/)
### Python examples

* [Determining last Friday's date](https://github.com/dabeaz/python-cookbook/blob/master/src/3/determining_last_fridays_date/example.py)
* [Parsing and plotting data from a CSV](https://github.com/jvns/pandas-cookbook/blob/master/cookbook/Chapter%201%20-%20Reading%20from%20a%20CSV.ipynb)

* [Analysis of LIGO data from GW150914](https://losc.ligo.org/s/events/GW150914/GW150914_tutorial.html)
* Some [SciPy recipes](http://scipy-cookbook.readthedocs.io/)
 * [Brownian motion](http://scipy-cookbook.readthedocs.io/items/BrownianMotion.html)
 * [Correlated random samples](http://scipy-cookbook.readthedocs.io/items/CorrelatedRandomSamples.html)
 * [Coupled spring-mass system](http://scipy-cookbook.readthedocs.io/items/CoupledSpringMassSystem.html)

### Useful resources
* [Python/numpy/scipy/matplotlib tutorial from Stanford's CS231n](http://cs231n.github.io/python-numpy-tutorial/) (also available as [a notebook](https://github.com/kuleshov/cs228-material/blob/master/tutorials/python/cs228-python-tutorial.ipynb))
* [Anaconda](https://www.continuum.io/downloads) - a utility to manage different Python environments, and packages installed therein
* [Scipy lectures](https://scipy-lectures.github.io/)
* [Google's introductory notes on Python (including video lectures)](https://developers.google.com/edu/python/introduction?pageId=105694254432924708823)

#### Textbooks
* [Think Python](http://greenteapress.com/wp/think-python/)
* [Dive Into Python 3](http://www.diveintopython3.net/)

### Misc.
* Dictionaries are actually implemented a fairly sophisticated structure called a [hash table](https://en.wikipedia.org/wiki/Hash_table).  To better understand this in the context of Python, I recommend [The Mighty Dictionary](https://www.youtube.com/watch?v=C4Kc8xzcA68), an excellent talk by Brandon Craig Rhodes presented at PyCon 2010.

* The `code` module can be very helpful for debugging:
```python
# Drop out to an interactive console, bringing the local environment with us.  Useful for inspecting variables, etc.
import code
code.interact(local=locals())
# Use Ctrl-D to resume normal execution where you left off when you're done!
```
