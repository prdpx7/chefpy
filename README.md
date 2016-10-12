# chefpy
#### Unofficial Codechef API
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/zuck007/chefpy/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/chefpy.svg)](https://badge.fury.io/py/chefpy)
## Installation
  ```
  pip install chefpy
  ```
## Usage
  ```
  $ python
  >>> from chefpy import Chefpy
  >>> user = Chefpy("zuck_007")
  >>> user.content
{u'username': u'Pradeep Khileri',
  'problems': {u'MUFFINS3': 'https://www.codechef.com/status/MUFFINS3,zuck_007', 'TIMEASR':....}
  >>> user.content.keys()
  [u'username', u'problems', u'user', u'rank']
  >>> user.get_stat()
  User  : zuck_007
  Contest : Global/Country Rank
  LongContest : 2347/1735
  ..........
  ```
#### Demo
[![asciicast](https://asciinema.org/a/83814.png)](https://asciinema.org/a/83814)

# Xchefpy

#### Sample Python Script using *chefpy*
## Usage
  ```
  $ Xchefpy --help
  usage: Xchefpy [-h] [--user USER] [--status] [--download DOWNLOAD]
               [--download-all]

  Making Backup for Codechef soultions

  optional arguments:
   -h, --help           show this help message and exit
   --user USER          Display general info
   --status             Get User Full Status eg:
              Xchefpy --user USERNAME --status
   --download DOWNLOAD  Download solution for problemCode eg:
              Xchefpy --user USERNAME --download 'PROBLEMCODE'
   --download-all       Download all solutions eg:
              Xchefpy --user USERNAME --download-all
  $ cd /tmp
  $ Xchefpy --user "zuck__007" --download "WOUT"
  $ ls -l
  .  ..  WOUT.cpp
  ```
#### Demo
[![asciicast](https://asciinema.org/a/83816.png)](https://asciinema.org/a/83816)
