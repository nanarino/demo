# 注意

本脚本兼容2或3层DOM树结构的【饿了么】的【药店类店铺】

Windows下写入的csv文件默认会用gbk编码，

由于可能出现的`UnicodeEncodeError`导致数据行丢失

（纯属推测，依然使用了try语句捕获写入时可能遇到的所有错误）

所以可以使用utf8编码规避，修改代码如下：

```python
#Windows下默认即为gbk：
csvFile = open("qs_%s.csv"%shop_id, "w")#, encoding='utf-8')
#指定为utf8：
csvFile = open("qs_%s.csv"%shop_id, "w", encoding='utf-8')
```

但是使用utf8编码也有缺陷，这将会导致在Windows系统上使用Office时打开csv文件乱码。



时间：2019年9月22日21:17:09

部分测试用店铺ID列表：

```python
[2233310913, 2231728687, 2231728687]
```

