This files are needed to retrieve the data:

- eutodic.py: 
    - Requires the following python modules to be installed: The csv modules, the request and response modules from urllib, the StringIO from io.
    - This file reads the Exoplanet.eu website and creates a base dictionary containg the exoplanet data from the above mentioned catalogue
- nasatodic.py: 
  - Requires the following modules python to be installed: the request and time modules, BeautifulSoup module from bs4. 
  - This file reads the NASA EXOPLANET ARCHIVE website and creates a base dictionary containg the exoplanet data from the above mentioned catalogue.
- xmldictonary.py: 
  - This file contains dicctionaries with data needed to convert the original NASA and EU column headings of the exoplanet data tables 
    into a single format reminiscent of the OEC XML tags
- __init__.py:
   - Needed for the files
