
# Create this hierarchy using General Tree

1. Below is the management hierarchy of a soft ware company.

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


2. when i run this i want show like in below

## run code
```python
if __name__ == '__main__':
    root = build_management_tree()
    root.print_tree("name")
    root.print_tree("designation")
    root.print_tree("both")
```

## output
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

3. when i run this i want show like in below

## run code
```python
if __name__ == '__main__':

    root.print_tree(0)

    root.print_tree(1)
  
    root.print_tree(2)

    root.print_tree(3)

```


## output
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