
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"http://imgur.com/1ZcRyrc.png\" style=\"float: left; margin: 20px; height: 55px\">\n",
    "\n",
    "## Lab: Cleaning Rock Song Data\n",
    "\n",
    "_Authors: Dave Yerrington (SF)_\n",
    "\n",
    "---\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np \n",
    "import seaborn as sns\n",
    "\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Load `rock.csv` and do an initial examination of its data columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "rockfile = \"../datasets/rock.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Song Clean</th>\n",
       "      <th>ARTIST CLEAN</th>\n",
       "      <th>Release Year</th>\n",
       "      <th>COMBINED</th>\n",
       "      <th>First?</th>\n",
       "      <th>Year?</th>\n",
       "      <th>PlayCount</th>\n",
       "      <th>F*G</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Caught Up in You</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1982</td>\n",
       "      <td>Caught Up in You by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>82</td>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fantasy Girl</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Fantasy Girl by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Hold On Loosely</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1981</td>\n",
       "      <td>Hold On Loosely by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rockin' Into the Night</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1980</td>\n",
       "      <td>Rockin' Into the Night by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Art For Arts Sake</td>\n",
       "      <td>10cc</td>\n",
       "      <td>1975</td>\n",
       "      <td>Art For Arts Sake by 10cc</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Song Clean ARTIST CLEAN Release Year  \\\n",
       "0        Caught Up in You  .38 Special         1982   \n",
       "1            Fantasy Girl  .38 Special          NaN   \n",
       "2         Hold On Loosely  .38 Special         1981   \n",
       "3  Rockin' Into the Night  .38 Special         1980   \n",
       "4       Art For Arts Sake         10cc         1975   \n",
       "\n",
       "                                COMBINED  First?  Year?  PlayCount  F*G  \n",
       "0        Caught Up in You by .38 Special       1      1         82   82  \n",
       "1            Fantasy Girl by .38 Special       1      0          3    0  \n",
       "2         Hold On Loosely by .38 Special       1      1         85   85  \n",
       "3  Rockin' Into the Night by .38 Special       1      1         18   18  \n",
       "4              Art For Arts Sake by 10cc       1      1          1    1  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Load the data.\n",
    "df = pd.read_csv(rockfile)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2230 entries, 0 to 2229\n",
      "Data columns (total 8 columns):\n",
      "Song Clean      2230 non-null object\n",
      "ARTIST CLEAN    2230 non-null object\n",
      "Release Year    1653 non-null object\n",
      "COMBINED        2230 non-null object\n",
      "First?          2230 non-null int64\n",
      "Year?           2230 non-null int64\n",
      "PlayCount       2230 non-null int64\n",
      "F*G             2230 non-null int64\n",
      "dtypes: int64(4), object(4)\n",
      "memory usage: 139.5+ KB\n"
     ]
    }
   ],
   "source": [
    "# Look at the information regarding its columns.\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2.  Clean up the column names.\n",
    "\n",
    "Let's clean up the column names. There are two ways we can accomplish this:\n",
    "\n",
    "#### 2.A Change the column names when you import the data using `pd.read_csv()`.\n",
    "\n",
    "Notice that, when passing `names=[..A LIST OF STRING..]` with a number of columns that matches the number of strings in the passed list, you replace the column names.\n",
    "\n",
    "NOTE: When you create custom column names, the first row of the `.csv` already represents a header. It is important to tell `pandas` to skip that row. The `skiprows=1` keyword argument to `read_csv()` will tell `pandas` to skip the first row."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>song</th>\n",
       "      <th>artist</th>\n",
       "      <th>release</th>\n",
       "      <th>song_artist</th>\n",
       "      <th>first</th>\n",
       "      <th>year</th>\n",
       "      <th>playcount</th>\n",
       "      <th>fg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Caught Up in You</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1982</td>\n",
       "      <td>Caught Up in You by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>82</td>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fantasy Girl</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Fantasy Girl by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Hold On Loosely</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1981</td>\n",
       "      <td>Hold On Loosely by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rockin' Into the Night</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1980</td>\n",
       "      <td>Rockin' Into the Night by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Art For Arts Sake</td>\n",
       "      <td>10cc</td>\n",
       "      <td>1975</td>\n",
       "      <td>Art For Arts Sake by 10cc</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     song       artist release  \\\n",
       "0        Caught Up in You  .38 Special    1982   \n",
       "1            Fantasy Girl  .38 Special     NaN   \n",
       "2         Hold On Loosely  .38 Special    1981   \n",
       "3  Rockin' Into the Night  .38 Special    1980   \n",
       "4       Art For Arts Sake         10cc    1975   \n",
       "\n",
       "                             song_artist  first  year  playcount  fg  \n",
       "0        Caught Up in You by .38 Special      1     1         82  82  \n",
       "1            Fantasy Girl by .38 Special      1     0          3   0  \n",
       "2         Hold On Loosely by .38 Special      1     1         85  85  \n",
       "3  Rockin' Into the Night by .38 Special      1     1         18  18  \n",
       "4              Art For Arts Sake by 10cc      1     1          1   1  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Change the column names when loading the '.csv':\n",
    "column_names = ['song', 'artist', 'release', 'song_artist', 'first', 'year', 'playcount', 'fg']\n",
    "df = pd.read_csv(rockfile, names=column_names, skiprows=1)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2.B Change column names using the `.rename()` function.\n",
    "\n",
    "The `.rename()` function takes an argument, `columns=name_dict`, in which `name_dict` is a dictionary containing the original column names as keys and the new column names as values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>song</th>\n",
       "      <th>artist</th>\n",
       "      <th>release</th>\n",
       "      <th>song_artist</th>\n",
       "      <th>first</th>\n",
       "      <th>year</th>\n",
       "      <th>playcount</th>\n",
       "      <th>fg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Caught Up in You</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1982</td>\n",
       "      <td>Caught Up in You by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>82</td>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fantasy Girl</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Fantasy Girl by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Hold On Loosely</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1981</td>\n",
       "      <td>Hold On Loosely by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rockin' Into the Night</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1980</td>\n",
       "      <td>Rockin' Into the Night by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     song       artist release  \\\n",
       "0        Caught Up in You  .38 Special    1982   \n",
       "1            Fantasy Girl  .38 Special     NaN   \n",
       "2         Hold On Loosely  .38 Special    1981   \n",
       "3  Rockin' Into the Night  .38 Special    1980   \n",
       "\n",
       "                             song_artist  first  year  playcount  fg  \n",
       "0        Caught Up in You by .38 Special      1     1         82  82  \n",
       "1            Fantasy Girl by .38 Special      1     0          3   0  \n",
       "2         Hold On Loosely by .38 Special      1     1         85  85  \n",
       "3  Rockin' Into the Night by .38 Special      1     1         18  18  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Change the column names using the `.rename()` function.\n",
    "\n",
    "df = pd.read_csv(rockfile)\n",
    "\n",
    "rename_map = {\n",
    "    # Original column: [renamed column]\n",
    "    'Song Clean':    'song', \n",
    "    'ARTIST CLEAN':  'artist', \n",
    "    'Release Year':  'release', \n",
    "    'COMBINED':      'song_artist', \n",
    "    'First?':        'first', \n",
    "    'Year?':         'year', \n",
    "    'PlayCount':     'playcount', \n",
    "    'F*G':           'fg'\n",
    "}\n",
    "\n",
    "df.rename(columns=rename_map, inplace=True)\n",
    "df.head(4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2.C Reassigning the `.columns` attribute of a DataFrame.\n",
    "\n",
    "You can also just reassign the `.columns` attribute to a list of strings containing the new column names. \n",
    "\n",
    "The only caveat with reassigning `.columns` is that you have to reassign all of the column names at once. You can't partially replace a value by working on `.columns` directly. You have to reassign `.columns` with a list of equal length. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>song</th>\n",
       "      <th>artist</th>\n",
       "      <th>release</th>\n",
       "      <th>song_artist</th>\n",
       "      <th>first</th>\n",
       "      <th>year</th>\n",
       "      <th>playcount</th>\n",
       "      <th>fg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Caught Up in You</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1982</td>\n",
       "      <td>Caught Up in You by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>82</td>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fantasy Girl</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Fantasy Girl by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Hold On Loosely</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1981</td>\n",
       "      <td>Hold On Loosely by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rockin' Into the Night</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1980</td>\n",
       "      <td>Rockin' Into the Night by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Art For Arts Sake</td>\n",
       "      <td>10cc</td>\n",
       "      <td>1975</td>\n",
       "      <td>Art For Arts Sake by 10cc</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     song       artist release  \\\n",
       "0        Caught Up in You  .38 Special    1982   \n",
       "1            Fantasy Girl  .38 Special     NaN   \n",
       "2         Hold On Loosely  .38 Special    1981   \n",
       "3  Rockin' Into the Night  .38 Special    1980   \n",
       "4       Art For Arts Sake         10cc    1975   \n",
       "\n",
       "                             song_artist  first  year  playcount  fg  \n",
       "0        Caught Up in You by .38 Special      1     1         82  82  \n",
       "1            Fantasy Girl by .38 Special      1     0          3   0  \n",
       "2         Hold On Loosely by .38 Special      1     1         85  85  \n",
       "3  Rockin' Into the Night by .38 Special      1     1         18  18  \n",
       "4              Art For Arts Sake by 10cc      1     1          1   1  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Replace the column names by reassigning the `.columns` attribute.\n",
    "df = pd.read_csv(rockfile)\n",
    "column_names = ['song', 'artist', 'release', 'song_artist', 'first', 'year', 'playcount', 'fg']\n",
    "df.columns = column_names\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Subsetting data where null values exist.\n",
    "\n",
    "We have mixed `str` and `NaN` values in the `release` column. `NaN` stands for \"not a number\" and is the way `pandas` handles \"nulls\" or nonexistent data. We can use the `.isnull()` method of a Series to find null values.\n",
    "\n",
    "Print the header of the data subset to where the `release` column is null values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>song</th>\n",
       "      <th>artist</th>\n",
       "      <th>release</th>\n",
       "      <th>song_artist</th>\n",
       "      <th>first</th>\n",
       "      <th>year</th>\n",
       "      <th>playcount</th>\n",
       "      <th>fg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fantasy Girl</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Fantasy Girl by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Baby, Please Don't Go</td>\n",
       "      <td>AC/DC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Baby, Please Don't Go by AC/DC</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>CAN'T STOP ROCK'N'ROLL</td>\n",
       "      <td>AC/DC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>CAN'T STOP ROCK'N'ROLL by AC/DC</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Girls Got Rhythm</td>\n",
       "      <td>AC/DC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Girls Got Rhythm by AC/DC</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Let's Get It Up</td>\n",
       "      <td>AC/DC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Let's Get It Up by AC/DC</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      song       artist release  \\\n",
       "1             Fantasy Girl  .38 Special     NaN   \n",
       "10   Baby, Please Don't Go        AC/DC     NaN   \n",
       "13  CAN'T STOP ROCK'N'ROLL        AC/DC     NaN   \n",
       "16        Girls Got Rhythm        AC/DC     NaN   \n",
       "24         Let's Get It Up        AC/DC     NaN   \n",
       "\n",
       "                        song_artist  first  year  playcount  fg  \n",
       "1       Fantasy Girl by .38 Special      1     0          3   0  \n",
       "10   Baby, Please Don't Go by AC/DC      1     0          1   0  \n",
       "13  CAN'T STOP ROCK'N'ROLL by AC/DC      1     0          5   0  \n",
       "16        Girls Got Rhythm by AC/DC      1     0         24   0  \n",
       "24         Let's Get It Up by AC/DC      1     0          4   0  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# This will show us records where `df['release']` is null.\n",
    "null_release_mask = df['release'].isnull()\n",
    "df[null_release_mask].head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. Update slices of your DataFrame based on mask selection/slices.\n",
    "\n",
    "In many scenarios, we want to upate values in our DataFrame according to criteria. Let's say we wanted to set all of the null values in `release` to 0.\n",
    "\n",
    "With newer versions of `pandas`, in order to manipulate data in the original DataFrame, we have to use `.loc` while performing reassignment using a mask and an index.\n",
    "\n",
    "For example, the following won't always work:\n",
    "```python\n",
    "df[row_mask]['column_name'] = new_value\n",
    "```\n",
    "\n",
    "The best way to accomplish the same task is:\n",
    "```python\n",
    "df.loc[row_mask, 'column_name'] = new_value\n",
    "```\n",
    "\n",
    "For multiple column assignment, you would use:\n",
    "```python\n",
    "df.loc[row_mask, ['col_1', 'col_2', 'col_3']] = new_value\n",
    "```\n",
    "\n",
    "#### 4.A Let's try it out. Make all of the null values in `release` 0."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>song</th>\n",
       "      <th>artist</th>\n",
       "      <th>release</th>\n",
       "      <th>song_artist</th>\n",
       "      <th>first</th>\n",
       "      <th>year</th>\n",
       "      <th>playcount</th>\n",
       "      <th>fg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Caught Up in You</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1982</td>\n",
       "      <td>Caught Up in You by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>82</td>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fantasy Girl</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>0</td>\n",
       "      <td>Fantasy Girl by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Hold On Loosely</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1981</td>\n",
       "      <td>Hold On Loosely by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rockin' Into the Night</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1980</td>\n",
       "      <td>Rockin' Into the Night by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Art For Arts Sake</td>\n",
       "      <td>10cc</td>\n",
       "      <td>1975</td>\n",
       "      <td>Art For Arts Sake by 10cc</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Kryptonite</td>\n",
       "      <td>3 Doors Down</td>\n",
       "      <td>2000</td>\n",
       "      <td>Kryptonite by 3 Doors Down</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>13</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Loser</td>\n",
       "      <td>3 Doors Down</td>\n",
       "      <td>2000</td>\n",
       "      <td>Loser by 3 Doors Down</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>When I'm Gone</td>\n",
       "      <td>3 Doors Down</td>\n",
       "      <td>2002</td>\n",
       "      <td>When I'm Gone by 3 Doors Down</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>What's Up?</td>\n",
       "      <td>4 Non Blondes</td>\n",
       "      <td>1992</td>\n",
       "      <td>What's Up? by 4 Non Blondes</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Take On Me</td>\n",
       "      <td>a-ha</td>\n",
       "      <td>1985</td>\n",
       "      <td>Take On Me by a-ha</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Baby, Please Don't Go</td>\n",
       "      <td>AC/DC</td>\n",
       "      <td>0</td>\n",
       "      <td>Baby, Please Don't Go by AC/DC</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Back In Black</td>\n",
       "      <td>AC/DC</td>\n",
       "      <td>1980</td>\n",
       "      <td>Back In Black by AC/DC</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>97</td>\n",
       "      <td>97</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Big Gun</td>\n",
       "      <td>AC/DC</td>\n",
       "      <td>1993</td>\n",
       "      <td>Big Gun by AC/DC</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>CAN'T STOP ROCK'N'ROLL</td>\n",
       "      <td>AC/DC</td>\n",
       "      <td>0</td>\n",
       "      <td>CAN'T STOP ROCK'N'ROLL by AC/DC</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Dirty Deeds Done Dirt Cheap</td>\n",
       "      <td>AC/DC</td>\n",
       "      <td>1976</td>\n",
       "      <td>Dirty Deeds Done Dirt Cheap by AC/DC</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           song         artist release  \\\n",
       "0              Caught Up in You    .38 Special    1982   \n",
       "1                  Fantasy Girl    .38 Special       0   \n",
       "2               Hold On Loosely    .38 Special    1981   \n",
       "3        Rockin' Into the Night    .38 Special    1980   \n",
       "4             Art For Arts Sake           10cc    1975   \n",
       "5                    Kryptonite   3 Doors Down    2000   \n",
       "6                         Loser   3 Doors Down    2000   \n",
       "7                 When I'm Gone   3 Doors Down    2002   \n",
       "8                    What's Up?  4 Non Blondes    1992   \n",
       "9                    Take On Me           a-ha    1985   \n",
       "10        Baby, Please Don't Go          AC/DC       0   \n",
       "11                Back In Black          AC/DC    1980   \n",
       "12                      Big Gun          AC/DC    1993   \n",
       "13       CAN'T STOP ROCK'N'ROLL          AC/DC       0   \n",
       "14  Dirty Deeds Done Dirt Cheap          AC/DC    1976   \n",
       "\n",
       "                              song_artist  first  year  playcount  fg  \n",
       "0         Caught Up in You by .38 Special      1     1         82  82  \n",
       "1             Fantasy Girl by .38 Special      1     0          3   0  \n",
       "2          Hold On Loosely by .38 Special      1     1         85  85  \n",
       "3   Rockin' Into the Night by .38 Special      1     1         18  18  \n",
       "4               Art For Arts Sake by 10cc      1     1          1   1  \n",
       "5              Kryptonite by 3 Doors Down      1     1         13  13  \n",
       "6                   Loser by 3 Doors Down      1     1          1   1  \n",
       "7           When I'm Gone by 3 Doors Down      1     1          6   6  \n",
       "8             What's Up? by 4 Non Blondes      1     1          3   3  \n",
       "9                      Take On Me by a-ha      1     1          1   1  \n",
       "10         Baby, Please Don't Go by AC/DC      1     0          1   0  \n",
       "11                 Back In Black by AC/DC      1     1         97  97  \n",
       "12                       Big Gun by AC/DC      1     1          6   6  \n",
       "13        CAN'T STOP ROCK'N'ROLL by AC/DC      1     0          5   0  \n",
       "14   Dirty Deeds Done Dirt Cheap by AC/DC      1     1         85  85  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We're going to reload our data to a fresh state.\n",
    "column_names = ['song', 'artist', 'release', 'song_artist', 'first', 'year', 'playcount', 'fg']\n",
    "df = pd.read_csv(rockfile, names=column_names, skiprows=1)\n",
    "\n",
    "# create/identify the target subset and use it as an indexing tool to set values.\n",
    "null_release_mask = df['release'].isnull()\n",
    "df.loc[null_release_mask, 'release'] = 0\n",
    "\n",
    "# We'll then print out our DataFrame's first 15 rows:\n",
    "df.head(15)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4.B Verify that `release` contains no null values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "song           0\n",
       "artist         0\n",
       "release        0\n",
       "song_artist    0\n",
       "first          0\n",
       "year           0\n",
       "playcount      0\n",
       "fg             0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5. Ensure that the data types of the columns make sense. \n",
    "\n",
    "Verifying column data types is a critical part of data munging. If columns have the wrong data type, then there is usually corrupted or incorrect data in some of the observations.\n",
    "\n",
    "#### 5.A Look at the data types for the columns. Are any incorrect given what the data represents?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2230 entries, 0 to 2229\n",
      "Data columns (total 8 columns):\n",
      "song           2230 non-null object\n",
      "artist         2230 non-null object\n",
      "release        1653 non-null object\n",
      "song_artist    2230 non-null object\n",
      "first          2230 non-null int64\n",
      "year           2230 non-null int64\n",
      "playcount      2230 non-null int64\n",
      "fg             2230 non-null int64\n",
      "dtypes: int64(4), object(4)\n",
      "memory usage: 139.5+ KB\n"
     ]
    }
   ],
   "source": [
    "# We're going to reload our data to a fresh state.\n",
    "column_names = ['song', 'artist', 'release', 'song_artist', 'first', 'year', 'playcount', 'fg']\n",
    "df = pd.read_csv(rockfile, names=column_names, skiprows=1)\n",
    "\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>song</th>\n",
       "      <th>artist</th>\n",
       "      <th>release</th>\n",
       "      <th>song_artist</th>\n",
       "      <th>first</th>\n",
       "      <th>year</th>\n",
       "      <th>playcount</th>\n",
       "      <th>fg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Caught Up in You</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1982</td>\n",
       "      <td>Caught Up in You by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>82</td>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fantasy Girl</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Fantasy Girl by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Hold On Loosely</td>\n",
       "      <td>.38 Special</td>\n",
       "      <td>1981</td>\n",
       "      <td>Hold On Loosely by .38 Special</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               song       artist release                      song_artist  \\\n",
       "0  Caught Up in You  .38 Special    1982  Caught Up in You by .38 Special   \n",
       "1      Fantasy Girl  .38 Special     NaN      Fantasy Girl by .38 Special   \n",
       "2   Hold On Loosely  .38 Special    1981   Hold On Loosely by .38 Special   \n",
       "\n",
       "   first  year  playcount  fg  \n",
       "0      1     1         82  82  \n",
       "1      1     0          3   0  \n",
       "2      1     1         85  85  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "_Only the `release` column appears to be wrong. It is represented as a string but should be an integer for year._"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 6. Investigate and clean up the `release` column.\n",
    "\n",
    "The `release` column is a string data type when it should be an integer.\n",
    "\n",
    "#### 6.A Figure out what value(s) are causing the `release` column to be encoded as a string instead of an integer."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['1982', nan, '1981', '1980', '1975', '2000', '2002', '1992', '1985',\n",
       "       '1993', '1976', '1995', '1979', '1984', '1977', '1990', '1986',\n",
       "       '1974', '2014', '1987', '1973', '2001', '1989', '1997', '1971',\n",
       "       '1972', '1994', '1970', '1966', '1965', '1983', '1955', '1978',\n",
       "       '1969', '1999', '1968', '1988', '1962', '2007', '1967', '1958',\n",
       "       '1071', '1996', '1991', '2005', '2011', '2004', '2012', '2003',\n",
       "       '1998', '2008', '1964', '2013', '2006', 'SONGFACTS.COM', '1963',\n",
       "       '1961'], dtype=object)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Looking at the unique values in the column can be a good way to find offending values:\n",
    "df.release.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# A row has SONGFACTS.COM as a value — this is clearly not a year."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 6.B Look at the rows in which there is incorrect data in the `release` column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>song</th>\n",
       "      <th>artist</th>\n",
       "      <th>release</th>\n",
       "      <th>song_artist</th>\n",
       "      <th>first</th>\n",
       "      <th>year</th>\n",
       "      <th>playcount</th>\n",
       "      <th>fg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1504</th>\n",
       "      <td>Bullfrog Blues</td>\n",
       "      <td>Rory Gallagher</td>\n",
       "      <td>SONGFACTS.COM</td>\n",
       "      <td>Bullfrog Blues by Rory Gallagher</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                song          artist        release  \\\n",
       "1504  Bullfrog Blues  Rory Gallagher  SONGFACTS.COM   \n",
       "\n",
       "                           song_artist  first  year  playcount  fg  \n",
       "1504  Bullfrog Blues by Rory Gallagher      1     1          1   1  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Slice and assign.\n",
    "release_mask = df['release'] == \"SONGFACTS.COM\"\n",
    "df[release_mask]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 6.C. Clean up the data. Normally we may replace the offending data with null np.nan values, however we previously converted all of the nan values in the release column to zeros so we might as well continue with the same practice. Replacing with 0 (or nan) will allow us to convert the column to numeric."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.loc[release_mask, 'release'] = np.nan\n",
    "df['release'] = df['release'].map(lambda x: float(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2230 entries, 0 to 2229\n",
      "Data columns (total 8 columns):\n",
      "song           2230 non-null object\n",
      "artist         2230 non-null object\n",
      "release        1652 non-null float64\n",
      "song_artist    2230 non-null object\n",
      "first          2230 non-null int64\n",
      "year           2230 non-null int64\n",
      "playcount      2230 non-null int64\n",
      "fg             2230 non-null int64\n",
      "dtypes: float64(1), int64(4), object(3)\n",
      "memory usage: 139.5+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Note:** Year can also be considered a descriptive value and therefore it also makes sense for a Year column to be an object.  \n",
    "However, just like in this situation, using conversion to numerics is a great way of identifying improper values in a year column."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 7. Get summary statistics for the `release` column using the `.describe()` function.\n",
    "\n",
    "Now that the `release` column is finally a numeric data type, we can apply the `.describe()` function.  \n",
    "\n",
    "#### 7.A Print out the summary stats for the `release` column. What is the earliest and latest release date?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    1652.000000\n",
       "mean     1978.019976\n",
       "std        24.191247\n",
       "min      1071.000000\n",
       "25%      1971.000000\n",
       "50%      1977.000000\n",
       "75%      1984.000000\n",
       "max      2014.000000\n",
       "Name: release, dtype: float64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['release'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# The earliest release date is is 1071 and latest is 2014."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 7.B Based on the summary statistics, is there anything else wrong with the `release` column? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>song</th>\n",
       "      <th>artist</th>\n",
       "      <th>release</th>\n",
       "      <th>song_artist</th>\n",
       "      <th>first</th>\n",
       "      <th>year</th>\n",
       "      <th>playcount</th>\n",
       "      <th>fg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>547</th>\n",
       "      <td>Levon</td>\n",
       "      <td>Elton John</td>\n",
       "      <td>1071.0</td>\n",
       "      <td>Levon by Elton John</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>8</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      song      artist  release          song_artist  first  year  playcount  \\\n",
       "547  Levon  Elton John   1071.0  Levon by Elton John      1     1          8   \n",
       "\n",
       "     fg  \n",
       "547   8  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# A year of 1071 for a song release seems wrong. \n",
    "# We might want to impose a cut off for what the earliest song can be.\n",
    "df[df.release == 1071]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "_Looking at the DataFrame that contains the year 1071, we can see that the year was probably corrupted and should be replaced with something else if possible._"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "### 8. Make changes and investigate using custom functions with `.apply()`.\n",
    "\n",
    "Let's say we want to traverse every single row in our data set and apply a function to that row.\n",
    "\n",
    "#### 8.A Write a function that will take a row of a DataFrame and print out the song, artist, and whether or not the release date is < 1970.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def release_inspector(row):\n",
    "    print('--------------------------------')\n",
    "    print(row['song'], row['artist'], row['release'], '< 1970?:', row['release'] < 1970)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# We're going to reload our data to a fresh state.\n",
    "column_names = ['song', 'artist', 'release', 'song_artist', 'first', 'year', 'playcount', 'fg']\n",
    "df = pd.read_csv(rockfile, names=column_names, skiprows=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 8.B Using the `.apply()` function, apply the function you wrote to the first four rows of the DataFrame.\n",
    "\n",
    "You will need to tell the `apply` function to operate row by row. Setting the keyword argument as `axis=1` indicates that the function should be applied to each row individually."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------\n",
      "--------------------------------\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "(\"'<' not supported between instances of 'str' and 'int'\", 'occurred at index 0')",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-23-3eea4d5d0176>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhead\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mapply\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrelease_inspector\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/Users/ricky.hennessy/anaconda/lib/python3.6/site-packages/pandas/core/frame.py\u001b[0m in \u001b[0;36mapply\u001b[0;34m(self, func, axis, broadcast, raw, reduce, args, **kwds)\u001b[0m\n\u001b[1;32m   4260\u001b[0m                         \u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4261\u001b[0m                         \u001b[0mreduce\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mreduce\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 4262\u001b[0;31m                         ignore_failures=ignore_failures)\n\u001b[0m\u001b[1;32m   4263\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4264\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_apply_broadcast\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Users/ricky.hennessy/anaconda/lib/python3.6/site-packages/pandas/core/frame.py\u001b[0m in \u001b[0;36m_apply_standard\u001b[0;34m(self, func, axis, ignore_failures, reduce)\u001b[0m\n\u001b[1;32m   4356\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4357\u001b[0m                 \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mv\u001b[0m \u001b[0;32min\u001b[0m \u001b[0menumerate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mseries_gen\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 4358\u001b[0;31m                     \u001b[0mresults\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   4359\u001b[0m                     \u001b[0mkeys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4360\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-21-ad4b8ae46bca>\u001b[0m in \u001b[0;36mrelease_inspector\u001b[0;34m(row)\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mrelease_inspector\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'--------------------------------'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'song'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'artist'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'release'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'< 1970?:'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'release'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;36m1970\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: (\"'<' not supported between instances of 'str' and 'int'\", 'occurred at index 0')"
     ]
    }
   ],
   "source": [
    "df.head(4).apply(release_inspector, axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You'll notice that there will be a final output Series of `None` values. The `.apply()` function, if a return value is not specified, will return a Series of `None` values (similar to how the default return for Python functions is `None` when a return statement is not specified)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 9. Write a function that converts cells in a DataFrame to float and otherwise replaces them with `np.nan`.\n",
    "\n",
    "If applied to our data, it would keep only the numeric information and otherwise input null values.\n",
    "\n",
    "Recall that the try-except syntax in Python is a great way to try something and take another action if the initial step fails:\n",
    "\n",
    "```python\n",
    "try:\n",
    "    Perform some action.\n",
    "except:\n",
    "   Perform some other action if the first failed with an error.\n",
    "```\n",
    "\n",
    "#### 9.A Write the function that takes a column and converts all of its values to float if possible and `np.nan` otherwise. The return value should be the converted Series."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "def converter_helper(value):\n",
    "    try:\n",
    "        return float(value)\n",
    "    except:\n",
    "        return np.nan\n",
    "\n",
    "def convert_to_float(column):\n",
    "    column = column.map(converter_helper)\n",
    "    return column"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 9.B Try your function out on the rock song data and ensure the output is what you expected.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>song</th>\n",
       "      <th>artist</th>\n",
       "      <th>release</th>\n",
       "      <th>song_artist</th>\n",
       "      <th>first</th>\n",
       "      <th>year</th>\n",
       "      <th>playcount</th>\n",
       "      <th>fg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1982.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>82.0</td>\n",
       "      <td>82.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1981.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>85.0</td>\n",
       "      <td>85.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1980.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>18.0</td>\n",
       "      <td>18.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1975.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2000.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>13.0</td>\n",
       "      <td>13.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2000.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2002.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>6.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1992.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1985.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   song  artist  release  song_artist  first  year  playcount    fg\n",
       "0   NaN     NaN   1982.0          NaN    1.0   1.0       82.0  82.0\n",
       "1   NaN     NaN      NaN          NaN    1.0   0.0        3.0   0.0\n",
       "2   NaN     NaN   1981.0          NaN    1.0   1.0       85.0  85.0\n",
       "3   NaN     NaN   1980.0          NaN    1.0   1.0       18.0  18.0\n",
       "4   NaN     NaN   1975.0          NaN    1.0   1.0        1.0   1.0\n",
       "5   NaN     NaN   2000.0          NaN    1.0   1.0       13.0  13.0\n",
       "6   NaN     NaN   2000.0          NaN    1.0   1.0        1.0   1.0\n",
       "7   NaN     NaN   2002.0          NaN    1.0   1.0        6.0   6.0\n",
       "8   NaN     NaN   1992.0          NaN    1.0   1.0        3.0   3.0\n",
       "9   NaN     NaN   1985.0          NaN    1.0   1.0        1.0   1.0"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.apply(convert_to_float).head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# create a new dataframe via applying our function\n",
    "\n",
    "df2 = df.apply(convert_to_float)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "#### 9.C Describe the new float-only DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>first</th>\n",
       "      <th>year</th>\n",
       "      <th>playcount</th>\n",
       "      <th>fg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2230.0</td>\n",
       "      <td>2230.000000</td>\n",
       "      <td>2230.000000</td>\n",
       "      <td>2230.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.741256</td>\n",
       "      <td>16.872646</td>\n",
       "      <td>15.048430</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.438043</td>\n",
       "      <td>25.302972</td>\n",
       "      <td>25.288366</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>18.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>142.000000</td>\n",
       "      <td>142.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        first         year    playcount           fg\n",
       "count  2230.0  2230.000000  2230.000000  2230.000000\n",
       "mean      1.0     0.741256    16.872646    15.048430\n",
       "std       0.0     0.438043    25.302972    25.288366\n",
       "min       1.0     0.000000     0.000000     0.000000\n",
       "25%       1.0     0.000000     1.000000     0.000000\n",
       "50%       1.0     1.000000     4.000000     3.000000\n",
       "75%       1.0     1.000000    21.000000    18.000000\n",
       "max       1.0     1.000000   142.000000   142.000000"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.describe()"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
