# Printing RStudio Cheatsheets at GVSU

## Data
The `essential-sheets/` directory contains many helpful sheets I deem as "essential" to learning R and R basics. Sheets were pulled from [the RStudio GitHub Page](https://github.com/rstudio/cheatsheets). 

Each individual sheet can be found in the `all-sheets/` directory in the event that you want to select your own. 

## Creating Your Own Sheet

If you wish to make your own file, create a new folder and place all of the sheets you want in that folder. Then use the `pdf_merger.py` program to merge the files into one PDF. This can be done with 

```
python3 pdf_merger.py my-sheets/
```

assuming you have for working directory set to the root directory of this repository and that you have a folder named `my-sheets`. Do note that some of the files do not have the same margins as the rest and others may need some editing to work properly with the Python program.

All sheets here are under a Creative Commons license, so be sure to follow those guidelines if you aim to edit the sheets. 

## Printing the Sheets
Printing is super easy and can cost less than $1089. Follow these steps.

1. Be prepared to send your combined `.pdf` file to copycenter@gvsu.edu. 
2. Go to the [GVSU Copy Center](https://www.gvsu.edu/busfin/gvsu-laker-store-copy-center-45.htm), located in the basement of the Laker Store.
3. Tell them that you have a pdf and would like the pages to be bound in a flipbook format. You want the following attributes (most of which happen by default):
    * Printed on slightly thicker paper
    * Full color
    * Minimal border
    * Spiral binding (the one that looks like a spring)
    * A clear front cover
    * Black back cover
    * Landscape printing, flipping on the long edge
    
If you are only doing one printing, they may be able to print and bind it for you right there (with a roughly 5 minute wait). 

## Payment
Payment is due after printing has finished. Cash is accepted until October 30, 2021. Otherwise, debit and credit cards work.

## Questions
Please post any questions, comments, or concerns as an issue in the issues tab. Thank you!
