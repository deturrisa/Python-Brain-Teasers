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

For example, given ```sh[(30, 75), (0, 50), (60, 150)]```, you should return 2.

### Two Sum Problem

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example:
```sh
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Roman Numeral to Integer
Given a roman numeral, convert it to an integer.
```sh
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
```