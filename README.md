simple-stopwatch
================

A very simple python3, ncurses based terminal stopwatch.

simple-stopwatch is not designed to be as precisely as possible, but should be
fine for simple tasks like measuring the time during a speech.

Installation
------------

run

    python setup.py install

in the root directory of this repository.

Usage
-----

    $ simple-stopwatch --help
    usage: simple-stopwatch [--hours-always]
                        [--color {black,blue,cyan,green,magenta,red,white,yellow,none}]
                        [--center] [--help]

    Simple ncurses based terminal stopwatch. Press space to pause and q to exit.

    optional arguments:
        --hours-always        display hours always
        --color {black,blue,cyan,green,magenta,red,white,yellow,none}
                              the color to use
        --center              center stopwatch
        --help                show this help message and exit

License
-------

Copyright (C) 2013 Christoph Göttschkes <just dot mychris at googlemail dot com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

