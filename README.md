# DCousins_Charger

<p align="center">
  <img src="https://github.com/RecognitionDesigns/DCousins_Charger/blob/main/images/DC_Charger.jpg" width="500" title="Dan Cousins Charger">
</p>

This repo is for use with Dan Cousins DDL/ANKI Vector charger with built in fan and LEDs.
The charger requires a raspberry pi with GPIO pins installed to work to its fully potential.

The script runs the fan and LEDs using the built in IR detection module in the charger.
Install this script on your Raspberry Pi and make it executable and run at startup.

Make the script executable: 
  ```
  sudo chmod +x ir_detection.py
  ```
Use crontab to run the script at startup (there are other methods to do this but this is very easy):
  ```
  sudo crontab -e
  ```
Then enter this line a the bottom of the crontab file:
  ```
  @reboot /home/user/path-to-script/ir_detection.py
  ```

Connect the integrated wiring using the GPIO pin guide below (These pins will work with the supplied script, you can change these if you are already using the pins shown here):

<p align="center">
  <img src="https://github.com/RecognitionDesigns/DCousins_Charger/blob/main/images/GPIO_DC_Charger.png" width="420" title="GPIO Pin Out">
</p>

For more information you can find Dan Cousins at the Official Digital Dream Labs Vector Owners group page on Facebook:
https://www.facebook.com/groups/AnkiVector

Have fun!
