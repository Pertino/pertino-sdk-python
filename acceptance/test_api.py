'''
Created on Jul 26, 2014

@author: lwoydziak
'''
from pertinosdk import PertinoSdk, where
from jsonconfigfile import Env
        
def test_whenOrgsAvailableThenCanListThem():
    pertinoSdk = PertinoSdk(Env().get("Pertino", "login"), Env().get("Pertino", "password"))
    organizations = pertinoSdk.listOrgs()
    assert len(organizations) > 0
    
def test_whenDevicesInOrganizationsThenCanListThem():
    pertinoSdk = PertinoSdk(Env().get("Pertino", "login"), Env().get("Pertino", "password"))
    organizations = pertinoSdk.listOrgs()
    devices = pertinoSdk.listDevicesIn(organizations[0])
    assert len(devices) > 0
     
def test_deleteMachinesWithNameContainingAuto():
    pertinoSdk = PertinoSdk(Env().get("Pertino", "login"), Env().get("Pertino", "password"))
    organizations = pertinoSdk.listOrgs()
    devices = pertinoSdk.listDevicesIn(organizations[0], where("hostName").contains("auto"))
    pertinoSdk.deleteFrom(organizations[0], devices)
    assert not pertinoSdk.listDevicesIn(organizations[0], where("hostName").contains("auto"))
    