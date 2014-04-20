## Sentech

Projet sentech

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

#### Environnement

 * Install virtualenvwrapper
 ** sudo apt-get install python-pip (source ubuntu/debian)
 ** sudo pip install virtualenvwrapper

 * Configure virtualenvwrapper
 ** add to your bash profile

  ```
    export WORKON_HOME=~/.virtualenvs
    mkdir -p $WORKON_HOME
    source /usr/local/bin/virtualenvwrapper.sh

  ```

  ** Load your bash variable

  ```
    source ~/.bashrc

  ```


#### Sentech plateform

  * clone https://github.com/Sentech/sentech on your workspace projet

  * Activate your virtualenv

  ```
    mkvirtualenv <your-env-name>
    source ~/.virtualenvs/<your-env-name>
    your prompt must begin with `` (your-env-name) ``

  ```

  * Install project requirements

  ```
    cd sentech
    pip install -r requirement.txt
    cp sentech/settings_local.py.sample sentech/settings_local.py
      ** Pour le moment pas besoin de faire des modifications sur settings_local.py
    mkdir db
    touch db/db.sqlite3
    python manage.py syncdb --all

    python manage.py migrate si erreur
    python manage.py migrate --fake

  ```

### Configure your local site


#### Apache

TBD


#### Nginx

TBD

