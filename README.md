
# COMP 170 SU25 WEEK 08

This assignment has two parts: a coding part based on current material we discuss in class and a reflection part to evaluate work you have already submitted.


## Finals week policy

There is no final exam for the course. There will be a final assignemnt that will be published the week before finals and will be due the week of finals. Additionally, 8 students in the course will be invited randomly to a brief meeting with the instructor during the course's final exam slot. The final exam slot for this course is on Tuesday, August 5, 2025 from 11 AM to 1 PM. If you are selected for a brief meeting, we'll spend about 15 minutes during the final exam slot to review your work. This interview will cover coding practices based on your past assignments. It is meant as a checkpoint to ensure that you have internalized the work you submitted.


## Code

We'll focus our work on classes `Person` and `Birthday` as we'll use them extensively in the course's project.

### Write method `Person.say_birthday(self)`

Write a method in class `Person` with header
```python
def say_birthday(self):
```
that returns a conversational string with someone's birthday. For example, if the birthday is on 6/29, the method should return the string "29th of June". Or, if someone's birthday is on 1/1, the conversational string should be "1st of January", etc.


### Redefine the `<` operator for two `Person` objects

Redefine the `<` operator with the *special function*
```python
def __lt__(self, other):
```
so that the invoking object (`self`) can compare itself to the referenced object (`other`) and return `true` if `self.first_name` is alphabetically less than `other.first_name`.


### Write a mutator for `Birthday.month`

Write a method with header
```python
def set_month(self, month):
```
that changes the object's month only if the passed argument is valid.


### Complete method `Birthday.days_until(self)`

The method should return the number of days between the current day and the next occurence of the birthday object. The method to compute this, as discussed in class, is to compute the number of days in the year for each of the two dates (today and the birthday). We completed method `Person.day_in_year(self, month, day)` to compute exactly that. For example
```python
day_in_year(2,15)
```
should return 46, because February 15 is the 46th day in the year. 

If $d_b$ is the day of the year for the target birthday and $d_t$ is the day of the year for today, the number of days until the target birthday is $d_b-d_t$ if $d_b>d_t$. Otherwise try $365+(d_b-d_t)$. Test the code with your birthday and verify that it returns the correct number of days until your next birthday party!


## Code requirements

* Methods that return a value should have one and only one `return` statement. Multiple `return` statements are not allowed.
* Methods with `print` statements should not have a `return` statement.
* The following commands should **not** be used: `import`, `break`, `continue`.


## Reflect

Review the posted solutions from the previous assignment: [ales](./solutions_week07/SuperAles.py) and [vehicles](./solutions_week07/SuperVehicles.py). Compare the posted solutions with your solutions. Notice the differences between your code and the solutions code and describe them. Trivial differences like the names of variables are not that important.

### Frequent mistakes expected at this point

* You wrote the superclass but forgot to rewrite the derived classes.

* **Code has no comments** to demonstrate mastery of the program.

* Extra points if your code has some tests that you wrote yourelf without being asked to (shows initiative/curiocity).


### Read more about:

* [Type hints in Python](https://docs.python.org/3/library/typing.html); also useful [cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#functions)
* [f-strings in Python](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)
* [lists in Python](https://docs.python.org/3/tutorial/datastructures.html). Also chapters 7.1 and 7.2 of the textbook.
* [the for statement](https://docs.python.org/3/reference/compound_stmts.html#for) and [for loop over a list in Python](https://docs.python.org/3/tutorial/controlflow.html#for-statements). Also chapter 2.3 and 7.1 of the textbook.
