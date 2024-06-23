
class HTMLNode:
    def __init__(self, tag: str|None=None, value: str|None=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        if self.props == None:
            return ""
        prop_pairs = []
        for key, value in self.props.items():
            prop_pairs.append(f"{key}=\"{value}\"")

        return " ".join(prop_pairs)
    
    def __repr__(self) -> str:
        return f"""HTMLNode(tag='{self.tag}',
    value='{self.value}'
    children='{self.children}'
    props='{self.props}')"""
