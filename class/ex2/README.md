# python类的继承

## 文件说明
### car.py
一个汽车的父类,其中有一个打印汽车信息的方法
### electric_car.py
电动汽车子类,其中包含父类的属性,多了一个电池信息,和一个打印电池信息的方法.
### main.py
运行文件用来观测结果
## 运行方式
```bash
python main.py
```

## 注意事项
1. 在python2.7中在继承的时候类要指明继承关系才可以,原始的类要继承Object类才行不然子类在继承的过程中会爆错:Error: super() argument 1 must be type, not classobj  
