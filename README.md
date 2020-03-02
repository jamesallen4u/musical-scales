# musical-scales
Code for the musical scales research project

Necessary dependencies to run these programs:
1. [SageMath](https://www.sagemath.org/)
2. [Python 3.x](https://www.python.org/downloads/)
3. [Wolfram Mathematica](https://www.wolfram.com/mathematica/)

Instructions to generate data spreadsheet:
1. Open and run **Generate GAP Columns and Orbits.ipynb** in a [SageMath notebook](https://doc.sagemath.org/html/en/prep/Intro-Tutorial.html) environment. If you complete this correctly, you should see a file called **S*x*_T*y*.csv** in the working directory, where *x* represents the Symmetric group you are looking at and *y* represents number of notes in a scale. <br/> <br/> You should also have a file called **S*x*_T*y*_orb.txt** in the directory. This file will serve as the input to the Mathematica script.<br/><br/>
2. Open and run **excel_col_create_new.nb** in Mathematica. Be sure to set appropriate output directories as well as correctly define the constants which set the number of subgroups up to conjugacy and number of orbits. This step should yield you a file called **S*x*_T*y*_m.csv**<br/><br/>
3. You can now merge the **S*x*_T*y*.csv** and **S*x*_T*y*_m.csv** files by either running the **merge_csv.py** script, or by manually copy/pasting the columns to a new combined spreadsheet. 