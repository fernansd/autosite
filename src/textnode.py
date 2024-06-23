class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text or ""
        self.text_type = text_type or ""
        self.url = url
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def __eq__(self, __value: object) -> bool:
        if self.text != __value.text:
            return False
        if self.text_type != __value.text_type:
            return False
        if self.url != __value.url:
            return False
        return True
    

