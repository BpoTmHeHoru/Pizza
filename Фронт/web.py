
from ast import Try
import imp
from operator import add
from web3 import Web3
from data import *


w3 = Web3(Web3.HTTPProvider(ip))
contract = w3.eth.contract(address=address, abi=abi)

def unlock(acc, key):
    account = Web3.toChecksumAddress(acc)
    w3.eth.default_account = account
    w3.geth.personal.unlock_account(account, key,  10)

if w3.isConnected:
    print('Ок')
def unlock(acc, key): 
    account = Web3.toChecksumAddress(acc)
    w3.eth.default_account = account
    w3.geth.personal.unlock_account(account, key, 10)

def registr(acc, key, login, passw, fio):
    try:
        unlock(acc, key)
        res =  contract.functions.Registr(fio, login, passw).transact()
        return res
    except Exception as e:
        return str(e)

def auth(acc, login, passw):
    try:
        w3.eth.default_account = w3.toChecksumAddress(acc)
        res = contract.functions.Auth(login, passw).call()
        return res
    except Exception as e:
        return str(e)
        
class cart:
    

    def AddBasket(Name, Fullprice, id):
        try:
            w3.eth.default_account = w3.toChecksumAddress(acc)
            res = contract.functions.AddBasket(Name, Fullprice, id).call()
            return True
        except Exception as e:
            return str(e)

def ReturnBasket(Name, Fullprice, id):
    try:
        w3.eth.default_account = w3.toChecksumAddress(acc)
        res = contract.functions.ReturnBasket(Name, Fullprice, id).call()
        return True
    except Exception as e:
        return str(e)

class Item: 
    def __init__(self, name, price, id):
        self.name = name
        self.price = price
        self.id = id 

    def AddBasket2(self):
        return self.price

    def getName(self):
        return self.name

class Cart:
    def __init__(self, list):
        self.list = []

    def addItem(self, item):
        self.list.append(self.list)

    def FullPrice(self):
        total = 0
        for item in self.list:
            name, price = item # or price = item[1]
            total = total + price

    def getNumItems(self):
        count = 0
        for c in range(self.list):
            count = self.list + 1
            return count

def main():
    item1 = Item("pizza", .500)
    item2 = Item("pizza2", 630)
    item3 = Item("pizza3", 1000)
    c = Cart()
    c.addItem(item1)
