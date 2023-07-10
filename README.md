<h1 align="center">NoneBot Plugin HeroCard</h1></br>

<p align="center"> 用于提取本子😇标题关键词的 NoneBot2 插件</p></br>

<p align="center">
  <a href="https://pypi.python.org/pypi/nonebot-plugin-herocard">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/nonebot-plugin-herocard?color=%23da3f3d">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue?style=flat" alt="python">
  <br />
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
- 发送 `(2020 Summer)テーマ(subtitle) [中国翻訳] (31P)(完)`格式消息即可收到回复

_\* 插件响应基于正则匹配，所以，甚至`朋友#(阴险)  你现在还求吗？还得是禾野吧老哥，回馈lz[作者さん]テーマ (31P)我感觉很顶`这样的指令都可用！_

- **注意：**
  1.  发送消息中**一定**要包含**日文假名**，不论 _平假名_ 还是 _片假名_ ，否则插件不生效
  2.  若出现`None`回复或是`不回复`，可以考虑在您**想要提取文本**的前后加上`。`/`.` =>中英文句号均可
  3.  标题中带**贴吧表情**（eg.😅🥵）的会自动删除

<details>
<summary><b>使用示例【图】<b></summary>
<img decoding="async" loading="lazy" src="https://github.com/Xie-Tiao/My-Imgurl/blob/main/nonebot_plugin_herocard_1.jpg"  width="216" height="710" >

</details>
  
---
 
  
**特别鸣谢**

[@nonebot/nonebot2](https://github.com/nonebot/nonebot2/) | [@monsterxcn/nonebot_plugin_epicfree](https://github.com/monsterxcn/nonebot_plugin_epicfree) | [@initialencounter/nonebot-plugin-cube](https://github.com/initialencounter/nonebot-plugin-cube/tree/main)

> 新人ざぁこ ♡ 一枚，代码写的烂，最好别指望我能修什么 bug！Ciallo ～(∠・ω< )⌒☆

**更新日志**

`1.0.5` 修复了已知bug

`1.0.4` 修复了不能回复多条消息的问题，以及消除贴吧表情后自带空格的 bug

`1.0.3` 修改了编译问题

`1.0.2` 修复一点 README.md 问题

`1.0.1` 修复一点 README.md 问题

`1.0.0` 首次发布，完善了 README.md
