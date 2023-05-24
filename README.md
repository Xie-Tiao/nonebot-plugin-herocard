<h1 align="center">NoneBot Plugin HeroCard</h1></br>

<p align="center"> 用于提取本子🥵标题关键词的 NoneBot2 插件</p></br>

<p align="center">
  <a href="https://pypi.python.org/pypi/nonebot-plugin-herocard">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/nonebot-plugin-herocard?color=%23da3f3d">
  </a>
  <img src="https://img.shields.io/badge/python-3.9-blue?style=flat" alt="python"><br />
</p></br>

**安装方法**

使用以下命令之一快速安装：

``` 
nb plugin install nonebot-plugin-herocard

pip install --upgrade nonebot-plugin-herocard
```
重启 Bot 即可体验此插件。

**使用方法**

 - 发送 `[作者さん]テーマ[中国翻訳] [DL版]`格式消息即可收到回复
 - 发送 `(2020 Summer)テーマ(subtitle) (31P) (完)`格式消息即可收到回复

*\* 插件响应基于正则匹配，所以，甚至`回馈lz[作者さん]テーマ (31P)我感觉很顶`这样的指令都可用！*
- **注意：** 
  1.  发送消息中**一定**要包含**日文假名**，不论 *平假名* 还是 *片假名* ，否则插件不生效 
  2.  若出现`None`回复或是`不回复`，可以考虑在您**想要提取文本**的前后加上`。`/`.` =>中英文句号均可


**特别鸣谢**

[@nonebot/nonebot2](https://github.com/nonebot/nonebot2/) | [@Mrs4s/go-cqhttp](https://github.com/Mrs4s/go-cqhttp) | [@monsterxcn/nonebot_plugin_epicfree](https://github.com/monsterxcn/nonebot_plugin_epicfree) 


> 新人ざぁこ♡一枚，代码写的烂，最好别指望我能修什么bug！Ciallo～(∠・ω< )⌒☆

**更新日志**

`1.0.2` 修复一点README.md问题

`1.0.1` 修复一点README.md问题

`1.0.0` 首次发布，完善了README.md
