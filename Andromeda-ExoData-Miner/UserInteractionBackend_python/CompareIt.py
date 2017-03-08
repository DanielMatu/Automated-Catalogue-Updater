from DataRetrival.eutodic import *
from DataRetrival.nasatodic import *
from DataRetrival.xmldictonary import orgxmldict, orgxmlconvert


def oecxmltags(columnheadingkey: str):
    '''
    return the corresponding pre-OECxml tag
    :param columnheadingkey:
    :return xmltag in stringformat:
    '''
    xmltag = ''

    # call every key in the main xml dictionary orgxmldict
    for key in orgxmldict.keys():
        # if the given columheading which is a key belonging to EUdict or NASAdict
        # exists at a value inside the sets connected to each key in the orgxmldict dictionary
        # use that orgxmldict key to find the corresponding pre-OECxml tag in the
        # orgxmlconvert dictionary and return it
        if columnheadingkey in orgxmldict.get(key):
            xmltag = orgxmlconvert.get(key)

    return xmltag


def OECify(dic: dict):
    for key in list(dic):
        if oecxmltags(key) != "":
            dic[oecxmltags(key)] = dic.pop(key)
            
            
# class MyTest(unittest.TestCase):
#     # checking if the name key has a value at index 0 to show
#     # a dictionary was generated with appropriate tags
#     def test_standard_nasa_tag(self):
#         dic = crawler()
#         oec_dict = OECify(dic)
#         self.assertNotEqual(dic['<name>'][0], None)

#     def test_standard_eu_tag(self):
#         dic = build_dict()
#         oec_dict = OECify(dic)
#         self.assertNotEqual(dic['<name>'][0], None)

# unittest.main()
