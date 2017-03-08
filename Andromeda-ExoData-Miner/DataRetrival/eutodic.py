import csv
import urllib.request
import urllib.response
from io import StringIO


def getCSV(url='http://www.exoplanet.eu/catalog/csv/'):
    '''
    String -> list of rows
    Takes the csv url and creates a list of rows
    '''
    list_of_rows = []
    data = urllib.request.urlopen(url).read().decode('ascii', 'ignore')
    datafile = StringIO(data)
    csvReader = csv.reader(datafile)
    for row in csvReader:
        list_of_rows.append(row)
    return list_of_rows


def build_dict(url='http://www.exoplanet.eu/catalog/csv/'):
    '''
    String -> Dictionary{tag : list of strings}
    Builds the eu dictionary based on the current eu exoplanet
    catalog database.
    '''
    rows = getCSV(url)
    eu_dict = {}
    # initialize each tag to an empty list
    for j in range(len(rows[0])):
        eu_dict[rows[0][j]] = []
    # iterate through every non-tag entry and map
    for i in range(len(rows) - 1):
        for j in range(len(rows[i])):
            eu_dict[rows[0][j]].append(rows[i + 1][j])
    # adjust for first key being '# name' and change to 'name'
    eu_dict['name'] = eu_dict['# name']
    del eu_dict['# name']
    return eu_dict

# class MyTest(unittest.TestCase):

#     def test_first_key_has_values(self):
#         dict = build_dict()
#         self.assertNotEqual(dict['name'][0], None)

#     def test_last_key_has_values(self):
#         dict = build_dict()
#         self.assertNotEqual(dict['star_alternate_names'][0], None)

# unittest.main()
