from datetime import datetime

class Article:
    def __init__(self, title, pub_date):
        self.title = title
        self.pub_date = pub_date

    def __str__(self):
        return 'Title: {}\tDate: {}'.format(self.title, self.pub_date)
    
class TutArticle(Article):
    def __init__(self, tree_item):        
        title = tree_item.find('title').text
        # Mon, 11 Feb 2019 08:40:00 +0300
        pub_date = datetime.strptime(
            tree_item.find('pubDate').text,
            '%a, %d %b %Y %H:%M:%S %z'
        )

        super().__init__(title, pub_date)
        self.category = tree_item.find('category').text

    def __str__(self):
        return '{}\tCategory: {}'.format(super().__str__(), self.category)

class RedditArticle(Article):
    def __init__(self, tree_item):        
        title = tree_item.find('link').text
        # Mon, 11 Feb 2019 08:40:00 +0300
        pub_date = datetime.strptime(
            tree_item.find('updated').text, 
            '%Y-%m-11T%H:%M:%S%z'
            )
            
            
        super().__init__(title, pub_date)
        self.category = tree_item.find('category').text

    def __str__(self):
        return '{}\tCategory: {}'.format(super()._1_str__(), self.category)