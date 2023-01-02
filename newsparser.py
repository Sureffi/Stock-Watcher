import requests

class NewsParser:
    def __init__(self, api_key) -> None:
        self.API_KEY = api_key
        self.URL = 'https://newsapi.org/v2/top-headlines'
    
    def get_news(self, company_name):
        '''Returns top 3 news for the given company name'''
        payload = {
            'apiKey':self.API_KEY,
            # 'country':'us',
            'q':company_name
        }
        
        response = requests.get(self.URL, params=payload).json()
        
        total_results = response['totalResults']
        all_articles = response['articles']
        formatted_articles = []
        
        if total_results < 3:
            for article in all_articles:
                tmp = {
                    'headline':article['title'],
                    'brief':article['description'],
                    'link':article['url']
                }
                formatted_articles.append(tmp)
        elif total_results >= 3:
            for article in all_articles[0:3]:
                tmp = {
                    'headline':article['title'],
                    'brief':article['description'],
                    'link':article['url']
                }
                formatted_articles.append(tmp)
                
        return formatted_articles