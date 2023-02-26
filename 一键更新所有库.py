# coding = utf-8
import os
import time


def pip_update():
    model_ls = os.popen('pip list -o').readlines()
    print("开始检查可以更新的库名......")
    list = [i.split()[0] for i in model_ls[2:-1]]
    print(f"可升级的库有:{list}")
    for item in list:
        if not item.startswith("\\x") and item != 'pip':
            try:
                print('-' * 100, f'开始升级库:{item}', sep='\n')
                os.system(f"pip install --upgrade {item}")
                print(f"{item}更新完毕！！！")
            except:
                print(f"升级错误:{item}，可以尝试重新更新!!!")


if __name__ == '__main__':
    pip_update()
    print("更新完毕，等待3秒后会自动关闭该窗口!")
    time.sleep(3)
    exit()
