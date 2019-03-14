# NBA Stats Master DataBase (Advanced + Basic) 2000-2019
**Contributors: Navid Rayhan (ongoing)**

**All data is taken from www.BasketballReference.com**

Basketballreference.com only has 3 datasets/NBA season (Basic, Advanced, per100) and no way to combine them. I created a **relational database and a database aggregation pipeline** using real datasets from the site storing complete NBA stats (Basic and Advanced) for every player from 2000-2019. The program is scalable so the data can be **updated in real time** as well to account for the ongoing 2019 season. 

The datasets were downloaded and compiled into one Excel Workbook and accessed with Python and SQLite. **Allows for 20 years of any combination of stats to be queried instead of single year/single stat restriction**

There is also an interactive subprogram to graph the relationship between any combination of 2 statistics.

## Software Used:
- Python 3.7, sqlite, numpy, matplotlib, xlrd, Excel, Jupyter

**Excel workbooks:**

<img src="https://raw.githubusercontent.com/NavidRayhan/Python-Projects/master/NBA%20Stats%20Database/screenshot_Excel.PNG" width="550">

**Database Viewer**

<img src="https://raw.githubusercontent.com/NavidRayhan/Python-Projects/master/NBA%20Stats%20Database/sc_database.PNG" width = "550">

**Subprogram to plot**

<img src="https://raw.githubusercontent.com/NavidRayhan/Python-Projects/master/NBA%20Stats%20Database/sc_jup.PNG" width ="550">

## Next Steps:

This is an ongoing project that I plan to advance further by:

  - creating a program to scrape the data directly off the site 
  - applying machine learning algorithms and statistical models to try to gain insight and predict career trajectories
  - Creating more complex time-visual graphics to display the changing trends in the last 20 years

