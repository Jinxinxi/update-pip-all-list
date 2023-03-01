# coding = utf-8
import os
import time
import sys
import speedtest as st
import pywifi
import configparser

# 分隔符
print('=' * 50)
# 检测python版本
try:
    os.popen("python --version").readlines()
    if True:
        print("python状态：已安装")
        print(f"python版本号：{sys.version}")
except:
    print("python状态：\033[31m未安装或安装错误\033[0m")

# 分隔符
print('=' * 50)


# 获取登录的用户名
def login_user():
    user_name = os.getlogin()
    return user_name


print(f"计算机用户名：\033[33m{login_user()}\033[0m")
time.sleep(1)

# 分隔符
print('=' * 50)


# 判断是否已经连接到WIFI
def gie():
    # 创建一个无线对象
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    print("获取网卡中......")
    ifaces = wifi.interfaces()[0]
    time.sleep(2)
    # 打印网卡的名称
    print(f"网卡名称：{ifaces.name()}")
    # 打印网卡的连接状态  未连接：0  已连接：4
    if ifaces.status() == 4:
        print("网络状态：已连接到网络!")
    elif ifaces.status() == 0:
        print("网络状态：未连接到网络!")
        exit()
    else:
        print("网络状态：\033[31m网络异常！\033[0m")
        exit()


gie()

# 检测pip源
print("正在检测您连接的pypi源......")
conf = configparser.ConfigParser()
path = f"C:/Users/{login_user()}/AppData/Roaming/pip/pip.ini"
conf.read(path)
index_url = conf.get("global", "index-url")
if index_url == 'https://pypi.org/simple':
    print("当前pypi源：pypi官方源")
    time.sleep(3)
else:
    print("当前pypi源：\\")

# 开始测网速
print("正在测试网速！！！请稍后......")


# 转换速度单位
def speed_unit(bytes):
    unit = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while bytes >= 1024 and i < len(unit) - 1:
        bytes /= 1024
        i += 1
    j = ('%.2f' % bytes).rstrip('0').rstrip('.')
    return '%s %s' % (j, unit[i])


spt = st.Speedtest()  # 调用Speedtest类
download_speed = speed_unit(spt.download())  # 测试下载速度
print("您的当前下载网速为：", download_speed)


# 更改pip源
def change_pip():
    conf.set("global", "index_url", "https://pypi.tuna.tsinghua.edu.cn/simple")
    print("当前pypi源：清华源")


# 判断是否换源
if spt.download() <= 524288000:
    print("当前网速较慢，将为你换源.....")
    change_pip()
else:
    print(end='')
# 分隔符
print('=' * 50)


# 开始检查并更新
def pip_update():
    print("开始检查可以更新的库名......")
    model_ls = os.popen('pip list -o').readlines()
    print("可升级的库有:")
    list = [i.split()[0] for i in model_ls[2:-1]]
    s_list = [list[j: j + 1] for j in range(0, len(list), 1)]
    print(''.join(str(x) for x in s_list), end='')
    print('\r')
    for item in list:
        if not item.startswith("\\x") and item != 'pip':
            try:
                print('-' * 100, f'开始升级库:{item}', sep='\n')
                os.system(f"pip install --upgrade {item}")
                print(f"{item}更新完毕！！！")
            except:
                print(f"升级错误:{item}，可以尝试重新更新!!!")


pip_update()
# 分隔符
print('=' * 50)

# end
print("更新完毕，等待3秒后会自动关闭该窗口!")
time.sleep(3)
exit()
