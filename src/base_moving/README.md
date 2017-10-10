#####底盘运动功能包说明######

1. base包为驱动底盘的功能包

2. mv_base_v01包为控制底盘停和走的功能包

3. driver文件夹为底盘驱动，插上底盘前先进如driver文件夹执行 sudo ./install.sh 安装驱动

4. 然后插上底盘，确认底盘接口为ttyUSB几，运行：rosrun spark_base spark_base_node /dev/ttyUSB0

5. 最后运行： rosrun mv_base_v01 listen_cmd 节点监听其他节点发过来的停或走命令

6. 当其他节点在话题base_control上发布消息时，底盘即可做出走或停的动作
