# chefpy
#### Unofficial Codechef API
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
  
# Xchefpy
  
#### Python Script to download  User's Solution using *chefpy*
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
  * Here is snap of my full Backup of all ACed Solution from [CodeChef](https://www.codechef.com/users/zuck_007) using this API
  ![snap](http://i.imgur.com/ACpkMfz.png)
