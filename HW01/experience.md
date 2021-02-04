
# Assignment experience

## What challenges did you encounter with this assignment, if any? 
The only challenge I encountered was getting it to recognize right triangles involving square roots when I had this initially:
```python
if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
    output += " and right triangle"
```
This was likely due to rounding at a very small decimal place so it was not exactly equal. To fix the problem, I learned of a new python function and changed it to this:
```python
if isclose(a**2 + b**2, c**2, abs_tol=1e-8) or isclose(b**2 + c**2, a**2, abs_tol=1e-8) or isclose(a**2 + c**2, b**2, abs_tol=1e-8):
        output += " and right triangle"
``` 

## What did you think about the requirements specification for this assignment?
The requirements specification didn't include details about what to do with side length inputs that could not form a triangle (when the sum of two sides is less than the third side) and did not include what to do with invalid inputs (like strings). Another piece of helpful information would be that an equilateral triangle cannot be a right triangle. Overall, the requirements specification made sense and was clear, though it left out some crucial information about how to handle edge cases. Additionally, it would be good to have a standardized way to output the classification when there is more than one.

## What challenges did you encounter with the tools?
No challenges, I used unittest a lot in SSW 555 last semester

## Describe the criteria you used to determine that you had sufficient test cases, i.e. how did you know you were done?
I knew I was done when I tested multiple values for each classification, rotated the lengths through the 3 variables to make sure all combinations worked correctly, involved decimals and square roots, and used invalid inputs in every way I could imagine to try to break the code. Once I had refactored to get side lengths involving square roots to be classified correctly as right triangles and all my tests were passing, I knew I was done. Then I changed my original check for strings as an invalid input, which was this:
```python
if isinstance(a,str) or isinstance(b,str) or isinstance(c,str):
    return "invalid input type"
```
to a try/except block just in case there's a different input type that would also cause problems as well. My tests still passed so I temporarily changed the return string value to break it to make sure it wasn't a bug before finishing completely.