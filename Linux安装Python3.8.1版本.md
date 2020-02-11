Linux环境下安装python3
安装步骤如下：

（１）wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz 下载安装包
（２）tar zxvf Python-3.6.3.tgz 解压安装包
（３）cd Python-3.6.3 转到该安装包目录下
（４）．/configure --prefix=/usr/local/python38 这一步及其重要，对安装进行配置，并指定安装路径，安装路径不指定的话不利于后面的系统管理
（５） make 编译
（６） make install 安装
默认输入python，还是python2.7，还需要建立软连接，使得系统默认的python版本是python3。有一点千万要记住，不要傻傻去卸载老版本，要不然后患无穷。
建立软连接：
（１）mv /usr/bin/python /usr/bin/python.bak
（２）ln -s /usr/local/python38/bin/python3.8 /usr/bin/python
这样配置之后，我们就会看到默认就是python38了
