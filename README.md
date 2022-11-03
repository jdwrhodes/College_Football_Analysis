# College_Football_Analysis
This repo is for analyzing a wide array of stats from Division 1 College Football from 2013-2021.

11/2/2022
Progress so far:
1. Completed multi-csv import pipeline using Glob and a For Loop.
2. Researched & implemented a Function to add team names that are missing their conference name to a dictionary. If multiple teams are missing from the same csv, then they are added to the same "Key."
3. Created a For Loop, using the Function above, to take all the team names and slice out the Conference name at the end. Then the list of conference names are added to their own new column and the Team Names are put back, without the conference name at the end.
4. Created the steps to find out what teams were missing names, provided by the For Loop, and then fix them in their separate csv files.

Future Goals
1. Take the process above and make it into a function that lives within it's own python file that can then be called into other python files.
2. Pad out any comments in the code to better describe what's going on.
3. Begin analysis process, starting with determining which of the 100+ team stats have the most impact upon games won each season.