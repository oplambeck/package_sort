# Package Sort Function

### Run Solution

To run the code simply run the `package_sort.py` file and the test suite will automatically run.
To add new test cases you can add calls to `sort(width, height, length, mass)` in the `if __name__ == '__main__':` block at the bottom of the file. 

### Objective

Imagine you work in Thoughtful’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

### Rules

Sort the packages using the following criteria:

* A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.

* A package is heavy when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

* STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.

* SPECIAL: packages that are either heavy or bulky can't be handled automatically.

* REJECTED: packages that are both heavy and bulky are rejected.

