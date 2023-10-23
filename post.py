class Post:
    def __init__(self, message, auther):
        self.message = message
        self.auther = auther

    def get_post_info(self):
        print(f"Post {self.message} written by {self.auther}")