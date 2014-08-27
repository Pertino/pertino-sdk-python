'''
Created on May 9, 2014

@author: lwoydziak
'''
from jsonconfigfile import Env
        
def pytest_configure(config):
    """ called after command line options have been parsed
        and all plugins and initial conftest files been loaded.
    """
    initialJson = '{ \
        "Pertino" : { \
            "login"          : "None", \
            "password"       : "None" \
        }\
    }'
    Env(initialJson, ".pertinoApiAcceptanceConfig", "PAPI_ACCEPTANCE_CONFIG")