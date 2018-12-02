# Twitter Stream Search

Searching twitter stream with filter for required tweet.

Installation
===
Before installation, my preference way of running this process is from virtual environment. So steps for running this project is based on virtual environment

From source
```
$ git clone https://github.com/bunkdeath/TwitterStreamSearch.git

$ cd TwitterStreamSearch
```

Before creating virtual environment make sure virtualenv is installed. Execute following code to install virtual environment.

```
$ pip install virtualenv
```

Based upon your permission, you might want to run above command using sudo permission.


Create new virtualenvironment and activate it.

```
$ virtualenv env
$ source env/bin/activate
```

Install project dependencies from requirements.txt file

```
$ pip install -r requirements.txt
```

Generate Twitter Tokens
===
To generate tokens you must create Twitter Developer Account and create app from link below.

https://developer.twitter.com/en/apps/create

Extract keys and token from the created app.

Put key,token ans secrets on the respective values of ```config.py``` file.

Running Search
===

You can search for multiple filters at once. open ```stream.py``` file and update line ```myStream.filter(track=[''])``` by placing any required string on ```track``` parameter.

Example: if you want to search stream related to football update code as

```myStream.filter(track=['football'])```

After updating filter, to execute the program perform following command

```
$ python stream.py
```

To stop the program press ```Control + c```

Enjoy your result stream.