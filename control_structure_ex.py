{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bc1c38b2",
   "metadata": {},
   "outputs": [],
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
   "execution_count": 2,
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
   "execution_count": 3,
   "id": "b7cd06c0",
   "metadata": {},
   "outputs": [],
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
   "execution_count": 4,
   "id": "397beae4",
   "metadata": {},
   "outputs": [],
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
   "execution_count": 5,
   "id": "46dfca44",
   "metadata": {},
   "outputs": [],
   "source": [
    "for number in range(1, 4):\n",
    "    print(number)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3ecc36b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "for letter in 'abcde':\n",
    "    print(letter)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "89138a12",
   "metadata": {},
   "outputs": [],
   "source": [
    "languages = ['bash', 'python', 'R', 'clojure']\n",
    "\n",
    "for programming_language in languages:\n",
    "    print(f'{programming_language} is a nice programming language')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "725524e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "i = 5\n",
    "while i <= 10:\n",
    "    print(i)\n",
    "    i += 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "dde18450",
   "metadata": {},
   "outputs": [],
   "source": [
    "for n in range(100_000):\n",
    "    print(n)\n",
    "    if n > 10:\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0cd89a33",
   "metadata": {},
   "outputs": [],
   "source": [
    "for n in range(10):\n",
    "    if n % 2 == 0:\n",
    "        continue\n",
    "    print(f'Here is an odd number: {n}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5d7e1f10",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset = [{'name': 'age', 'type': 'int', 'data': [20, 25, 43, 11, 15, 53, 36]},\n",
    "           {'name': 'is_vegetarian', 'type': 'boolean', 'data': [False, True, False, False, True, False, False]},\n",
    "           {'name': 'shoe size', 'type': 'int', 'data': [8, 11, 7, 10, 7, 9, 10]},\n",
    "           {'name': 'ISP', 'type': 'categorical', 'data': ['AT&T', 'Spectrum', 'Spectrum', 'Spectrum', 'AT&T', 'Spectrum', 'AT&T']},\n",
    "           {'name': 'BMI', 'type': 'float', 'data': [29.9, 20.4, 23.3, 21.7, 22.2, 22.8, 27.0]}]\n",
    "\n",
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
   "execution_count": 7,
   "id": "bb496400",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What day of the Week is it:Fun day\n",
      "Today is Fun day\n"
     ]
    }
   ],
   "source": [
    "day = input('What day of the Week is it?:')\n",
    "\n",
    "if day.lower() in ['monday', 'mon'] or day.upper in ['monday', 'mon']:\n",
    "    print('Today is Monday')\n",
    "else:\n",
    "    print(f'Today is {day.capitalize()}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "30526309",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What day of the Week is it?: sunday\n",
      "Today you are Free!\n"
     ]
    }
   ],
   "source": [
    "day = input('What day of the Week is it?: ')\n",
    "\n",
    "if day.lower() not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:\n",
    "    print('Invalid input. Please enter the full name of the day')\n",
    "    day = input('That is not a day of the week: ')\n",
    "\n",
    "\n",
    "if day.lower() in ['sunday', 'saturday']:\n",
    "    print('Today you are Free!')\n",
    "else:\n",
    "    print('Today you have to work!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "314244fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " How much did you make? type 1 for pay: 1\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1300.0"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total_pay = input(' How much did you make? type 1 for pay: ')\n",
    "hours_worked = 100\n",
    "hourly_rate = 10\n",
    "overtime_rate = hourly_rate * 1.5\n",
    "\n",
    "if hours_worked <=40:\n",
    "    total_pay = hours_worked * hourly_rate\n",
    "    \n",
    "else:\n",
    "    regular_pay = 40 * hourly_rate\n",
    "    overtime_pay = (hours_worked - 40) * overtime_rate\n",
    "    total_pay = regular_pay + overtime_pay\n",
    "\n",
    "total_pay"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e58bce6c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "# Test to see if the formulas work #\n",
    "\n",
    "i = 10\n",
    "while i <= 100:\n",
    "    print(i)\n",
    "    i = i + 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "367e6015",
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
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "i = 5\n",
    "while i <= 15:\n",
    "    print(i)\n",
    "    i = i + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "568533e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "i = 0\n",
    "while i <= 100:\n",
    "    print(i)\n",
    "    i = i + 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "8e7573ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n",
      "0\n",
      "-5\n",
      "-10\n"
     ]
    }
   ],
   "source": [
    "i = 100\n",
    "while i >= -10:\n",
    "    print(i)\n",
    "    i = i - 5 + 5 - 5 + 5 - 5 + 5 - 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "f1a0a0c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "f = 100\n",
    "while f >= 5:\n",
    "    print(f)\n",
    "    f = f - 5 + 5 - 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "4007cc75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number From 0 to 10: 7\n",
      "7 * 1 = 7\n",
      "7 * 2 = 14\n",
      "7 * 3 = 21\n",
      "7 * 4 = 28\n",
      "7 * 5 = 35\n",
      "7 * 6 = 42\n",
      "7 * 7 = 49\n",
      "7 * 8 = 56\n",
      "7 * 9 = 63\n",
      "7 * 10 = 70\n"
     ]
    }
   ],
   "source": [
    "Number = input('Enter a number From 0 to 10:')\n",
    "Number = int(Number)\n",
    "for i in range(1,11):\n",
    "    print(f'{Number} * {i} = {Number * i}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "c4297fc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "22\n",
      "333\n",
      "4444\n",
      "55555\n",
      "666666\n",
      "7777777\n",
      "88888888\n",
      "999999999\n"
     ]
    }
   ],
   "source": [
    "for b in range(1, 10):\n",
    "    print(str(b) * b )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "1adfc94f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is an odd number between 1 through 50: 8\n",
      "Try again!!!\n",
      "What is an odd number between 1 through 50: 9\n"
     ]
    }
   ],
   "source": [
    "num = input('What is an odd number between 1 through 50: ')\n",
    "while True:\n",
    "    if (num.isdigit() ==  False\n",
    "       or int(num) > 50\n",
    "       or int(num) < 1\n",
    "       or int(num) % 2 == 0):\n",
    "        print('Try again!!!')\n",
    "        num = input('What is an odd number between 1 through 50: ')\n",
    "    else:\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "d8897941",
   "metadata": {},
   "outputs": [],
   "source": [
    "num = int(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "93071e8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Skipping  9\n",
      "ODD 1\n",
      "ODD 3\n",
      "ODD 5\n",
      "ODD 7\n",
      "Skip 9\n",
      "ODD 11\n",
      "ODD 13\n",
      "ODD 15\n",
      "ODD 17\n",
      "ODD 19\n",
      "ODD 21\n",
      "ODD 23\n",
      "ODD 25\n",
      "ODD 27\n",
      "ODD 29\n",
      "ODD 31\n",
      "ODD 33\n",
      "ODD 35\n",
      "ODD 37\n",
      "ODD 39\n",
      "ODD 41\n",
      "ODD 43\n",
      "ODD 45\n",
      "ODD 47\n",
      "ODD 49\n"
     ]
    }
   ],
   "source": [
    "print(' Skipping ', num)\n",
    "for i in range(1, 50):\n",
    "    if i % 2 == 0:\n",
    "        continue\n",
    "    elif i == num:\n",
    "        print('Skip', i)\n",
    "    else:\n",
    "        print('ODD', i)\n",
    "        \n",
    "        # questions as the whole loop should had skipped and not just prompeted, i reffer back to the class.#\n",
    "        #Return before test #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "94383842",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Must be positive Numbers : 8\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "num = input('Must be positive Numbers : ')\n",
    "\n",
    "\n",
    "while True:\n",
    "    if (num.isdigit() ==  False\n",
    "       or int(num) <= 0):\n",
    "        print('Wrong Answer')\n",
    "        num = input('Positive number: ')\n",
    "    else:\n",
    "        break\n",
    "\n",
    "        \n",
    "for i in reversed(range(1, int(num) + 1)):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "386326c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "FIZZ\n",
      "4\n",
      "BUZZ\n",
      "FIZZ\n",
      "7\n",
      "8\n",
      "FIZZ\n",
      "BUZZ\n",
      "11\n",
      "FIZZ\n",
      "13\n",
      "14\n",
      "FIZZBUZZ\n",
      "16\n",
      "17\n",
      "FIZZ\n",
      "19\n",
      "BUZZ\n",
      "FIZZ\n",
      "22\n",
      "23\n",
      "FIZZ\n",
      "BUZZ\n",
      "26\n",
      "FIZZ\n",
      "28\n",
      "29\n",
      "FIZZBUZZ\n",
      "31\n",
      "32\n",
      "FIZZ\n",
      "34\n",
      "BUZZ\n",
      "FIZZ\n",
      "37\n",
      "38\n",
      "FIZZ\n",
      "BUZZ\n",
      "41\n",
      "FIZZ\n",
      "43\n",
      "44\n",
      "FIZZBUZZ\n",
      "46\n",
      "47\n",
      "FIZZ\n",
      "49\n",
      "BUZZ\n",
      "FIZZ\n",
      "52\n",
      "53\n",
      "FIZZ\n",
      "BUZZ\n",
      "56\n",
      "FIZZ\n",
      "58\n",
      "59\n",
      "FIZZBUZZ\n",
      "61\n",
      "62\n",
      "FIZZ\n",
      "64\n",
      "BUZZ\n",
      "FIZZ\n",
      "67\n",
      "68\n",
      "FIZZ\n",
      "BUZZ\n",
      "71\n",
      "FIZZ\n",
      "73\n",
      "74\n",
      "FIZZBUZZ\n",
      "76\n",
      "77\n",
      "FIZZ\n",
      "79\n",
      "BUZZ\n",
      "FIZZ\n",
      "82\n",
      "83\n",
      "FIZZ\n",
      "BUZZ\n",
      "86\n",
      "FIZZ\n",
      "88\n",
      "89\n",
      "FIZZBUZZ\n",
      "91\n",
      "92\n",
      "FIZZ\n",
      "94\n",
      "BUZZ\n",
      "FIZZ\n",
      "97\n",
      "98\n",
      "FIZZ\n",
      "BUZZ\n"
     ]
    }
   ],
   "source": [
    "# VERY IMPORTANT TO MEM COULD BE FOR A JOB #\n",
    "\n",
    "for F in range(1, 101):\n",
    "    if (F % 3 == 0) and (F % 5 == 0):\n",
    "        print('FIZZBUZZ')\n",
    "    elif F % 3 == 0:\n",
    "        print('FIZZ')\n",
    "    elif F % 5 == 0:\n",
    "        print('BUZZ')                   \n",
    "    else:\n",
    "        print(F)\n",
    "    # VERY IMPORTANT TO MEM COULD BE FOR A JOB #\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "9af1152d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Put in a Positive NUMBER: 8\n",
      "       TABLE \n",
      "  #  |  **2    |cubed\n",
      "------|-------|-----\n",
      "  1   |   1   |  1  \n",
      "  2   |   4   |  8  \n",
      "  3   |   9   | 27  \n",
      "  4   |  16   | 64  \n",
      "  5   |  25   | 125 \n",
      "  6   |  36   | 216 \n",
      "  7   |  49   | 343 \n",
      "  8   |  64   | 512 \n"
     ]
    }
   ],
   "source": [
    "    num = input('Put in a Positive NUMBER: ')\n",
    "\n",
    "    print('       TABLE ')\n",
    "    print('  #  |  **2    |cubed')\n",
    "    print('------|-------|-----')\n",
    "\n",
    "    num = int(num)\n",
    "    for K in range(1, num + 1):\n",
    "        \n",
    "        print('{:^6}|{:^7}|{:^5}'.format(K, K ** 2, K ** 3))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "f29312fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What Grade did you get?: 90\n",
      "A, GREAT JOB\n",
      "To input another grade, enter yes or y:y\n",
      "What Grade did you get?: 89\n",
      "B, So Close\n",
      "To input another grade, enter yes or y:y\n",
      "What Grade did you get?: 50\n",
      "F, redo the course \n",
      "To input another grade, enter yes or y:Y\n",
      "What Grade did you get?: 20\n",
      "F, redo the course \n",
      "To input another grade, enter yes or y:n\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    num = input('What Grade did you get?: ')\n",
    "    num = int(num)\n",
    "    if num >= 90:\n",
    "        print('A, GREAT JOB')\n",
    "    elif num >= 89:\n",
    "        print('B, So Close')\n",
    "    elif num >= 79:\n",
    "        print('C, Work Harder')\n",
    "    elif num >= 70:\n",
    "        print('D, Almost failed Retrain')\n",
    "    else:\n",
    "        print('F, redo the course ')\n",
    "        \n",
    "    choice = input('To input another grade, enter yes or y:')\n",
    "    if choice.lower() in ['yes', 'y']or choice.upper() in ['yes', 'y']:\n",
    "        continue\n",
    "    else:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29110326",
   "metadata": {},
   "outputs": [],
   "source": []
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
