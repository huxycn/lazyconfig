from setuptools import setup, find_packages

setup(
    name='lazyconfig',
    version='0.0.1',
    author='huxiaoyang',
    author_email='545960442@qq.com',

    install_requires=[
        "cloudpickle",
        "pyyaml",
        "fvcore>=0.1.5,<0.1.6",  # required like this to make it pip installable
        "iopath>=0.1.7,<0.1.10",
        "omegaconf>=2.1",
        "hydra-core>=1.1",
        "black==22.3.0",
    ],

    packages=find_packages()
)
