# CMPS 2200  Recitation 02

**Name (Team Member 1):**_________________________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here**

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer.
- [ ]  

**TODO: your answer goes here**
[(10, 9144, 1134), (20, 154304, 9134), (50, 4520152, 142597), (100, 73322432, 1142597), (1000, 395237250560, 1142849990), (5000, 603868118744576, 142856974901), (10000, 9662889899913216, 1142856974901)]
the result show that the value when n^c<log_b(a) is larger than the value when n^c>log_b(a) 

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**
[(10, 15, 36, 19), (20, 31, 92, 42), (50, 63, 276, 89), (100, 127, 652, 184), (1000, 1023, 9120, 1525), (5000, 8191, 61728, 12274), (10000, 16383, 133456, 24561)]
the result show that when f(n)=n. the value is the largest and when f(n)=1 the value is the smallest.

for time span [(10, 5.9604644775390625, 2.1457672119140625, 11.920928955078125), (20, 1.9073486328125, 1.430511474609375, 3.5762786865234375), (50, 1.6689300537109375, 2.384185791015625, 3.814697265625), (100, 2.1457672119140625, 2.384185791015625, 4.5299530029296875), (1000, 9.298324584960938, 3.5762786865234375, 6.9141387939453125), (5000, 4.5299530029296875, 4.5299530029296875, 8.821487426757812), (10000, 4.5299530029296875, 4.5299530029296875, 8.821487426757812)]
when f(n)=logn it take longest time.


