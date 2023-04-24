# SI507_Final_Project
This is my final project for SI 507.

## Required packages and files:
To run this code, you will need to have installed the following python 3 packages:
* bs4
* selenium
* urllib
* argparse
* plotly


Additionally, you will need to download the chromedriver and install it in the root directory of this repository. ChromeDriver can be installed here: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).

## How to use my code:
When my code first runs, it will scrape all congressperson data from Wikipedia and store it locally. After this is done, my code offers two main functionalities: searching the congressperson data and visualizing the congressperson data. Users can interact with my code by running `main.py` with several optional arguments and a few required arguments. 

### How to search using my code:
To use this repository's search functionality, users can run a line of code of the following form in the command line:
```
python3 main.py  [--name NAME] [--party PARTY] [--gender GENDER] [--ethnicity ETHNICITY] [--birthday BIRTHDAY] [--position POSITION] [--birthplace BIRTHPLACE] [--constituency CONSTITUENCY] search
```
This code will return a list of the names of all congresspersons in our database that satisfy the specified search criteria. For example, to search for all congresspersons of the Han ethnicity from Beijing, we could run the following search:
```
python3 main.py --ethnicity 汉 --constituency 北京市 search
```
If we wanted to learn more about a specific congressperson, we can also get a detailed view by searching their name:
```
python3 main.py --name 潘敬东 search
```
## How to visualize using my code:
To use this repository's visualization functionality, users can run a line of code of the following form in the command line:
```
python3 main.py [--graphic {table,barplot,piechart}] [--graphic_property {name,party,gender,ethnicity,birthday,position,birthplace,constituency}] visualize
```
This code will make a visualization (e.g. table, barplot, piechart) using `plotly` to depict how the demographics of our congresspersons break down. For example, to visualize the genders of congresspersons using a piechart, the user could run the following command:
```
python3 main.py --graphic piechart --graphic_property gender visualize
```


