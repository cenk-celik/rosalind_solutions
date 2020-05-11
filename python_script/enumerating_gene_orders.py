{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true,
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "# Enumerating Gene Orders\n",
    "## Problem\n",
    "A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.\n",
    "\n",
    "> **Given:** A positive integer n≤7.\n",
    "\n",
    "> **Return**: The total number of permutations of length n, followed by a list of all such permutations (in any order)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "outputs": [],
   "source": [
    "with open(\"/Users/cenkcelik/Downloads/rosalind_perm.txt\") as file:\n",
    "    N = int(file.read())"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "outputs": [],
   "source": [
    "import itertools\n",
    "\n",
    "def permutation(n):\n",
    "    perm = itertools.permutations(list(range(1, n + 1)))\n",
    "    for i, j in enumerate(list(perm)):\n",
    "        permutation_list = ''\n",
    "        for item in j:\n",
    "            permutation_list += str(item) + ' '\n",
    "        print(permutation_list)\n",
    "\n",
    "def total_permutation(n):\n",
    "    perm = itertools.permutations(list(range(1, n + 1)))\n",
    "    print(len(list(perm)))"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "outputs": [],
   "source": [
    "def enumerating_gene_orders(n):\n",
    "    total_permutation(n)\n",
    "    permutation(n)"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n",
      "1 2 3 4 \n",
      "1 2 4 3 \n",
      "1 3 2 4 \n",
      "1 3 4 2 \n",
      "1 4 2 3 \n",
      "1 4 3 2 \n",
      "2 1 3 4 \n",
      "2 1 4 3 \n",
      "2 3 1 4 \n",
      "2 3 4 1 \n",
      "2 4 1 3 \n",
      "2 4 3 1 \n",
      "3 1 2 4 \n",
      "3 1 4 2 \n",
      "3 2 1 4 \n",
      "3 2 4 1 \n",
      "3 4 1 2 \n",
      "3 4 2 1 \n",
      "4 1 2 3 \n",
      "4 1 3 2 \n",
      "4 2 1 3 \n",
      "4 2 3 1 \n",
      "4 3 1 2 \n",
      "4 3 2 1 \n"
     ]
    }
   ],
   "source": [
    "enumerating_gene_orders(N)"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "outputs": [],
   "source": [
    "\n"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  }
 ],
 "metadata": {
  "kernelspec": {
   "name": "pycharm-c44dcd6d",
   "language": "python",
   "display_name": "PyCharm (rosalind_solutions)"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}