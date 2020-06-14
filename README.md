# Chuck it!
An interactive drinking game


## Shopping  list
- [10 Aviation 7-pin connectors and sockets](https://www.amazon.de/Clyxgs-Panelmontage-Aviation-M%C3%A4nnlich-Weiblich-Silber/dp/B07VJYPBHK/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=6%2Bpin%2Baviation&qid=1591522216&s=ce-de&sr=1-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVVJTUlI4UUQzOUMzJmVuY3J5cHRlZElkPUEwOTQyNzcyTUFCQ08yWDZNU1RBJmVuY3J5cHRlZEFkSWQ9QTAzMDc5NjUyNENUWlk1S1RHMUcmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1)
- [NeoPixel LEDS](https://www.ebay.de/itm/123868061007)


## Connecotr Pinout
- 1: 3.37
- 2: Data IN
- 3: Data OUT
- 4: Buttoun OUT
- 5: - free -
- 6: 5.0V
- 7: GND

# install Python 3.7
from https://gist.github.com/SeppPenner/6a5a30ebc8f79936fa136c524417761d

sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev uuid-dev -y

or in one line:

sudo apt-get update -y && sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y && wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz && tar xf Python-3.7.0.tar.xz && cd Python-3.7.0 && ./configure && make -j 4 && sudo make altinstall && cd .. && sudo rm -r Python-3.7.0 && rm Python-3.7.0.tar.xz && sudo apt-get --purge remove build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y && sudo apt-get autoremove -y && sudo apt-get clean

## Color Scheme
https://www.color-hex.com/color-palette/63697
