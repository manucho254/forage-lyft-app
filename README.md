# Starter Repo

- This was a project designed by lyft to recreate a component that was left unfinished by the previous developer, refactor the code and tests the new functionality
- The project was about a car servicing system that checks for different servicing criteria for a different cars that lyft owns.
- The design was supposed to be changed from the previous one which was a complete mess and draft a new system architecture for the component.
- The new design uses Factory design pattern and strategy design pattern to create a better design for the system.
- This reduces the coupling between different classes.

##### Though process for the new design:

- created different folder and files that would have the classes of the different car Component like the Engine, Battery and Tire.

- The various types of Engines were:	
   > Capulet Engine -> Servicing criteria Once every 30,000 miles. <br>
   > Willoughby Engine -> Servicing criteria is Once every 60,000 miles. </br>
   > Sternman Engine -> Servicing criteria is Only when the warning indicator is on. </br>

- The various types of Batteries were:
   > Spindler Batter -> Servicing criteria is Once every 2 years. </br>
   > Nubbin Battery	-> Servicing criteria Once every 4 years. </br>

- The various types of Tires were:
   > Carrigan tires  - If any value of an array containing 4 values and each value is in the range of 0 through 1 contains a value greater than 0.9. </br>
   > Octoprime tires - If sum of an array containing 4 values and each value is in the range of 0 through 1 greater or equal to 3. </br>


I changed my project structure now to:

root
`
batteries:
    |

engines:
    |
test:
    |

tires:
    |
    __init__.py
    abstract_tire.py
    carrigan.py
    octoprime.py
__init__.py
.gitignore
README.md
serviceable.py
`