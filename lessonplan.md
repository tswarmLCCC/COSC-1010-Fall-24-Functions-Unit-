# Subroutines

### Slide deck
The slides to accompany this section [are here](https://docs.google.com/presentation/d/1Xmo3ZSVzCj0DXMMvFfVt1wN_ywjROf3al3XcKkdC96k/edit?usp=sharing)

## TEACHER NOTES - Subroutines

A subroutine is just a ‘package’ for code.  You can write any code inside a subroutine, including calling other subroutines (we’ll get on to that bit later).

A subroutine has to be **defined (**created) before it can be **called **(used) by the program.

A subroutine can be **called **at any time during the program by typing its identifier.

Subroutines allow us to code common tasks once and reuse them many times.  This helps make our program smaller and more efficient.

Subroutine names are created using lowercase letters with underscores between words.  This is not a syntax rule but it is the common convention.  Using this instead of camel case helps us differentiate between subroutines and variables/lists when we are reading the code.

You may hear the terms ‘procedure’ or ‘function’ referred to in other programming languages.  In more complex languages these are other ‘flavours’ of subroutine that work in slightly different ways.  However, at beginner level Python handily combines them all into subroutines.

A subroutine will not run when it is created (using the **def **command). It has to be called in the program.

A subroutine can have many arguments.  They are separated by commas in the brackets when the subroutine is defined.

The **key idea** here is that when we use subroutines our code will no longer run in line order.  Instead it will jump from the main program to each subroutine called and back again.

It is extremely useful to spend time with your students tracing examples and getting them to tell you which line number will execute next until you are satisfied that they have grasped the concept.  

[This Python visualiser website is excellent for this](http://pythontutor.com/visualize.html#mode=edit) - paste the code in and watch it run line by line. 

### What Is A Subroutine?

A subroutine is a set of actions that is given a single name (identifier) in a very similar way to a variable or list.

They help us break our program down into smaller individual sections that are easier to test and reuse.  This becomes more important as we start to write longer and more complex programs.

A subroutine has to be **defined** (created) before it can be **called **(used) by the program.

There are lots of built in subroutines in Python, but these activities teach us how to create our own.  The code for **defining **(creating)** **a subroutine looks like this:


```
def subroutineName():
	Code to run when subroutine is called goes here
	return(data) - this is optional, it is not always needed
```


A subroutine can be **called ** at any time during the program by typing its identifier.  This makes the program jump from the call line to the subroutine. The code for calling a subroutine looks like this:


```
subroutineName()
```

When the subroutine is called, we usually store the returned data in a new variable.  The code for this is below:

```
newVariable = functionName()

print(newVariable)
```

This is really useful if your program needs to perform the same task multiple times at different points during the runtime - instead of writing the code for the task multiple times, we would create one subroutine and call it as many times as we need.  In this set of lessons we will be creating subroutines that carry out tasks using the skills we have previously learned (input, output, selection, iteration, lists etc).

**PLEASE NOTE - **a lot of the subroutines in the following tasks are very simplistic.  I’ve really broken it down to show _how_ to define & call subroutines to reduce the cognitive load on students when learning these techniques.  There aren’t really any advantages of coding these tasks as subroutines compared to just coding them into the main program.  subroutines become progressively more useful as your programs become more complex.



### Functions

A subroutine can also return a result (data) to the main program as its final action.  This type of subroutine is called a **function. **The code to return data goes **inside **the definition part of the program like this:


```
return(data)
```
A function that adds two numbers and returns the result to the main program.

```
#Creates & names the function
Def adder():
	# Stores two numbers in two variables.

	num1 = 10
	num2 = 15


    # Adds the variable contents together and returns the total to the main program

	return num1 + num2

# Calls the adder function and stores the data returned
outputNum = adder()

# Outputs the data in the outputNum variable
print(outputNum)
```

### Subroutines With Arguments

As well as getting data out of subroutines, we can put data in.  We do this using arguments.  

You can think of arguments as variables used by the subroutine.  They are named in the brackets after the subroutine name when the subroutine is defined and separated by commas..

In this first example we will put data into the arguments by typing it specifically into the brackets when we call the subroutine.  This subroutine has one argument called num1.  We will put the number 42 into the subroutine.

```
def add_five(num1):
	print(num1 + 5)

add_five(42)
```

This second example performs the same task, but this time the user can input a number rather than have it fixed to 42.  I’ve used a variable called userInput to store what the user types in.  The value input by the user gets stored in the _userInput_ variable and then **passed **to the _num1_ argument when the subroutine is called.

```
def add_five(num1):
 print(num1 + 5)

userInput = int(input("Enter a number"))
add_five(userInput)
```

## Predict & Run
At the 'predict' & 'run' stages students work entirely with example code.  They should inspect it carefully and write a prediction about what it will do.

They then run the code and compare the result to their prediction.

## Misconceptions & Errors to Watch Out For

- The subroutine name is identical everywhere it is used (capitals matter)
- The subroutine call is **not** indented inside the subroutine
- The subroutine is defined **before** it has been called