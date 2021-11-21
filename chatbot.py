from chatterbot import ChatBot
#from chatterbot import languages
import languages # 自作言語モジュール

bot = ChatBot(
        name='MyBot',
        tagger_language=languages.JPN # 日本語モデルを指定
        # tagger_language=languages.GINZA # GINZAモデルの場合
)