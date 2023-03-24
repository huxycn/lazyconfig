from lazyconfig import LazyConfig, instantiate


cfg = LazyConfig.load('./demo/a.py')

print('cfg:', cfg)

cfg.a = instantiate(cfg.a)

print('a:', cfg.a)

# print('b:', cfg.b)

# print('c:', cfg.c)


# cfg = LazyConfig.load(self.root_filename)
# cfg.lazyobj.x = {"a": 1, "b": 2, "c": L(count)(x={"r": "a", "s": 2.4, "t": [1, 2, 3, "z"]})}
# cfg.list = ["a", 1, "b", 3.2]
# py_str = LazyConfig.to_py(cfg)
