# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Python lists and tuples are similar in that they are sequences of values. They are also indexed by integers. The main   difference between them is that tuples are immutable, while lists are. Lists are denoted using square brackets [ ] while tuples are generally denoted using parenthesis ( ). Only tuples will work as keys in dictionaries, because they are hashable. This means that there is a specific integer that correlates to a specific value. Keys must be immutable to be hashable, otherwise there could potentially be multiple integers for one key. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Python lists and sets are similar in that they store sequences of values. The main difference is that sets do not allow duplicates, and they are unordered, while lists are indexed by integers. An example of a list is  
a = [1, 2, 1, 2, 3]  

An example of a set would be  
b = ([1, 2, 3, 4, 5, 6])  

Sets are better for finding a specific element because there are no duplicates and because they are unordered.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Python's lamda is essentially a way of creating a function without assigning it a name. This makes it valuable for creating parameters to other functions. For example, it can be used in the key argument of a sorted function to perform operations on a list before it is compared and sorted. Ex:  
  
sorted(['watermelon', 'Coconut', 'banana', 'apple'], key=lamda word: word.lower())  

This would return ['apple', 'banana', 'Coconut', 'watermelon'], because even though 'Coconut is capitalized (and thus would appear first), our function of lamda turns it into 'coconut' before comparing and sorting it.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





