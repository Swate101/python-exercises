{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bc1c38b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I like coffee!\n",
      " Coffee is the best!\n"
     ]
    }
   ],
   "source": [
    "i_like_coffee = True\n",
    "\n",
    "if i_like_coffee:\n",
    "    print('I like coffee!')\n",
    "    print(' Coffee is the best!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d224d755",
   "metadata": {},
   "outputs": [],
   "source": [
    "i_like_coffee = False\n",
    "\n",
    "if i_like_coffee:\n",
    "    print('I like coffee!')\n",
    "    print(' Coffee is the best!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b7cd06c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "looks like a nice, sunny day!\n"
     ]
    }
   ],
   "source": [
    "it_is_raining = False\n",
    "if it_is_raining:\n",
    "    print('Better bring an umbrella!')\n",
    "else:\n",
    "    print('looks like a nice, sunny day!')\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "397beae4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Middle of the road, huh?\n"
     ]
    }
   ],
   "source": [
    "coffee_preference = 'medium'\n",
    "\n",
    "if coffee_preference == 'dark':\n",
    "    print('I love a good dark roast!')\n",
    "elif coffee_preference == 'medium':\n",
    "    print('Middle of the road, huh?')\n",
    "elif coffee_preference == 'light':\n",
    "    print('Light roast has the most caffeine!')\n",
    "else:\n",
    "    print('How about some tea then?')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "46dfca44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "for number in range(1, 4):\n",
    "    print(number)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3ecc36b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n",
      "b\n",
      "c\n",
      "d\n",
      "e\n"
     ]
    }
   ],
   "source": [
    "for letter in 'abcde':\n",
    "    print(letter)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "89138a12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bash is a nice programming language\n",
      "python is a nice programming language\n",
      "R is a nice programming language\n",
      "clojure is a nice programming language\n"
     ]
    }
   ],
   "source": [
    "languages = ['bash', 'python', 'R', 'clojure']\n",
    "\n",
    "for programming_language in languages:\n",
    "    print(f'{programming_language} is a nice programming language')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "725524e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "i = 5\n",
    "while i <= 10:\n",
    "    print(i)\n",
    "    i += 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "dde18450",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n"
     ]
    }
   ],
   "source": [
    "for n in range(100_000):\n",
    "    print(n)\n",
    "    if n > 10:\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0cd89a33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here is an odd number: 1\n",
      "Here is an odd number: 3\n",
      "Here is an odd number: 5\n",
      "Here is an odd number: 7\n",
      "Here is an odd number: 9\n"
     ]
    }
   ],
   "source": [
    "for n in range(10):\n",
    "    if n % 2 == 0:\n",
    "        continue\n",
    "    print(f'Here is an odd number: {n}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5d7e1f10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "age average: 29.00\n",
      "is_vegetarian is not numeric, skipping\n",
      "shoe size average: 8.86\n",
      "ISP is not numeric, skipping\n",
      "BMI average: 23.90\n"
     ]
    }
   ],
   "source": [
    "dataset = [{'name': 'age', 'type': 'int', 'data': [20, 25, 43, 11, 15, 53, 36]},\n",
    "           {'name': 'is_vegetarian', 'type': 'boolean', 'data': [False, True, False, False, True, False, False]},\n",
    "           {'name': 'shoe size', 'type': 'int', 'data': [8, 11, 7, 10, 7, 9, 10]},\n",
    "           {'name': 'ISP', 'type': 'categorical', 'data': ['AT&T', 'Spectrum', 'Spectrum', 'Spectrum', 'AT&T', 'Spectrum', 'AT&T']},\n",
    "           {'name': 'BMI', 'type': 'float', 'data': [29.9, 20.4, 23.3, 21.7, 22.2, 22.8, 27.0]}]\n",
    "\n",
    "# print the means for the numeric data\n",
    "for feature in dataset:\n",
    "    if feature['type'] == 'categorical' or feature['type'] == 'boolean':\n",
    "        print(f\"{feature['name']} is not numeric, skipping\")\n",
    "        continue\n",
    "    avg = sum(feature['data']) / len(feature['data'])\n",
    "    print(f\"{feature['name']} average: {avg:.2f}\") # the :.2f formats the decimal to 2 places.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d9dac18",
   "metadata": {},
   "outputs": [],
   "source": [
    "day = input\n",
    "if day.lower() in ['monday', 'mon']\n",
    "print "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
