# Samurai,a simple framework
##开发环境
###准备

```buildoutcfg
# git clone
git clone git@github.com:MartinChenjq/samurai.git
# cd root
cd samurai/
# 建虚环境
virtualenv venv --python=python3.9
source venv/bin/activate
# 装包
pip install -r requirements.txt
# dev mode
FLASK_ENV=development FLASK_APP=samurai.app:app flask run



```
### [huey](https://huey.readthedocs.io/en/latest/) ,a simple task queue 
```buildoutcfg
# run task 
huey_consumer.py samurai.task.huey
```

### [redis](https://redis.io/download) 安装
```buildoutcfg
# download
mv /usr/local/
cd /usr/local/redis-6.2.5/
make
sudo make install
redis-server
```

### [pytest](https://docs.pytest.org/en/6.2.x/)
尽量使用pytest做单元测试

```commandline
pytest
```



## 测试环境
```buildoutcfg
参考开发环境
```

## 生产部署
* 单独部署
* 容器部署
```buildoutcfg

```