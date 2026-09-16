# Assignment 2 — CampusWheels

## Files

- `rental.py` — contains the `Vehicle`, `Renter`, `ElectricCar`, and `Motorbike` classes.
- `main.py` — demonstrates that the classes work.

## How to run

Open a terminal in the `Assignment_02` folder and run:

```bash
python main.py
```

## What the program demonstrates

The program shows:

- A new vehicle starts as available.
- 'rent()' changes a vehicle to rented.
- 'return_vehicle()' changes it back to available.
- A renter starts with an empty 'rente' list.
- Invalid renter names and license numbers raise 'ValueError'.
- The validation also works when 'name' or 'license_no' is changed later.
- 'ElectricCar' and 'Motorbike' inherit from 'Vehicle'.
- A mixed list can contain all three vehicle types, and each class has its own '__str__()' output.

## AI-use note

I used AI to help explain the assignment requirements and to draft/check parts of my code. I reviewed the code and kept the implementation simple so I can explain how each class, property, method, inheritance, and polymorphism part works.
