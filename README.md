# _Target Tracker Interface_

### _As a navigation support for a forklift a graphical interface which emulates a compass functionality is developed which has the intention to assist forklift driver to navigate in a warehouse to a preselected target._

## `Development`

The graphical interface will follow a design pattern commonly found in computer games. Therefore the requirements for the application's development are:

- Python 3.11.8
- Pygame 2.5.2

Furthermore, the next definitions are applied to the application in regards with the interface display:

- One pixel equals $10 cm$
- A tile size is $30$ by $30$ $pixels$
- Total display area is $900$ by $900$ $pixels$

## `Software Architecture`

- State
- Unit: Compass / Target
- Sensor: Client to connect to sensor
- Command: Rules applied to update units
- Interface: Display were units are rendered

### Class State:

The `state` knows and maintains the current status of all elements in the application.

### Class Unit:

A `unit` represents any element that can be rendered on a displayed surface. Unit is a base class.

### Class Target:

### Class Compass:
