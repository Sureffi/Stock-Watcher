from stocks import Stocks
from newsparser import NewsParser
from messenger import Messenger

STOCK = "tsla"
COMPANY_NAME = "Tesla"

API_KEY_STOCKS = ''                 #Use https://www.alphavantage.co
API_KEY_NEWS = ''                   #Use https://newsapi.org

TWIOLIO_SID = ''                    #Use https://www.twilio.com
TWILIO_TOKEN = ''
TWILIO_PN = ''

TO_NUMBER = ''



news = NewsParser(API_KEY_NEWS)
stock = Stocks(API_KEY_STOCKS)
messenger = Messenger(TWIOLIO_SID, TWILIO_TOKEN, TWILIO_PN, TO_NUMBER)    

def create_message(change):
    top_news = news.get_news(COMPANY_NAME)
    
    if change < 0:
        message = f"{STOCK.upper()}: 🔻{str(change).strip('-')}%\n-------------------\n"
    else:
        message = f"{STOCK.upper()}: 🔺{change}%\n-------------------\n"
    
    for article in top_news:
        message += (f"Headline: {article['headline']}\n"
                    f"Brief: {article['brief']}\n"
                    f"Link: {article['link']}\n-------------------\n")
    return message


if __name__ == '__main__':
    change = stock.difference(STOCK)    
        
    message = create_message(change)

    messenger.message(message)
