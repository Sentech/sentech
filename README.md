## Sentech

Project sentech

To breathe new life into the Senegalese tech community (RIP DakarLUG),
we're building the sentech.cc website in the open, based on Django.

We don't know where it will lead us, and we can use all the help we can get,
so join us!

### Features

  * blog/news.
  * community events.
  * forum.


### Requirements

You just need ``python``, ``python-dev``, ``virtualenvwrapper``, ``pip``  and ``git`` installed on your system.


### Installation

#### Environment

 * Install virtualenvwrapper

  ``` 
    $ sudo apt-get install python-pip (source ubuntu/debian)
    $ sudo pip install virtualenvwrapper
  ```

 * Configure virtualenvwrapper
 ** add to your bash profile

  ```
    $ export WORKON_HOME=~/.virtualenvs
    $ mkdir -p $WORKON_HOME
    $ source /usr/local/bin/virtualenvwrapper.sh

  ```

 * Reload your bash variables

  ```
    $ source ~/.bashrc
  ```


#### Sentech platform

  * Activate your virtualenv (for instance, name it sentech)

  ```
    $ mkvirtualenv sentech
    
    # your prompt now indicates the active virtual env  `` (sentech) ``
    (sentech) $ 
  ```

  * Install project requirements

  ```
    (sentech) $ cd sentech
    # you're now inside the overall sentech virtualenv directory
    
    # install the dependencies
    (sentech) $ pip install -r requirement.txt
    
    # clone the sentech project from github
    (sentech) $ git clone https://github.com/Sentech/sentech
    
    # go into your cloned sentech project
    (sentech) $ cd sentech
    
    # set up a local settings file that won't be committed to the repo
    (sentech) $ cp settings_local.py.sample settings_local.py
   
    # set up a sqlite3 db
    (sentech) $ mkdir db
    (sentech) $ touch db/db.sqlite3
    (sentech) $ python manage.py syncdb --all

    # in case you got an error setting up the db:
    (sentech) $ python manage.py migrate
    (sentech) $ python manage.py migrate --fake

  ```

### Configure your local site


#### Apache

TBD


#### Nginx

TBD

