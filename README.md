This project is developing code for the automated analysis of the text of Web standards, particularly Technical Reports published by the W3C, as part of a larger research project studying privacy in technical standard-setting.

For more information, if you want to use these tools or collaborate on their development, please [contact Nick Doty](mailto:npdoty@ischool.berkeley.edu).

[Some basic graphs produced with this code are available online.](https://npdoty.name/tr-analysis/graphs/)

## Usage

Scripts are neither parameterized nor user friendly. Current usage pattern:

* `python fetch.py` downloads TRs into an `archives` directory (not checked in to the repository)
* `python search.py` will create a file `tr-search.json` with the section titles and lengths for every available RFC

The `graphs` directory contains d3 histograms of published reports.

## See also

* [BigBang](https://github.com/datactive/bigbang/), a toolkit for studying communications data from collaborative projects
* [rfc-analysis](https://github.com/npdoty/rfc-analysis), a set of scripts for analyzing IETF RFCs
* [IETF docstats](http://www.arkko.com/tools/docstats.html), some running statistics on IETF documents, especially authorship information