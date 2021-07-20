# dvwapypoc
1.lowbrute.py 运行成功截图
![Image text]( https://github.com/guiyue/dvwapypoc/blob/main/1626415280(1).png)
2.high_token1.py运行成功截图
![Image text]( https://github.com/guiyue/dvwapypoc/blob/main/2.jpg)
3.high_token2.py运行成功截图
![Image text]( https://github.com/guiyue/dvwapypoc/blob/main/2.jpg)
脚本token1和token2的区别在于：如何提取出token值。
  token1：使用bs4的findall查找标签并提取出来；当然使用正则更好
   rt = soup1.find_all(type="hidden")
    token = rt[0].attrs["value"]
  token2:使用selector的css选择器
      selector = parsel.Selector(response1.text)
    rt=selector.css('input')
    # rt2=selector.css('input:nth-child(9)::attr(value)')
    # print(rt.extract())
    # print(rt2.extract_first())
    rt=selector.css('input::attr(value)')
