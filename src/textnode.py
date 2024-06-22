class TextNode:

    def __init__(self, content, text_type, url=None):
        self.content = content
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.content == other.content \
            and self.text_type == other.text_type \
            and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.content}, {self.text_type}, {self.url})"
