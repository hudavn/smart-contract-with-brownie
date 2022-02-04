from ast import Store
from brownie import accounts, SimpleStorage


def deploy_simple_storage():
    account =  accounts.load("dd-test")

    simple_storage = SimpleStorage.deploy({"from" : account})

    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from" : account})
    transaction.wait(1)
    updated_value = simple_storage.retrieve()
    print(updated_value)

def main():
    deploy_simple_storage()