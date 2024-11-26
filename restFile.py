#!/usr/bin/env python3
import requests
from requests import Timeout, RequestException

## Base Class for REST API.
# This has the methods and properties for the RESTful API
class RestBase(object):
    def __init__(self):
        self._baseUrl = 'https://petstore.swagger.io/v2'
        self._headers = {'Accept': 'application/json'}

    ## Method to send GET, PUT, POST and DELETE requests to RESTful API server
    # Returns a tuple of status code and response body
    def _sendRequest(self, api, requestType='GET', params=None, json=None, data=None):
        url = f'{self._baseUrl}{api}'
        try:
            if requestType == 'GET':
                response = requests.get(url=url, headers=self._headers, params=params)
            elif requestType == 'PUT':
                response = requests.put(url=url, headers=self._headers, json=json)
            elif requestType == 'POST':
                if json:
                    response = requests.post(url=url, headers=self._headers, json=json)
                elif data:
                    response = requests.post(url=url, headers=self._headers, data=data)
            elif requestType == 'DELETE':
                response = requests.delete(url=url, headers=self._headers)
            else:
                raise Exception('Invalid Method')
        except Timeout as t:
            print(f"The request timed out - {t}")
            return None
        except RequestException as re:
            print(f"Request Exception occurred - {re}")
            return None
        except Exception as e:
            print(f"Exception occurred - {e}")
            return None
        if response.text != '':
            return (response.status_code, response.json())
        return (response.status_code, response.text)

    ## Method to get pet details
    def getPetDetails(self, petId):
        assert type(petId) is int, 'PETID must be an integer'
        return self._sendRequest(f"/pet/{petId}", requestType='GET')

    ## Method to get pet details by status
    def getPetDetailsByStatus(self, status):
        assert status in ['available', 'pending', 'sold'], \
            'Status must be available/pending/sold'
        params = {'status': status}
        return self._sendRequest(f"/pet/findByStatus", requestType='GET', params=params)

    ## Method to add pet to the server
    def addPet(self, petData):
        assert petData != None, 'Pet details mandatory'
        return self._sendRequest('/pet', requestType='POST', json=petData)

    ## Method to modify the existing pet record
    def modifyPet(self, petData):
        assert petData != None, 'Pet details mandatory'
        return self._sendRequest('/pet', requestType='PUT', json=petData)

    ## Method to modify the existing pet using form
    def modifyPetByForm(self, petData):
        assert petData != None, 'Pet details mandatory'
        return self._sendRequest(f"/pet/{petData['petId']}", requestType='POST', data=petData)

    ## Method to delete the existing pet record
    def deletePet(self, petId):
        assert petId != None, 'Pet ID mandatory'
        return self._sendRequest(f'/pet/{petId}', requestType='DELETE')

    ## Method to get store inventory
    def getStoreInventory(self):
        return self._sendRequest(f"/store/inventory", requestType='GET')

    ## Method to get store orders
    def getStoreOrder(self, orderId):
        assert orderId != None, 'Order ID mandatory'
        return self._sendRequest(f"/store/order/{orderId}", requestType='GET')

    ## Method to create a store order
    def createStoreOrder(self, orderData):
        assert orderData != None, 'Order Data mandatory'
        return self._sendRequest('/store/order', requestType='POST', json=orderData)

    ## Method to delete a store order
    def deleteStoreOrder(self, orderId):
        assert orderId != None, 'Order ID mandatory'
        return self._sendRequest(f'/store/order/{orderId}', requestType='DELETE')

    ## Method to add user
    def addUser(self, userData):
        assert userData != None, 'USer Data mandatory'
        return self._sendRequest('/user', requestType='POST', json=userData)

    ## Method to get user details
    def getUserDetails(self, userName):
        assert userName != None, 'Username mandatory'
        return self._sendRequest(f"/user/{userName}", requestType='GET')

    ## Method to update existing user details
    def udpateUserDetails(self, userData):
        assert userData != None, 'Updated user details mandatory'
        return self._sendRequest(f"/user/{userData['username']}", requestType='PUT', json=userData)

    ## Method to delete existing user
    def deleteUser(self, userName):
        assert userName != None, 'Username mandatory'
        return self._sendRequest(f'/user/{userName}', requestType='DELETE')

    ## Method to login
    def userLogin(self, username, password):
        assert username != None and password != None, 'Username and password mandatory'
        data = {'username': username, 'password': password}
        return self._sendRequest(f'/user/login', requestType='GET', params=data)

    ## Method to logout of current account
    def userLogout(self):
        return self._sendRequest(f'/user/logout', requestType='GET')
