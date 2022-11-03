# test that load_rel can work
from lazyconfig import LazyConfig

x = LazyConfig.load_rel("dir1_a.py", "dir1a_dict")
assert x["a"] == 1
