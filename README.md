# lcd_project
Code to control 16x2 LCD screen through I2C

This code only works in Linux and make sure that I2C is enabled, and Python 3.x is installed.
I2C support may already be enabled on your device, but if not, you'll need to look up how to do so depending on what device you are using.

I wrote this code to display the date, time, and weather on the LCD screen.

The main point of this code is to demonstrate how anyone can access an API through Python, format the data, and show two lines of text on a 16x2 LCD.

1) Check out this project.
2) Download https://gist.github.com/DenisFromHR/cc863375a6e19dce359d and place it in the same folder as where the code will reside.
3) Move the updateLCD.service and updateLCD.timer files to the systemd directory on your device. 
   In Arch Linux, the systemd service folder is under /usr/lib/systemd/system/
   In Ubuntu, the systemd service folder is under /lib/systemd/system
4) Change the path for the ExecStart line in the updateLCD.service file to match the path of where you will be placing the updateTimeandWeather.py file.
5) Move the 10-i2c-perms.rules if needed for your device to /etc/udev/rules.d folder. Make sure to go in and change OWNER= to whichever user will be running the code. In my case, I was using Ubuntu on a Rock64, and the default user was rock64.
6) Make sure to enable the timer which runs the python every minute by typing the following command: "systemctl enable updateLCD.timer"
7) You can increase and decrease the interval in which the timer runs the Python script. You can either search for systemd.timer or type in man systemd.timer to get more instructions on how to do this.
8) If you plan on displaying the weather on your LCD like me, sign up for an API key from a company that provides weather information. I used openweathermap since it was free, but feel free to use something else if you prefer. Make sure to change put in your zip code in the updateTimeAndWeather.py file in the url where it says {insert_zip_code_here}, and the API key with {insert_api_key_here}
9) Fingers crossed, you'll see the date, time, and weather info on your screen.

Happy coding !
