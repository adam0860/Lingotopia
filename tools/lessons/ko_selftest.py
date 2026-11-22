"""Self-test for ko_rom: every sound change the KBC Introductory Unit prints (Appendix) plus the standard
cases that the rules are written for. The Korean build runs this first and stops if anything is wrong,
so a change to the engine can never silently change a lesson."""
import re

import ko_rom as K

COUNT = 0

# (spelling, pronunciation) -- printed in the book (Appendix 1, Lesson 5/6 rules)
BOOK = """입니다 임니다
앞문 암문
받는다 반는다
끝나요 끈나요
뒷문 뒨문
있나요 인나요
젖는 전는
몇 명 면 명
낳는다 난는다
석면 성면
부엌문 부엉문
깎는 깡는
담력 담녁
궁리 궁니
난로 날로
칼날 칼랄
백로 뱅노
섭리 섬니
한여름 한녀름
꽃잎 꼰닙
길 이름 길 리름
서울역 서울력
학교 학꾜
있다 읻따
국밥 국빱
학생 학쌩
학장 학짱
비빔밥 비빔빱
물가 물까
월부 월부
팔고 팔고
단발 단발
헌병 헌병
않고 안코
넣다 너타
좋지 조치
각하 가카
받히다 바치다
입학 이팍
꽂히다 꼬치다
굳이 구지
같이 가치
닫혀요 다쳐요
신라 실라
삶으세요 살므세요
많아요 마나요
맑게 말께
몫 목
밟 밥"""

# standard Korean pronunciation (Standard Pronunciation Rules, 표준 발음법)
STANDARD = """좋아요 조아요
읽어요 일거요
없어요 업써요
있어요 이써요
앉아요 안자요
읽고 일꼬
읽다 익따
넓다 널따
앉다 안따
젊다 점따
밖에 바께
부엌에 부어케
꽃이 꼬치
옷을 오슬
집에 지베
몫이 목씨
값이 갑씨
싫어요 시러요
싫네 실레
놓는 논는
한국어 한구거
국물 궁물
먹는 멍는
종로 종노
앞에 아페
닭 닥
삶 삼
읊어 을퍼
핥아 할타
놓치다 노치다
어떻게 어떠케
괜찮아요 괜차나요
맛있어요 마시써요
맛없어요 마덥써요
십육 심뉵
육십육 육씸뉵
열여섯 열려섣
열일곱 열릴곱
열여덟 열려덜
스물여섯 스물려섣
서른일곱 서른닐곱
마흔여덟 마흔녀덜
아흔여섯 아흔녀섣
열아홉 여라홉
서른아홉 서르나홉
칠십육 칠씸뉵
넓히다 널피다
앉히다 안치다
밟다 밥따
싫다 실타
옳다 올타
많다 만타
않는 안는
끓이다 끄리다
잃어요 이러요
읽히다 일키다
값 갑
없다 업따
닫다 닫따
곧이 고지
밭이 바치
해돋이 해도지
묻히다 무치다
학교에서 학꾜에서"""

# Revised Romanization of how the word is said
RR = """한글 hangeul
서울 seoul
김치 gimchi
감사합니다 gamsahamnida
안녕하세요 annyeonghaseyo
의사 uisa
가져요 gajeoyo
쪄요 jjeoyo
학교 hakgyo
입니다 imnida
신라 silla
좋지 jochi
같이 gachi
한국어 hangugeo
밖에 bakke
있어요 isseoyo
없어요 eopseoyo
읽어요 ilgeoyo
많아요 manayo
이름 ireum
라면 ramyeon
나라 nara
칼날 kallal
꽃잎 kkonnip
색깔 saekkal
까마귀 kkamagwi
어머니 eomeoni
아버지 abeoji
고맙습니다 gomapseumnida
괜찮아요 gwaenchanayo
뭐예요 mwoyeyo
왜 wae
외국 oeguk
위 wi
쉬어요 swieoyo
점심 jeomsim
십육 simnyuk
육십육 yuksimnyuk
열여섯 yeollyeoseot
서른일곱 seoreunnilgop
좋아요 joayo
싫어요 sireoyo
앉아요 anjayo
넓어요 neolbeoyo
닭 dak
삶 sam
읊어 eulpeo
핥아 hata
얼음 eoreum
달이 dari
강아지 gangaji
먹어요 meogeoyo
학생 haksaeng
국밥 gukbap
몇 시 myeot si
책 chaek
물 mul
밥 bap
꽃 kkot
빵 ppang
딸 ttal
짜장면 jjajangmyeon
쌀 ssal
뜨거워요 tteugeowoyo
의자 uija
회사 hoesa
사과 sagwa
요리 yori
유럽 yureop""".replace("핥아 hata", "핥아 halta")


def run():
    global COUNT
    bad = []
    for line in BOOK.split("\n") + STANDARD.split("\n"):
        # the spelling and the pronunciation are separated by one space; a phrase has one space inside each half
        m = re.match(r"^(\S+(?: \S+)?) (\S+(?: \S+)?)$", line)
        parts = line.split(" ")
        if len(parts) == 2:
            w, exp = parts
        elif len(parts) == 4:
            w, exp = " ".join(parts[:2]), " ".join(parts[2:])
        else:
            raise ValueError(line)
        COUNT += 1
        got = K.pron(w)
        if got != exp:
            bad.append(f"pron({w!r}) = {got!r}, expected {exp!r}")
    for line in RR.split("\n"):
        m = re.match(r"([^a-z]+?)\s+([a-z ]+)$", line)
        w, exp = m.group(1), m.group(2)
        COUNT += 1
        got = K.romanize(w)
        if got != exp:
            bad.append(f"romanize({w!r}) = {got!r}, expected {exp!r}")
    # compose / decompose round trip over every syllable
    for o in range(0xAC00, 0xD7A4):
        ch = chr(o)
        l, v, t = K.decompose(ch)
        if K.compose(l, v, t) != ch:
            bad.append(f"round trip {ch}")
            break
    COUNT += 1
    return bad
