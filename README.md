Prefect Demo for the Evening of Python Coding
=============================================

This repository demonstrates a simple use case of [prefect](https://www.prefect.io/) for the [evening of python coding](https://github.com/Jacob-Barhak/EveningOfPythonCoding)


INSTALLATION & DEPENDENCIES:
----------------------------
To install:
1. Copy the files in this repository to a directory of choice
2. Install Anaconda from https://www.anaconda.com/download/
3. install prefect: `conda install -c conda-forge prefect`



It is recommended you use Anaconda, yet other python environments should work as well
Tested on Windows 10 Python 3.8.5 with prefect 0.15.1 . See requirements.txt for more details.



USAGE:
------

python PrefectDemo.py <number to count to> <numbers per file>
* for <number to count to>  numbers break into prime divisors or indicate as prime save as several files each with <numbers per file> numbers in the file. Do some calculations in parallel.


EXAMPLES:
---------

### Basic use:
python PrefectDemo.py 
The program will generate 4 files with 5000 numbers each broken into prime components or indicated as prime

### Advanced use:
python PrefectDemo.py 100 50
* for 100 numbers break into prime divisors or indicate as prime save as 2 files each with 50 numbers per file
* for even more advanced use uncomment some of the `@task` decorators in the code to see the effect 


FILES:
------
* PrefectDemo.py : Demo python file
* Readme.md : The file that you are reading now
* requirements.txt - The lst of dependent libraries


DEVELOPER CONTACT INFO:
-----------------------

Please pass questions to:

Jacob Barhak Ph.D.
jacob.barhak@gmail.com
https://sites.google.com/view/jacob-barhak/home


LICENSE
-------
<a rel="license" href="http://creativecommons.org/publicdomain/zero/1.0/"> <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />  </a>

To the extent possible under law, Jacob Barhak has waived all copyright and 
related or neighboring rights to Prefect Demo for the Evening of Python Coding
This work is published from: United States.
