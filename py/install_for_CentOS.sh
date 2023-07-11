mkdir /home/download
cd /home/download
yum -y update
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
tar -xvf Python-3.7.2.tar.xz
cd Python-3.7.2
./configure --prefix=/usr/local/python3
make && make install
echo "[global]
index-url = https://pypi.doubanio.com/simple
trusted-host = pypi.doubanio.com" > ~/.pip/pip.conf
pip3 install --upgrade pip
