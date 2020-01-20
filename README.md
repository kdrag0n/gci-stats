# Google Code-in Stats

This is a simple stats fetcher for Google Code-in. It currently tracks the number of tasks completed within each organization and can save the data to a Graphite database.

## Installation

To install the dependencies:

```bash
pip3 install -Ur requirements.txt
```

**Python 3.6** or newer is required.

## Usage

No arguments are required to print a simple report to the console:

```bash
python get_stats.py
```

The data can also be sent to a Graphite-compatible database server by specifying the address of the server as an argument:

```bash
python get_stats.py 10.0.2.1
```

Example output:
```
Fedora Project: 2488
FOSSASIA: 2164
OpenWISP: 1871
Liquid Galaxy project: 1414
TensorFlow: 1286
SCoRe Lab: 1204
OSGeo: 942
CCExtractor Development: 912
OpenMRS: 859
Wikimedia: 690
JBoss Community: 685
The Julia Programming Language: 656
Open Roberta: 547
Sugar Labs: 547
BRL-CAD: 454
Systers, an AnitaB.org community: 445
MetaBrainz Foundation: 419
The Mifos Initiative: 389
Haiku: 288
The ns-3 Network Simulator Project: 277
Drupal: 262
Public Lab: 232
Australian Open Source Software Innovation and Education: 197
The Terasology Foundation: 197
R Project for Statistical Computing: 181
CircuitVerse.org: 177
Apertium: 154
Copyleft Games: 110
CloudCV: 100
```
