from UserInteractionBackend_python import CompareIt


def organizeDic(source, catalog):
    '''
    Helper function for mergeSources
    Organizes planets by their respective systems
    :param source dictionary (eu or nasa) in the format {<column>: {values} ...}
    :param catalog: catalog # indicating which catalog it is, nasa = 1, eu = 0
    :return: source dictionary in the format {systemname: [{planet1}, {planet2}, ...]}
    '''
    CompareIt.OECify(source)
    planets = []

    # preparing set containing system names
    sysNames = source.get('<star><name>')
    nameSet = set()

    # populate nameSet
    for item in sysNames:
        nameSet.add(item)

    datasize = len(source.get('<planet><discoverymethod>'))

    # populate euplanets (dict of individual eu planet dictionaries)
    for i in range(datasize):
        planet = {k: v[i] for k, v in source.items()}
        planets.append(planet)

    # add planet name for nasa
    if type(catalog) == int and catalog == 1:
        for items in planets:
            # Create new key '<planet><name>' and assign the concatenation of '<star><name>' + 'pl_letter'
            items['<planet><name>'] = items.get('<star><name>') + " " + items.get('pl_letter')

    systemDict = {}

    # dictionary with {systemName: [{planet1}, {planet2}]} format
    for item in nameSet:
        systemDict[item] = []
        for i in range(len(planets)):
            if planets[i].get('<star><name>') == item:
                systemDict[item].append(planets[i])

    return systemDict


def unpack(merged):
    '''
    Helper function for mergeSources
    "unpack" the merged dictionary to a format that works for xmlgenerator.py
    :param merged: merged dictionary of the form {systemname: [{planet1}, {planet2}, ...]}
    :return: unpacked dictionary of form {1: {planet1}, 2: {planet2} ...}
    '''
    i = 0
    unpacked = {}

    for key in list(merged):
        for item in merged.get(key):
            unpacked[i] = item
            i += 1
    return unpacked


def mergeSources(eu, nasa):
    '''
    Merge content from eu and nasa
    :param eu: eu dictionary
    :param nasa: nasa dictionary
    :return: merged dictionary of the form {1: {planet1}, 2: {planet2} ...}
    '''

    # signify the dictionary containing data from exoplanet.eu with a 0
    eu = organizeDic(eu, 0)
    # signify the dictionary containing data from Nasa with a 1
    nasa = organizeDic(nasa, 1)

    merged = {}

    for nKey in list(nasa):
        for eKey in list(eu):
            if nKey == eKey:
                if len(nKey) < len(eKey):
                    merged[nKey] = eu.get(eKey)
                else:
                    merged[nKey] = nasa.get(nKey)

    return unpack(merged)
