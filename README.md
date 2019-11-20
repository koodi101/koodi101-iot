# Koodi101  Internet of Things (IoT)

### Raspberry pi – first time setup
1. Login with **pi:raspberry** (or use ssh pi@\<ip\>)
2. Type ```sudo raspi-config```
3. Change the password for pi user to something else
4. Under network options, configure the wifi (if needed)
5. Under localization options, configure keyboard layout
6. Under interfacing options, enable **SPI** and **I2C**
7. Exit the raspi-config

RPI should now connect to wifi. You can check the ip address by typing
```hostname -I```

If you want to use ssh to connect to your RPI, you can do it by writing

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

Now you can connect from your own machine with ```ssh pi@<ip>``` if you are in the same network.

### Setting up the sensor

Enviro pHAT is an environmental sensing board that lets you measure temperature, pressure, light, colour, motion and analog sensors. It should be pre-set to a plug-and-play level, so no pin configuration is needed.

### Run the project

The Enviro pHAT developers have been generous enough to provide a one-line installer script that should be run inside the Raspberry Pi Zero. Just open a terminal and type the following into it (and type 'y' or 'n' when prompted):

```bash
curl https://get.pimoroni.com/envirophat | bash
```

First clone your forked version of this repository to the Rasperry pi and go to the iot folder

```bash
git clone <url>
```

You can now try our app by starting it with

```bash
ENDPOINT=http://you-server/api/temperature python3 rpi.py
```

### Starting the app automatically

One way to keep raspberry sending information without manual
work, is to use cron to run our script every minute.

That can be achieved by opening crontab editor by typing ```crontab -e```

Window will open and you can append the following line at end of the file,
of course replacing the endpoint with a correct one.

```bash
* * * * * ENDPOINT=http://you-server/api/temperature python3 /home/pi/koodi101-iot/iot/rpi.py >> /home/pi/rpi.log 2>&1
```

So what does this mean?

* **\* \* \* \* \*** ENDPOINT=http://you-server/api/temperature python3 /home/pi/koodi101-template/iot/rpi.py >> /home/pi/rpi.log 2>&1
  * When to run the script, *see below*

* \* \* \* \* \* **ENDPOINT=http://you-server/api/temperature** python3 /home/pi/koodi101-template/iot/rpi.py >> /home/pi/rpi.log 2>&1
  * Pass environmental variable for script to be executed

* \* \* \* \* \* ENDPOINT=http://you-server/api/temperature **python3 /home/pi/koodi101-template/iot/rpi.py** >> /home/pi/rpi.log 2>&1
  * Normal command to run a script with python

* \* \* \* \* \* ENDPOINT=http://you-server/api/temperature python3 /home/pi/koodi101-template/iot/rpi.py **>> /home/pi/rpi.log** 2>&1
  * **Append** output to a file

* \* \* \* \* \* ENDPOINT=http://you-server/api/temperature python3 /home/pi/koodi101-template/iot/rpi.py >> /home/pi/rpi.log **2>&1**
  * By default, error messages wouldn't be logged into the file. With this definition, we redirect the to standard output and therefore into the same file.

Cron works by comparing current time to parameters at the beginning of every line. If it matches, it will run the script.

Our example is run every minute, although it should match at anytime, why is it so? Well, cron runs only every minute, so that is why this will work and that is why we can't schedule it to run more often.

There exist cool tool to "translate" cron time entries into human readable form: [https://crontab.guru](https://crontab.guru)
