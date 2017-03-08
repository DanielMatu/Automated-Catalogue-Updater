import xml.etree.ElementTree as ET


# the python script found in this file was developed with help
# and reference to
# https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue/blob/6735e0522e9c5152260d8a3b492d04ebd19c7ef0/generate_systems_kepler.py

def xmlgenerator(numfiles, foldername, source):
    # check incoming parameters
    if type(numfiles) == int:
        filelimit = numfiles
    if type(foldername) == str:
        destinationfolder = foldername

    if type(numfiles) == int and type(foldername) == str:
        lastsystemname = ""
        numcandidates = 0

        # get the size of the data set(i.e rows in Exoplanet.EU)
        datasize = len(list(source))

        # run a loop that goes over each planet in the dictionary and adds
        # it's data to the corresponding system xml file
        for i in range((datasize - (datasize - filelimit))):
            # keep track of the iteration
            # print(i)
            # set the system name of a file to that of the available stars
            systemname = (source.get(i)).get('<star><name>')
            if systemname != lastsystemname:
                # set system to to be the root xml tag of all files
                root = ET.Element("system")
                ET.SubElement(root, "name").text = systemname
                # set star to be a sub xmltag of system
                star = ET.SubElement(root, "star")
            # set planet to be a sub xmltag of star
            # this code is outside the above if statment to make sure
            # that multiple planets are added to the same file
            planet = ET.SubElement(star, "planet")
            # for each planet in the planets dictionary
            # gather the respective Systerm, Hoststar, and planet data
            # and wrtie them to xml files
            for key in (source.get(i)).keys():
                # partition each key and check what primary OEC tag it carries
                # such as <system>, <star> or <planet>
                generate(root, key, source, i, 0)
                generate(star, key, source, i, 1)
                generate(planet, key, source, i, 2)
                # if (key.partition('<system>'))[1] == '<system>':
                #     #   print(key)
                #     #   print((key.partition('<system>')))
                #     systempartion = (key.partition('<system>'))
                #     datatag = systempartion[2]
                #     #    print(systemname)
                #     if datatag.endswith('>'):
                #         datatag = datatag.strip('<')
                #         datatag = datatag.strip('>')
                #         # if the key has data write to xml
                #         if (source.get(i)).get(key) != '':
                #             # get the respective data from each key of the planet dictionary
                #             # and write it to xml
                #             element = ET.SubElement(root, datatag)
                #             element.text = (source.get(i)).get(key)
                #             # print(key)
                #             # create variables to hold the format of possible errorplus and errorminus data
                #             errorpluskey = key + 'errorplus'
                #             errorminuskey = key + 'errorminus'
                #             # if keys with errorplus and errorminus data exist for current data called by key
                #             # write it into the respective data xml tag
                #             if errorpluskey in ((source.get(i)).keys()):
                #                 element.attrib["errorplus"] = (source.get(i)).get(errorpluskey)
                #             if errorminuskey in ((source.get(i)).keys()):
                #                 element.attrib["errorminus"] = (source.get(i)).get(errorminuskey)
                #
                # if (key.partition('<star>'))[1] == '<star>':
                #     # print(key)
                #     # print((key.partition('<star>')))
                #     systempartion = (key.partition('<star>'))
                #     datatag = systempartion[2]
                #     # print(systemname)
                #     if datatag.endswith('>'):
                #         datatag = datatag.strip('<')
                #         datatag = datatag.strip('>')
                #         if (source.get(i)).get(key) != '':
                #             # get the respective data from each key of the planet dictionary
                #             # and write it to xml
                #             element = ET.SubElement(star, datatag)
                #             element.text = (source.get(i)).get(key)
                #             # print(key)
                #             # create variables to hold the format of possible errorplus and errorminus data
                #             errorpluskey = key + 'errorplus'
                #             errorminuskey = key + 'errorminus'
                #             # if keys with errorplus and errorminus data exist for current data called by key
                #             # write it into the respective data xml tag
                #             if errorpluskey in ((source.get(i)).keys()):
                #                 element.attrib["errorplus"] = (source.get(i)).get(errorpluskey)
                #             if errorminuskey in ((source.get(i)).keys()):
                #                 element.attrib["errorminus"] = (source.get(i)).get(errorminuskey)
                #
                # if (key.partition('<planet>'))[1] == '<planet>':
                #     # print(key)
                #     # print((key.partition('<planet>')))
                #     systempartion = (key.partition('<planet>'))
                #     datatag = systempartion[2]
                #     # print(systemname)
                #     if datatag.endswith('>'):
                #         datatag = datatag.strip('<')
                #         datatag = datatag.strip('>')
                #         if (source.get(i)).get(key) != '':
                #             # get the respective data from each key of the planet dictionary
                #             # and write it to xml
                #             element = ET.SubElement(planet, datatag)
                #             element.text = (source.get(i)).get(key)
                #             # print(key)
                #             # create variables to hold the format of possible errorplus and errorminus data
                #             errorpluskey = key + 'errorplus'
                #             errorminuskey = key + 'errorminus'
                #             # if keys with errorplus and errorminus data exist for current data called by key
                #             # write it into the respective data xml tag
                #             if errorpluskey in ((source.get(i)).keys()):
                #                 element.attrib["errorplus"] = (source.get(i)).get(errorpluskey)
                #             if errorminuskey in ((source.get(i)).keys()):
                #                 element.attrib["errorminus"] = (source.get(i)).get(errorminuskey)

            tree = ET.ElementTree(root)
            tree.write("../" + destinationfolder + "/" + systemname + ".xml")
            print(systemname + ".xml")
            lastsystemname = systemname
            numcandidates += 1

        print("Number of candidates: %d" % numcandidates)


def generate(primarytag, key, source, i, indicator):
    if indicator == 0:
        name = "system"
    elif indicator == 1:
        name = "star"
    else:
        name = "planet"
    if (key.partition('<' + name + '>'))[1] == '<' + name + '>':
        # print(key)
        # print((key.partition('<planet>')))
        systempartion = (key.partition('<' + name + '>'))
        datatag = systempartion[2]
        # print(systemname)
        if datatag.endswith('>'):
            datatag = datatag.strip('<')
            datatag = datatag.strip('>')
            if (source.get(i)).get(key) != '':
                # get the respective data from each key of the planet dictionary
                # and write it to xml
                element = ET.SubElement(primarytag, datatag)
                element.text = (source.get(i)).get(key)
                # print(key)
                # create variables to hold the format of possible errorplus and errorminus data
                errorpluskey = key + 'errorplus'
                errorminuskey = key + 'errorminus'
                # if keys with errorplus and errorminus data exist for current data called by key
                # write it into the respective data xml tag
                if errorpluskey in ((source.get(i)).keys()):
                    element.attrib["errorplus"] = (source.get(i)).get(errorpluskey)
                if errorminuskey in ((source.get(i)).keys()):
                    element.attrib["errorminus"] = (source.get(i)).get(errorminuskey)

# if __name__ == "__main__":
#
#     eu = Driver.buildEUdict()
#     nasa = Driver.buildNasadict()
#     merged = MergeIt.mergeSources(eu, nasa)
#     xmlgenerator(7, "systems_eu", merged)
