# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. Prompt user for the package type
2. Convert the entire string to lowercase
2. While the input is not equal to green blue or purple repeat
   1. output "that is not an option" 
   2. prompt the user for the package type 
   3. convert the entire string to lowercase

3. If package is green
   1. price = 49.99
   2. plan_gB = 2
   3. rate = 15
3. if the user chooses blue
   1.price =70.00
   2.plan_gB = 4
   3. rate = 10
4. if the user chooses purple 
   1. price = 99.95

  
   
6. If package is green or blue
   1. prompt user how many gBs they used this month and 
   save as the variable used_gB
8. prompt the user how many months they owe and set = to months


9. if package is green or blue
   1. Calculate total = [price + (used_gB - plan_gB) * rate] * months
10. otherwise if package is purple 
    1. total = price * months


11. if package is green and total >= 75
    1. prompt user if they have a coupon
    2. if yes
       1. total - 25 = total
    2. otherwise
       3. total + 0 = total
12. print 'The amount of money that you owe for the (plan color) plan is (total)'