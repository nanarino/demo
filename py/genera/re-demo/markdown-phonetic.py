#适配转换：text注音 转为 markdown/html注音
#"古(こ)川(がわ)" -> "<ruby>古<rp>(</rp><rt>こ</rt><rp>)</rp></ruby><ruby>川<rp>(</rp><rt>がわ</rt><rp>)</rp></ruby>"
#（）不需要第二个参数；()需要加第二个参数True
#注音：只适用于单汉字
import re


def to_ruby(shift):
    def up_ruby(r):
        r = r.group("kannji")
        ret = re.search([r'(?<=（).*(?=）)', r'(?<=\().*(?=\))'][shift],
                        r).group()
        return "<ruby>%s<rp>(</rp><rt>%s</rt><rp>)</rp></ruby>" % (r[0], ret)

    return up_ruby


def format_ruby(text, shift=False):  #true英文半角括号
    return re.sub(
        r'(?P<kannji>[\u4e00-\u9fa5]' + [r'（.*?）)', r'\(.*?\))'][shift],
        to_ruby(shift), text)
