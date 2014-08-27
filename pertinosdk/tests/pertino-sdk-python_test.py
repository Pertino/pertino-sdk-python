'''
Created on Jul 26, 2014

@author: lwoydziak
'''
from mockito.mocking import mock
from pertinosdk import PertinoSdk, QueryBuilder, where
from mockito.mockito import when, verify
from mockito.matchers import any, Matcher

class Contains(Matcher):
    def __init__(self, sub):
        self.sub = sub
        
    def matches(self, arg):
        if not hasattr(arg, 'find'):
            return  
        
        if not self.sub or len(self.sub) <= 0:
            return
        
        for sub in self.sub:
            if not arg.find(sub) > -1:
                return
            
        return True
    
    def __repr__(self):
        return "<Contains: '%s'>" % (str(self.sub)) 

def setupSdk():
    requests = mock()
    pertinoSdk = PertinoSdk('a', 'b', requests)
    response = mock()
    when(requests).get(any(), auth=any()).thenReturn(response)
    return pertinoSdk, requests, response

def test_CanRetrieveOrganizationListUnfiltered():
    pertinoSdk, requests, response = setupSdk()
    json = {"orgs": [{"name": "organization", "id": 1234}]}
    when(response).json().thenReturn(json)
    assert pertinoSdk.listOrgs() == json["orgs"]
    verify(requests).get('http://api.labs.pertino.com:5000/api/v0-alpha/orgs?user_key=993e79924d5b6346fe62a5cf62183bc5', auth=('a', 'b'))

def test_CanRetrieveOrganizationListFiltered():
    pertinoSdk, requests, response = setupSdk()
    json = {"orgs": [{"name": "organization", "id": 1234}]}
    when(response).json().thenReturn(json)
    closure = mock()
    pertinoSdk.listOrgs(closure=closure.function)
    verify(closure).function(json["orgs"][0])
    
def test_CanRetrieveDevicesListUnfiltered():
    pertinoSdk, requests, response = setupSdk()
    json = {"devices": [{"ipv4Address": "123.456.789.10", "hostName": "host", "id": 1234}]}
    when(response).json().thenReturn(json)
    assert pertinoSdk.listDevicesIn({"id":1}) == json["devices"]
    verify(requests).get('http://api.labs.pertino.com:5000/api/v0-alpha/orgs/1/devices?user_key=993e79924d5b6346fe62a5cf62183bc5', auth=any())

def test_CanRetrieveDevicesListFiltered():
    pertinoSdk, requests, response = setupSdk()
    json = {"devices": [{"ipv4Address": "123.456.789.10", "hostName": "host", "id": 1234}]}
    when(response).json().thenReturn(json)
    closure = mock()
    pertinoSdk.listDevicesIn({"id":1}, closure.function)
    verify(closure).function(json["devices"][0])

def test_CanDeleteMachine():
    pertinoSdk, requests, response = setupSdk()
    when(requests).delete(any(), auth=any()).thenReturn(response)
    devices = [{"ipv4Address": "123.456.789.10", "hostName": "host", "id": 1234}]
    pertinoSdk.deleteFrom({"id":1}, devices)
    verify(requests, times=1).delete('http://api.labs.pertino.com:5000/api/v0-alpha/orgs/1/devices/1234?user_key=993e79924d5b6346fe62a5cf62183bc5', auth=any())   

def test_CanBuildClosureToFilterApiResponses():
    isQueryBuilder = any(QueryBuilder)
    assert isQueryBuilder.matches(where("any"))
    closure = where("someField").contains("desired")
    testDictionaryMatched = {"someField":"desired"}
    assert closure(testDictionaryMatched)
    testDictionaryNotMatched = {"someField":"nothing"}
    assert not closure(testDictionaryNotMatched)
    
    