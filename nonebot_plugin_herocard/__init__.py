from nonebot.plugin.on import on_regex
try:
    from nonebot.adapters.onebot.v11 import Bot, Event  # type: ignore
    from nonebot.adapters.onebot.v11.event import (  # type: ignore
        MessageEvent,
    )
except ImportError:
    from nonebot.adapters.cqhttp import Bot, Event  # type: ignore
    from nonebot.adapters.cqhttp.event import (  # type: ignore
        MessageEvent,
    )
import re
def hero(text):
    # text = test_text
    pattern = r"(?<=\])(.*?)(?=\[|\(|\.|\【|\。)"
    pattern2 = r"(?<=\))(.*?)(?=\[|\.|\【|\。)"
    pattern3 = r"(?<=\.)(.*?)(?=\[|\.|\【|\。|\()"
    pattern4 = r"(?<=\。)(.*?)(?=\[|\.|\【|\。|\()"

    patterns = [pattern, pattern2, pattern3, pattern4]

    for p in patterns:
        result = re.search(p, text)
        if result and result.group() != ' ':
            return (result.group().strip())

hero_assistant = on_regex(r"あ|い|う|え|お|か|き|く|け|こ|さ|し|す|せ|そ|た|ち|つ|て|と|な|に|ぬ|ね|の|は|ひ|ふ|へ|ほ|ま|み|む|め|も|や|ゆ|よ|ら|り|る|れ|ろ|わ|を|ん|ア|イ|ウ|エ|オ|カ|キ|ク|ケ|コ|サ|シ|ス|セ|ソ|タ|チ|ツ|テ|ト|ナ|ニ|ヌ|ネ|ノ|ハ|ヒ|フ|ヘ|ホ|マ|ミ|ム|メ|モ|ヤ|ユ|ヨ|ラ|リ|ル|レ|ロ|ワ|ヲ|ン", priority=50, block=True)

@hero_assistant.handle()
async def test_handle(bot:Bot, event: MessageEvent):

    if text := event.get_plaintext():
        text_list = []
        # 按照空白行分割文本成多个段落，排除包含空白字符的段落
        raw_text_list = text.split('\n')
        raw_text_list = [paragraph.strip() for paragraph in raw_text_list if paragraph.strip()]
        # 循环遍历 text_list 中的内容
        for text in raw_text_list:
                edit_text = re.sub(r'#\((呵呵|哈哈|吐舌|啊|酷|怒|开心|汗|泪|黑线|鄙视|不高兴|真棒|钱|疑问|阴险|吐|咦|委屈|花心|呼~|笑眼|冷|太开心|滑稽|勉强|狂汗|乖|睡觉|惊哭|生气|惊讶|喷|爱心|心碎|玫瑰|礼物|彩虹|星星月亮|太阳|钱币|灯泡|茶杯|蛋糕|音乐|haha|胜利|大拇指|弱|OK|瓜|翔|吓|帅|小乖|捂嘴笑|你懂的|what|酸爽|呀咩爹|笑尿|挖鼻|犀利|小红脸|懒得理|沙发|手纸|香蕉|便便|药丸|红领巾|蜡烛|三道杠|暗中观察|吃瓜|喝酒|嘿嘿嘿|噗|困成狗|微微一笑|托腮|摊手|柯基暗中观察|欢呼|炸药|突然兴奋|紧张|黑头瞪眼|黑头高兴)\)', '', text)
                text_list.append(edit_text)
        for text in text_list:
            msg = hero(text)
            # print(msg)
            await hero_assistant.finish(str(msg))
    else:
        await hero_assistant.finish("呜...出错了，前后加个'。'再试试？")
