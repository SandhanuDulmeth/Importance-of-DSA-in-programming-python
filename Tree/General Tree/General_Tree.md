
# Management Hierarchy General Tree
## In this problem, you will create and manipulate a general tree to represent the management hierarchy of a software company. Follow the questions below and refer to the corresponding answer files for the code implementations.

# 1. Build the Management Hierarchy Tree

## Construct a general tree based on the following management hierarchy:

```mathematica
Anika (Director)
   |__Rohan (Operations Head)
      |__Meera (Logistics Manager)
         |__Kunal (Warehouse Supervisor)
         |__Zara (Fleet Coordinator)
      |__Tahir (Quality Control Manager)
   |__Samir (Technology Head)
      |__Aisha (Software Manager)
         |__Dev (Backend Lead)
         |__Nia (Frontend Lead)
      |__Rehan (Cybersecurity Manager)
```
Refer to the [Question 1 Answer](Answer/Answer_1.py) for the solution.

# 2. Print the Management Tree in Different Formats

## When you run the following code:
```python
if __name__ == '__main__':
    root = build_management_tree()
    root.print_tree("name")
    root.print_tree("designation")
    root.print_tree("both")
```

## The expected output is:
```mathematica
Anika
   |__Rohan
      |__Meera
         |__Kunal
         |__Zara
      |__Tahir
   |__Samir
      |__Aisha
         |__Dev
         |__Nia
      |__Rehan

Director
   |__Operations Head
      |__Logistics Manager
         |__Warehouse Supervisor
         |__Fleet Coordinator
      |__Quality Control Manager
   |__Technology Head
      |__Software Manager
         |__Backend Lead
         |__Frontend Lead
      |__Cybersecurity Manager

Anika (Director)
   |__Rohan (Operations Head)
      |__Meera (Logistics Manager)
         |__Kunal (Warehouse Supervisor)
         |__Zara (Fleet Coordinator)
      |__Tahir (Quality Control Manager)
   |__Samir (Technology Head)
      |__Aisha (Software Manager)
         |__Dev (Backend Lead)
         |__Nia (Frontend Lead)
      |__Rehan (Cybersecurity Manager)
```

Refer to the [Question 2 Answer](Answer/Answer_2.py) for the solution.

# 3. Print the Management Tree at Different Levels

## Enhance your code by adding functionality to print the tree up to a specified level. When you run the following code:
```python
if __name__ == '__main__':

    root.print_tree(0)

    root.print_tree(1)
  
    root.print_tree(2)

    root.print_tree(3)

```


## The expected output should be:
```mathematica
Anika (Director)


Anika (Director)
   |__Rohan (Operations Head)
   |__Samir (Technology Head)


Anika (Director)
   |__Rohan (Operations Head)
      |__Meera (Logistics Manager)
      |__Tahir (Quality Control Manager)
   |__Samir (Technology Head)
      |__Aisha (Software Manager)
      |__Rehan (Cybersecurity Manager)


Anika (Director)
   |__Rohan (Operations Head)
      |__Meera (Logistics Manager)
         |__Kunal (Warehouse Supervisor)
         |__Zara (Fleet Coordinator)
      |__Tahir (Quality Control Manager)
   |__Samir (Technology Head)
      |__Aisha (Software Manager)
         |__Dev (Backend Lead)
         |__Nia (Frontend Lead)
      |__Rehan (Cybersecurity Manager)
```

Refer to the [Question 3 Answer](Answer/Answer_3.py) for the solution.