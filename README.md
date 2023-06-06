# German Life Expectancy Analysis using Python

This project was created as part of the Research Software Engineering course at the University of Potsdam. 

There are multiple reasons why analyzing the projected population might be interesting. 
In general this can be intersting for planning and policy development, resource allocation, healthcare and public health planning as well as economic forecasting.

For Germany this might be especially interesting, not just because of it past, especially the reunification in 1990, but also to have a glimps into the future. 

There might be regional variations: east - west, rural - city, south - north, Germany - Baveria. Each state has distinct characteristics, including demographics and socioeconomic factors. 
Examining this can provide insights into the effectiveness of local policies.

Finally, getting some insight into the prospective population across Germany might help me in the future, iff I were to start a famility what states I better should not move to. This is especially true when considering long-term property investments.

* [Problem Description](#problem-description)
* [How to get started and Requirements](#how-to-get-started-requirements)
* [Running the Program](#running-the-program)
  * [CLI](#cli)
* [Dataset](#dataset)
* [Licencse](https://gitup.uni-potsdam.de/nbertrand/gleaup/-/blob/main/LICENSE) 
* [Citation](https://gitup.uni-potsdam.de/nbertrand/gleaup/-/blob/main/CITATION.cff)
  
## Problem Description

The Project will tackle questions regarding the projected population of each state in Germany. 

1. Is there a difference a difference in population increase between city states from 2022 and 2070? 
2. What state has the largest increase and decrease in population from 2022 to 2070? In absolute number as well in relation to current population.
3. How is the general trend from 2022 and 2070 for former east German states and west German states?
4. Is there a difference in population growth between genders from 2022 and 2070 across the whole country?  
5. Does the same apply in east vs west?
6. How much does the population decrease and increase in Berlin, seperated by gender, from 2022 to 2040 and finally from 2040 to 2070?

## How to get started and Requirements

Download the repository and have ipython as well as matplotlib and pandas installed. 
Testet using Python 3.11.3 - I do not give garanties that it works with older version.


## Running the Program

The Programm has two parts:
1. An ipython / Jupyternotebook that can be opened with an editor of choice. 
2. Command Line Interface Interaction with the programm

Furthermore, every function is callable from another script.

Program files are stored in the src folder.
Generated data in form of text and plots are stored in the Results folder.
Further documentation can be found in the description.txt

## CLI

```console
foo@bar:~$ python "PROGRAMM.PY" 1.csv 2.csv
```
PROGRAMM.PY is any of the src files except data_helper.py this one does not have CLI data passthrough

for example

```console
foo@bar:~$ python east_west_trend.py 1.csv 2.csv
```
## Dataset
The Datasets origin is from [Genesis, ]{https://www-genesis.destatis.de/genesis/online} a statistical data service provided by the German government. 

### Dataset used is
GENESIS-Tabelle: 12421-0004, Staat population projections with moderate life expectancy and moderate net migration


Data is used was split in 2 seperate csv files. This one done to circumvent dataset size restriction for free users. 
Data is recorded in time steps from 2022 then 2025 and continueing in steps of 5 years until 2070 
Age groups are initialy of 1 year each from 0 to 101.  

values are in 1000s for the projected population per year.

The CSV Helper is there to make the CSV workable. 
1. It merged both CSV and threw out the top rows and bottom rows with unnessary information.
2. Renamed the Headers and made the headers for the years into int. 
3. Initinal all data was in form of strings so the numerical values in the Year columns had to be converted
4. QoL change changed German Umlaute to ae, ue, oe, and renamed weiblich maennlich and insgesammt into the English equivalent.

And at least for the CLI GLOBAL VARIABLES will be used these are:
## Add some additional Data points making later work easier.

All States in a list: 
- states[0] : West german states
- states[1] : East german states (Berlin counts as West german)
- states[2] : City states
- states[3] : telling the programm to use all states

time and sex should be self explanatory

## [MIT Licencse](https://gitup.uni-potsdam.de/nbertrand/gleaup/-/blob/main/LICENSE)  
 
## [Citation](https://gitup.uni-potsdam.de/nbertrand/gleaup/-/blob/main/CITATION.cff)  