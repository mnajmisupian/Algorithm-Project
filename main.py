# from Problem2 import problem2dhl as P2
from Problem2 import problem2 as P2
from Problem1 import p1Q1 as P1q1
from Problem1 import p1Q2 as P1q2
from Problem1 import p1Q4 as P1q4
import problem3 as P3
# from Problem3 import problem3 as P3

score = {}
COURIER_NAME = ["cityLE", "posLaju", "gdex", "jnt", "dhl"]


def webScrape():
    global score
    score[COURIER_NAME[0]] = P2.cityLink(
        "http://autoworld.com.my/news/2020/09/25/city-link-express-takes-delivery-of-277-new-isuzu-trucks/",
        "https://www.thestar.com.my/business/business-news/2015/01/05/citylink-mulls-main-market-listing-in-three-years",
        "https://www.thesundaily.my/gear-up/isuzu-lorries--city-link-s-preferred-choice-AK729310",
    )

    score[COURIER_NAME[1]] = P2.posLaju(
        "https://www.thestar.com.my/business/business-news/2021/02/22/pos-malaysia-records-rm233b-revenue-in-fy20",
        "https://soyacincau.com/2020/08/15/pos-malaysia-e-consignment-notes-qr-code-available/",
        "https://www.theborneopost.com/2020/07/08/poslaju-customers-urged-to-bear-with-longer-waiting-time/",
    )

    score[COURIER_NAME[2]] = P2.gdex(
        "https://www.theedgemarkets.com/article/gdex-stands-benefit-pickup-ecommerce-activities-says-kenanga-research",
        "https://www.theedgemarkets.com/article/gdex-look-creating-industrial-reit-part-next-growth-phase",
        "https://www.theedgemarkets.com/article/gdex-2q-net-profit-down-absence-gain-warns-covid19-impact",
    )

    score[COURIER_NAME[3]] = P2.jnt(
        "https://www.straitstimes.com/asia/se-asia/pandemic-fuelled-e-shopping-boom-spurs-courier-firms-growth",
        "https://www.theedgemarkets.com/article/indonesias-jt-express-said-weigh-us1-billionplus-us-ipo",
        "https://kr-asia.com/one-masters-two-apprentices-how-indonesias-jt-express-rose-in-china-on-the-back-of-pinduoduo",
    )

    score[COURIER_NAME[4]] = P2.dhl(
        "https://www.theedgemarkets.com/article/tech-digitalisation-way-forward-dhl-express",
        "https://www.theedgemarkets.com/article/dhl-predicts-strong-growth-b2b-ecommerce",
        "https://www.theedgemarkets.com/article/special-report-rocky-road-ahead-logistics-operators-amid-pandemic",
    )



P1q1.start()
P1q2.start()
P1q4.start()
# webScrape()
# P3.start(score)