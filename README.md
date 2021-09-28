# 生成requirements
pip freeze > requirements.txt

# 安装requirements依赖包
pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn

# 安装单个包
pip --default-timeout=1000 install -U 模块名  -i https://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn