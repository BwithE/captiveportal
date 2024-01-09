# Captive Portal
This login system ensures that only authorized individuals with valid accounts can access the network.

I crafted this login page to seamlessly integrate with a Synology router featuring a guest portal, facilitating user registration before granting network access.

To set up, clone this repository using the command:
```git clone https://github.com/bwithe/captiveportal```

Then, execute the following command to run the server:

 ```python3 server.py```

You will be prompted to input the IP address and port for the captive portal. Press Enter for default settings.

Please note that all usernames and passwords are currently stored in clear text in the users.txt file. A future update will include password hashing for enhanced security. 

![image](https://github.com/BwithE/captiveportal/assets/144924113/da884d51-e4c0-4a4d-808c-2dd918c0b7b6)

![image](https://github.com/BwithE/captiveportal/assets/144924113/cd0bf20f-a73e-421a-9d5e-ebd38ab394f8)

![image](https://github.com/BwithE/captiveportal/assets/144924113/298eae69-cadb-46d9-8852-e33285af52ab)



