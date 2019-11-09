#!/bin/bash

clear
sleep 1
echo "Loading..." | lolcat
sleep 2
clear
echo "welcome" | lolcat
sleep 2
clear
echo"==========================================
author : BLANK
Github : https://github.com/hacksidrap
Facebook : ananta poetra sidrap
==============================================="

###########################################
# CTRL + C
###########################################
trap ctrl_c INT
ctrl_c() {
clear
echo "[#] detected ctrl+c exit...."
echo "[#] JANGAN SALAH GUNAKAN TOOLS INI"
sleep 1
echo''''
echo "[#] BLACK"

echo "thanks..."
sleep 1
exit
}

lagi=1
while [$lagi -it 3 ];
do
echo''''
echo''''
echo "1. hack fb" | lolcat
echo "-----------------------------------------" | lolcat
echo "2. hack camera" | lolcat
echo "-----------------------------------------" | lolcat
echo "3. deface" | lolcat
echo "----------------------------------------" | lolcat
echo "00. exit" | lolcat
echo''''
read -p "pilih no : " pill;

case $pill in
1)clear
git clone https://github.com/hacksidrap/fbbrute
cd fbbrute
pip2 install mechanize
python2 force.py

;;

2)clear
git clone https://github.com/hacksidrap/camera
cd camera
sh camera.sh

;;

3)clear
git clone https://github.com/hacksidrap/deface
cd deface
sh tebas.sh

;;

00)clear
echo " add my Facebook ananta poetra sidrap"
exit
;;

esace
done
done

