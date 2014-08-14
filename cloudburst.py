'''
Created on Aug 11, 2014

@author: lwoydziak
@author: shankins

'''
import requests
from json import dumps
import json

# example http://localhost:5000/api/v0-alpha/orgs/8/devices?user_key=993e79924d5b6346fe62a5cf62183bc5

class CloudburstAPI(object):
    '''
    classdocs
    '''
    CLOUDBURST_APP_KEY = '993e79924d5b6346fe62a5cf62183bc5'

    USER_KEY='?user_key=' + CLOUDBURST_APP_KEY
    #BASE_URL='http://api.labs.pertino.com:5000'
    BASE_URL='http://54.200.33.10:5000'
    BASE_PATH='/api/v0-alpha'
    ORGS_PATH='/orgs'
    DEVICES_PATH='/devices'
    

    def __init__(self, username, password, requestsObject=None, defaultCookies=None):
        self.__username = username
        self.__password = password
        self.requests = requests if not requestsObject else requestsObject
        
    
    def listOrgs(self):
        url = self.BASE_URL+self.BASE_PATH+self.ORGS_PATH+self.USER_KEY
        resp = self.requests.get(url, auth=(self.__username, self.__password))
        return resp.json()


    def listDevices(self, org_id):
        url = self.BASE_URL+self.BASE_PATH+self.ORGS_PATH+"/"+ str(org_id) + self.DEVICES_PATH+self.USER_KEY
        resp = self.requests.get(url, auth=(self.__username, self.__password))
        return resp.json()


    def deleteDevice(self, org_id, dev_id):
        url = self.BASE_URL+self.BASE_PATH+self.ORGS_PATH+"/"+ str(org_id) + self.DEVICES_PATH+ "/" + str(dev_id) + self.USER_KEY
        resp = self.requests.delete(url, auth=(self.__username, self.__password))
        return resp

    def deleteDeviceByName(self, org_name, device_name):
        orgsjson = api.listOrgs()
        for org in orgsjson['orgs']:
            if org['name'] == org_name:
                #print "%s %s" % (org['id'], org['name'])
        
	        devsjson = api.listDevices(org['id'])
                for dev in devsjson['devices']:
                    if dev['hostName'] == device_name:
                        #print "DELETING %s %s %s %s" % (org['id'], org['name'], dev['id'], dev['hostName'])
                        self.deleteDevice(org['id'],dev['id'])
                        
                        return #our work is done here
                return #our work is done here
        return

    

