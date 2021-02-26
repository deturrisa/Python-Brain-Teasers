# Solved problems

## Cash register problem

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

## Classroom interval problem

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given ```sh[(30, 75), (0, 50), (60, 150)]```, you should return 2.

## Two Sum Problem

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example:
```sh
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Roman Numeral to Integer
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
## Straight Line 

You are given an array coordinates, ```coordinates[i] = [x, y]```, where ```[x, y]``` represents the coordinate of a point. Check if these points make a straight line in the XY plane.
E.g
```sh
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
```

## Max 69
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 
```sh
Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
```

```sh
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
```

## 1710. Maximum Units on a Truck
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

```sh
Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
```
```sh
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
```

```sh
Constraints:

- <= boxTypes.length <= 1000
- <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
- <= truckSize <= 106
```
## 12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```sh
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

```sh
Example 1:

Input: num = 3
Output: "III"
```
```sh
Example 2:

Input: num = 4
Output: "IV"
```
```sh
Example 3:

Input: num = 9
Output: "IX"
```
```sh
Example 4:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```
```sh
Example 5:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```
```sh
Constraints:

1 <= num <= 3999
```
