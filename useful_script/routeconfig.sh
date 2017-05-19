#! /bin/sh

i=0

for dev in `ip link | grep 'en' | cut -d ':' -f 2 | grep 'en' | cut -d ' ' -f 2`
do
    if [ $i = 0 ];then
        dev1=`echo $dev`
    fi


    if [ $i = 1 ];then
        dev2=`echo $dev`
    fi


    if [ $i = 2 ];then
        dev3=`echo $dev`
    fi

    let i=$i+1
    firewall-cmd --change-interface=$dev --zone=internal --permanent > /dev/null 2>&1;
done

while true
do
    echo "which dev is the export?($dev1, $dev2, $dev3)"
    read ex_dev

    if [ "$ex_dev" = "$dev2" ] || [ "$ex_dev" = "$dev1" ] || [ "$ex_dev" = "$dev3" ];then
    	firewall-cmd --direct --add-rule ipv4 nat POSTROUTING 0 -o $ex_dev -j MASQUERADE --permanet;
        break
    else
    	echo "no such dev"
    fi
done

grep "net.ipv4.ip_forward=1" /etc/sysctl.conf > /dev/null
if [ $? -ne '0' ];then
    echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf;
fi
firewall-cmd --set-default-zone=internal;
firewall-cmd --zone=internal --add-service=dns --permanent;
firewall-cmd --zone=internal --add-masquerade --permanent;
firewall-cmd --complete-reload;
