1. 运行 `./vncinstall.sh'
2. 执行 `vncpasswd`
3. 启动 `systemctl start vncserver@:1`
4. 如果报错，运行 `rm -Rf /tmp/.X11-unix/`，后再次启动服务
