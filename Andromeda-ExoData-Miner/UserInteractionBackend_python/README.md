These are the files for the back-end of the software:


- CompareIt.py: 
  - Requires the following files to be imported: xmldictonary.py, eutodic.py, nasatodic.py
  - This file contains functions that change the dictionaries and the data in them to a single format reminiscent of the OEC XML tags
- xmlgenerator.py:
  - Requires the following files to be imported: xmldictonary.py, eutodic.py, nasatodic.py, math, os, xml.etree.ElementTree. 
  - This file contains scripts that generates OEC usable XML files
- Driver.py: 
  - Requires the following files to be imported: eutodic.py, nasatodic.py, CompareIt.py.
  - This file solely is for the purpose to demo the working features of Sprint 1 and for testing purposes
