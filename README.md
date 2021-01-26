# Solved problems

### Cash register problem

Create a python program that will take two inputs, first is the price of an item (e.g. 0.75GBP) and second is the amount paid by a customer for the item (e.g. 20GBP). 

The program should return the least change possible to give back to the customer (e.g. 1 ten pound, 1 five pound, 2 two pound coins, 1 twenty pence coin, and 1 five pence coin).

Test 

```sh
cash_reg(20,19.99)
cash_reg(20,19.98)
cash_reg(20,0.75)
cash_reg(20,0.75)
cash_reg(20,0.49)
```

Excpected output 
```sh
1 one pence, 
1 two pence, 
1 ten pound, 1 five pound, 2 two pound, 1 twenty pence, 1 five pence, 
1 ten pound, 1 five pound, 2 two pound, 1 twenty pence, 1 five pence, 
1 ten pound, 1 five pound, 2 two pound, 1 fifty pence, 1 one pence, 
```

### Classroom interval problem

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.