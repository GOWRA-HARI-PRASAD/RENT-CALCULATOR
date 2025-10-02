# HexSoftwares_Project_RENT-CALCULATOR

This program calculates the total rent and other shared expenses for a group of roommates and then divides the total equally among them.

### Program Code

```python
#total_rent
#food
#water
#elec_charges
#persons

total_rent=int(input("enter the total rent= "))
food=int(input("enter the total food charges= "))
water=int(input("enter the water charges= "))
elec_charges=int(input("enter the electricity charges= "))
persons=int(input("enter the persons living in room= "))

total_amount=(total_rent+food+water+elec_charges)//persons
print("Each person will pay= ",total_amount)
```

### Explanation

The program prompts the user to enter several integer values to calculate the total shared cost.

  * **total\_rent:** The full amount of rent for the living space.
  * **food:** The total charges for shared food expenses.
  * **water:** The total water bill.
  * **elec\_charges:** The total electricity bill.
  * **persons:** The number of people sharing the costs.

The program then adds all the shared expenses together to get a **total\_amount** and divides this by the number of **persons**. The `//` operator is used to perform integer division, which ensures the result is a whole number.

Finally, it prints the calculated amount that each person needs to pay.

### Input and Output

The program takes five integer inputs from the user and prints a single integer as the output, representing each person's share of the expenses.

**Input:**

```
enter the total rent= 10000
enter the total food charges= 2000
enter the water charges= 500
enter the electricity charges= 1500
enter the persons living in room= 4
```

**Output:**

```
Each person will pay= 3500
```

### Test Cases

| **Input** | **Expected Output** | **Explanation** |
| :--- | :--- | :--- |
| `10000, 2000, 500, 1500, 4` | `3500` | The total cost ($14,000) is divided by 4 people. |
| `15000, 3000, 800, 2200, 5` | `4200` | The total cost ($21,000) is divided by 5 people. |
| `5000, 1000, 200, 800, 2` | `3500` | The total cost ($7,000) is divided by 2 people. |

### Conclusion

This code provides a simple yet effective solution for calculating and distributing shared household expenses. It is straightforward and easy to use, making it an excellent tool for basic budgeting among roommates.
