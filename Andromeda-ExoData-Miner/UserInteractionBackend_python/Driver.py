from DataRetrival import eutodic, nasatodic
from UserInteractionBackend_python import CompareIt, xmlgenerator, MergeIt


def buildEUdict():
    '''
    Creates a dictionary representation of Exoplanet.eu's catalogue
    '''

    url = 'http://www.exoplanet.eu/catalog/csv/'
    eu_dict = eutodic.build_dict(url)

    return eu_dict


def buildNasadict():
    '''
    Creates a dictionary representation of NASA's catalogue
    '''

    nasa_dict = nasatodic.crawler()

    return nasa_dict


if __name__ == "__main__":
    eu = buildEUdict()
    nasa = buildNasadict()
    merged = MergeIt.mergeSources(eu, nasa)
    xmlgenerator.xmlgenerator(len(list(merged)), "/UserInteractionFrontend_shell/mfork/open_exoplanet_catalogue/systems", merged)
