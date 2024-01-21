sudo apt-get install -y unixodbc unixodbc-dev
sudo apt-get inatall -y gpg
sudo apt-get install -y wget
sudo wget https://packages.snowflake.com/gpg-pubkey/snowflake-oss-debin.pub
sudo apt-key add snowflake-oss-debin.pub
sudo echo "deb http://packages.snowflake.com/debin/odbc/4.6.0/ubuntu/18.04 /" | sudo tee -a /etc/apt/sources.list.d/snowflake-odbc.list
sudo apt-get update 
sudo apt-get install -y snowflake-odbc
