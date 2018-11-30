# RPI HOME AND TELEGRAM CONTROL BOT
The implementation is a prototype of a smart home system with a integrated chat-bot using telegram.
The video of the implementation is here  -->  https://youtu.be/wNByyyrFuyQ

### Pre-requiste
1) RasberyPi Model B
2) Telegram Program Pre-install. 
3) OpenCV Pre-install 

### Command to Start HomePi
    $ source ~/.profile
    $ workon cv
    $ ./0_homepi/Smart-Security-Camera/main.sh

### Command to activate Telegram BOT
    cd tg
    bin/telegram-cli -k tg-server.pub -W -s  actions.lua

