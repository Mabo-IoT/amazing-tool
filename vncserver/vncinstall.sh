#! /bin/sh

yum localinstall -y tigervnc-server-1.3.1-9.el7.x86_64.rpm;
cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:1.service;
sed -i -e 's|/home/<USER>|/root|' /etc/systemd/system/vncserver@:1.service;
sed -i -e 's|<USER>|root|' /etc/systemd/system/vncserver@:1.service;
systemctl daemon-reload;
firewall-cmd --permanent --add-service vnc-server;
firewall-cmd --coplete-reload;
systemctl enable vncserver@:1;
echo "\nOK, let's start the vnc-server"
