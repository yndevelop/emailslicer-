#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:32:07 2021

@author: user
"""
# get user email address 
email = input("What is your email address?: ").strip()

# slice out user name
user_name = email[:email.index("@")]

# slice domain name
domain = email[email.index("@") + 1 :]

# format message 
output = "Your user name is {} and your domain name is {}"

# display output message
print(output.format(user_name,domain))