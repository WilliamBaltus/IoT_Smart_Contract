# IOT Smart Contract
This is a project for EE-629. A smart contract that will execute utilizing Chainlink, Ethereum (Kovan network), and Raspberry Pi!
Check out the website at https://sites.google.com/stevens.edu/williambaltus/home.  
(The website contains much of the information on the progress and achievement of this project)

<h2> A Synopsis </h2>

This project leverages IoT, Cloud, and Distributed Ledger Technology. It's task is to execute a transaction between two wallets on the Ethereum Kovan test network based on environmental data gathered from a BME680 sensor. The flow of events in this project is the following: 
1. Collect environmental data via a BME680 sensor and Raspberry Pi
2. Push sensor data to Firebase Database via Raspberry Pi
3. Load webpage using Flask
4. Pull data from Firebase Database
5. Publish data on webpage
6. When webpage is GET requested, return JSONified data!
7. Smart contract with paired LINK node sends GET request to webpage
8. Smart contract receives environmental data
9. Smart contract compares environmental data to threshold value
10. Smart contract transfers funds from one wallet to another

<h2> Replication and Running :white_check_mark:</h2>
Prerequisites:  

- [ ] Google Firebase Database (Cloudstore)
- [ ] Heroku account and app created
- [ ] Add Firebase environmental variables to config vars section of Heroku app 
- [ ] Raspberry Pi
- [ ] BME680
- [ ] 4 Male to Male jumper cables
- [ ] Breadboard

<h4> Running </h4> 

Wire the BME680 and the Raspberry Pi as follows:
![Image of Wiring](/images/bme.jpg)

Install all requirements to run via ```pip install -r requirements.txt``` 

Next install bme680 requirements  via ```pip3 install adafruit-circuitpython-bme680```

Next 


This project cannot be directly replicated from this repository but a brief tutorial can be found below. 
<h3> Flask WebPage </h3>

<h3> Google Firebase Database </h3>

<h3> Heroku-- Cloud Hosting </h3>

---------------------------------------------------------------------------------------------------------
# ---------------------------LABS-------------------------------
---------------------------------------------------------------------------------------------------------

<h2> Lesson 5 </h2>  

<h3> Lesson 5A  </h3>  

![Image of Lesson5A](/images/lesson5A.png)

<h3> Lesson 5B  </h3>  

![Image of Lesson5B](/images/lesson5B_hello.png)


![Image of Lesson5B](/images/lesson5B_CPU.png)

<h2> Lesson 6 </h2>  

<h3> Lesson 6A  </h3>  

![Image of Lesson6A](/images/lesson6A.png)  
  
![Image of Lesson6A](/images/Lesson6A2.png)  


<h3> Lesson 6B  </h3>  

![Image of Lesson6B](/images/lesson6B.png)
  
<h2> Lesson 7 </h2> 

<h3> Lesson 7B  </h3>  

![Image of Lesson7B](/images/lesson7B.PNG)

<h2> Lesson 8 </h2> 

<h3> Lesson 8A  </h3>  

![Image of Lesson8A](/images/lesson8A.png)
  
![Image of Lesson8A_titanic](/images/lesson8A_titanic.png)

<h3> Lesson 8B </h3>

I was unable to set this up properly, I was have issues sending over the .csv file unfortunately. 

<h2> Lesson 9 </h2> 

<h3> Lesson 9A </h3>  

![Image of Lesson9A](/images/lesson9A.png)

<h3> Lesson 9B </h3>  

![Image of Lesson9B](/images/lesson9B.png)

<h2> Lesson 10 </h2> 

<h3> Lesson 10A </h3>  

![Image of Lesson10A](/images/Lesson10A-1.png)
![Image of Lesson10A](/images/Lesson10A-2.png)
![Image of Lesson10A](/images/Lesson10A-3.png)
![Image of Lesson10A](/images/Lesson10A-4.png)

<h3> Lesson 10B </h3>  

![Image of Lesson10B](/images/Lesson10B.png)

