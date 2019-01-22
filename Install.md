
Install selenium supported WebDriver

# For mozilla
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz

# For chromedriver
wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_mac64.zip
tar xvfz chromedriver_mac64.zip
mv chromedriver /usr/local/bin/
/usr/local/bin/chromedriver -v
pip3 install selenium

mv geckodriver ~/.local/bin
