#!/usr/bin/env markdown

# Lab1Calculator.py test definitions

Valid inputs are in the form of an operation specifier and two values.

Valid operation specifiers are: "a", "addition", "s", and "subtraction".
Providing one of these as input should result in a prompt for the first of the two values.
Providing anything except one of these should result in a re-prompt for a
new operation specifier.

The two values must both of the same type.
In case of addition, they must be one of [int, float, str, tuple, list, bool].
In case of subtraction, they must be one of [int, float]


Here are a set of test cases and their expected values, in the form of:
<inputs>
<outputs>

"invalid" will be used to represent a re-prompting for new input due to invalid inputs.

```
a .5 .5
1.0

s .5 .5
0.0

s None None
invalid

a "4" "2"
42

# dicts are not considered valid by the spec
a {4} {2}
invalid

a [4] [2]
[4, 2]

a (4, 2) (4, 2)
(4, 2, 4, 2)

# should reprompt immediately, without waiting for user to waste more input
s [4]
invalid

a True False
False

a False False
False

a True True
True

s True False
invalid

a None
invalid

s .5 1
invalid

a "8" 8
invalid
```
