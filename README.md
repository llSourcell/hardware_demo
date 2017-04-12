# hardware_demo


# voyeur

This is the code for [this](https://www.youtube.com/watch?v=YKtbO6iW9-Y) video by Siraj Raval on Youtube.
Voyuer is the code used to control a robotic Venetian blind. It consists of a Raspberry Pi 3, a camera and screen to display the camera output. It using OpenCV to control a servo to close a Venetion blind when it detects a face and open a Venetian blind when it doesn't detect a face.

The goal of the work is to question how we interact with technology. Is looking at our screens similar to looking through windows? What permission do we have to look through these windows? Who is controlling what we see through these screens? What happens if the screens react to our presence?

_NOTE: The project is still in development and this code/instructions are for a very early prototype._

## Materials
  * [Raspberry Pi Model 3](https://www.adafruit.com/products/3055)
  * [Pi Cobbler and Breakout Cable](https://www.adafruit.com/products/2029)
  * [Breadboard](https://www.adafruit.com/product/239)
  * [5V Power Supply](https://www.adafruit.com/products/1995)
  * [Pibow Case](https://www.adafruit.com/products/2083)
  * [Raspberry Pi Camera](https://www.adafruit.com/products/3099)
  * [Raspberry Pi Camera Case](https://www.adafruit.com/products/3253)
  * [Continuous Rotation Servo](https://www.adafruit.com/products/154)
  * [Jumper Wires](https://www.adafruit.com/products/758)

## Construction

### Setup/Install Required Software
This installs OpenCV from a binary. The version is a bit outdated and only has python2 bindings, but I've found that having an outdated version is much easier than having to compile OpenCV from source. PyImageSearch has a tutorial if you'd like to try and [install OpenCV and the python3 bindings from source](http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/).
```
sudo apt-get install opencv
```

Install pigpio library to interface with the gpio pins.
```
sudo apt-get install pigpio
```

Start pigpio daemon process so the library can communicate with the gpio pins.
```
sudo pigpiod
```

### Setup Harware
  1. Connect and configure the camera module to the Rasberry Pi. [Tutorial](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/)
  2. Connect the Pi cobbler and breakout cable to the GPIO pins on the Raspberry Pi on one end and the breadboard on the other.
  3. Using the breadboard, connect the servo to the Raspberry Pi GPIO pins. Since we are powering only a single servo, we're connect the servo directly to the Raspberry Pi. The servo is controlled via Pulse Width Modulation (PWM) signals driven in software by the `pigpio` library. Connect the red cable on the servo to the 5V pin on the Pi, the brown cable to the GND pin on the Pi, and the yellow cable to pin 18 (the pin we'll use to send the PWM signal) on the Pi. [Reference](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor/hardware).
  4. Attach the servo to the blind openning/closing mechanism. I strung a piece of wire through the top of the servo to twist the blinds open/close when the servo turns.

### Putting it all together
Now with all the requisite software + hardware, you can use the code in this repo to control the blinds! Clone this repo and you should be ready to go!

Be forewarned, the code here is still very rough. Before optimizing I wanted to get this working end-to-end so the blind control code has no safeguards in place to prevent the blinds from getting damaged if they're not in the expected state. e.g. the main code expects the blinds to start open, if they don't the code might think the blinds are in one state, but actually be in another.

Another thing I'm not proud of right now is shelling out to the `pigs` command line tool to send the PWM signals to the servo. In my haste to get the prototype working, I had some trouble working with the pigpio python bindings directly, but was able to use the command line tool without problems.

## Resources
PWM software control on the Pi
  * [pigpio library/resources](http://abyz.co.uk/rpi/pigpio/index.html)
  * [pigpio servo control command](http://abyz.co.uk/rpi/pigpio/pigs.html#S/SERVO)

PyImageSearch Python OpenCV Tutorials
  * [PyImageSearch face detector in 5 minutes](http://www.pyimagesearch.com/2015/05/11/creating-a-face-detection-api-with-python-and-opencv-in-just-5-minutes/)
  * [PyImageSearch increase Pi camera FPS fps](http://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/)
  
# Credits

Credits go to [Etan](https://github.com/etanzapinsky) and Siraj
