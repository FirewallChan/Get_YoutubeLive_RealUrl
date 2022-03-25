# Get_YoutubeLive_RealUrl
获取Youtube直播的真实链接（HLS格式的M3U8

说来惭愧，只是做了些微小的工作
（获取直播状态的部分是从StackOverflow上找到的思路，获取直播地址则是用调用现成的命令行程序）

这个Python文件需要requests和youtube-dl这两个python程序，通过pip安装即可。
注意：在同一频道有多个直播同时开始的情况下，你只能获取到第一个直播间的地址，因为本程序使用的是频道，而非直播地址来获取真实的直播地址。
艹，好绕啊。总归就是碰到同频多播的情况就麻爪了。

2022.03.25更新  
这个项目和AutoStreamUrls合并了，另外一个项目多出了还可以抓取bilibili直播源的功能  
另外还优化了Youtube抓取的代码  
详细见另外一个项目的ReadME.md
