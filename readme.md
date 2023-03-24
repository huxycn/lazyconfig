# lazyconfig

> Extract detetron2.config as a stand-alone util

## Install

```shell
pip install git+https://github.com/huxycn/lazyconfig.git
```

## Usage

- reference: https://detectron2.readthedocs.io/en/latest/tutorials/lazyconfigs.html


## 2023.03.24

- lazy.py line29: add positional arguments support [DONE]

```
python demo/main.py
```

- lazy.py line234: add int/float/str support failed [TODO]

```
FAIL: test_to_py (test_lazy_config.TestLazyPythonConfig)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/huxiaoyang/Desktop/lazyconfig/tests/test_lazy_config.py", line 80, in test_to_py
    self.assertEqual(py_str, expected)
AssertionError: 'cfg.[52 chars].dir1a_str = "base_a_1"\ncfg.dir1b_dict.a = 1\[273 chars]2]\n' != 'cfg.[52 chars].dir1b_dict.a = 1\ncfg.dir1b_dict.b = 2\ncfg.l[210 chars]2]\n'
  cfg.dir1a_dict.a = "modified"
  cfg.dir1a_dict.b = 2
- cfg.dir1a_str = "base_a_1"
  cfg.dir1b_dict.a = 1
  cfg.dir1b_dict.b = 2
- cfg.dir1b_str = "base_a_1_from_b"
  cfg.lazyobj = itertools.count(
      x={
          "a": 1,
          "b": 2,
          "c": itertools.count(x={"r": "a", "s": 2.4, "t": [1, 2, 3, "z"]}),
      },
      y="base_a_1_from_b",
  )
  cfg.list = ["a", 1, "b", 3.2]


----------------------------------------------------------------------
```
