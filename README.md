# font-awesome-3-to-4

**A Python utility for upgrading HTML font awesome classes from v3.2 to v4.0**

Author: Robert Clarke <rob@redanorak.co.uk>

Contributor: Bryan Keiren <contact@bryankeiren.com>

## Introduction

A simple utility designed to automate the process of upgrading your HTML files or templates from font awesome 3.2 to 4.0. Modifies class names and class structure as per the [official instructions](https://github.com/FortAwesome/Font-Awesome/wiki/Upgrading-from-3.2.1-to-4).

## Installation and Dependencies

You can just download these files to any box running python 2.7. There are no dependencies beyond the core python distribution.

font-awesome-3-to-4 depends on the HTMLParser module which has been renamed in Python 3, so this version will only run in python 2. It's been tested on Ubuntu 13.04 but should run fine on Windows or any other popular OS

## Usage

It's easiest to use the provided script to run the converter. The script accepts one or more html file paths as its arguments, parses the HTML within the files and overwrites the files.

```
$ python fa3tofa4.py ~/website/index.html
```

The script accepts one or more html file paths as it's arguments, parses the html within the files and overwrites the files. If you're feeling very confident you can feed it a list of all your html files using xargs or similar. Obviously exercise some caution when doing that!

Alternatively you can fire up a shell in the source directory and talk directly to the parser

```
>>> from fontawesomeupgrader import FontAwesomeUpgrader
>>> fa_upgrader = FontAwesomeUpgrader()
>>> fa_upgrader.process_html('hello<div><i class="icon-check"></i>')
```

## What does it do?

font-awesome-3-to-4 is an HTML parser which looks for font-awesome 3.2 classes and converts where possible to font-awesome 4.0, automating the conversion procedure described by the official docs. It checks for i, ul or span elements and maps font awesome classes to newer ones. 

Because this is based on a proper HTML Parser (the one that comes with python) it is in theory less likely to cause damage than a regex based solution. The parser is very flexible and tolerant of bad or incomplete HTML, and is often capable of handling HTML templates with other languages embedded. 

font-awesome-3-to-4 has been tested on a large batch of Django templates with positive results

## Known limitations

* stacked icons required some manual interventation for a succesful migration - see the font awesome docs for their implementation in fa 4.x
* icon classes referenced in CSS or JavaScript will not be parsed, you'll need to fix those yourself

## Todo

* Check it works ok with various character encodings
* Possibly break out HTMLFixerBase into separate project for future HTML maintenace chores

## License

```
Copyright 2013 Robert Clarke

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
