class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return None

        accumulator = ""
        for key, value in self.props.items():
            accumulator = accumulator + f' {key}="{value}"'

        return accumulator[1:]

    def __repr__(self):
        return f'HTMLNODE({self.tag}, {self.value}, children: {self.children}. {self.props})'
