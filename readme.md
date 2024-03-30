# rk_website 问答仓库 学习
---

### 快速使用
git clone https://github.com/RKwork85/rk_website.git


在本地开启数据库服务后
修改配置文件rk_website/config 
6 7 8 行设置为本地数据库服务:用户名：密码：连接的数据库

```
cd rk_website

# 安装必要依赖，python3.10

pip install -r requirements.txt

flask 

#数据库初始化

flask db init
flask db migrate
flask db upgrade

// 运行程序
python app.py 

```
即可
### 关于学习指南

> 1 因为本人有完整的git commit 记录,所以可以按照仓库的提交记录一步步进行学习；

> 2 本人的邮件配置服务没有关闭，请勿滥用



### 友情链接
[1 原知了问答github链接](https://github.com/MUC-NBM/zlktqa)

[2 官方视频教程](https://www.bilibili.com/video/BV17r4y1y7jJ/?spm_id_from=333.337.search-card.all.click&vd_source=e49a601b01caa7c68d00c886dc01dfcf)

