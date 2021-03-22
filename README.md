# Finding registrar country from a URL

## Setup
First, create an account at [IPInfo](https://ipinfo.io). Add your API access token to the `.env` file.

Paste your list of contacts into the `input.csv` file. The following columns are available (feel free to add or remove as you wish, but you may need to edit the `main.py` script).

## Installing dependencies
```
// Clone this repo and cd into it
$ git clone
$ cd country-lookup

// Check if you have pipenv installed. 
$ which pipenv
/usr/local/bin/pipenv

// If not:
$ pipx install pipenv

// Then, in the project directory, install dependencies:
$ pipenv install

```

## Run the program
```
$ python3 main.py
```

## Changing the target country
Just pass the two digit country code as an unnamed argument:
```
$ python 3 main.py ar
```
[Two-letter country codes from IBAN](https://www.iban.com/country-codes)

You'll find the list of US registered domains in `output.csv`.
