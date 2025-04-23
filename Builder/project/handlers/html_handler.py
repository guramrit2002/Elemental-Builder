class HTMLhandler:

    def __render_component(self, component):
        ctype = component.get("type")
        props = component.get("props", {})

        if ctype == "heading":
            return (f"<{props.get('level', 'h2')}>{props.get('text')}"
                    f"</{props.get('level', 'h2')}>")

        elif ctype == "text":
            return f"<p>{props.get('content')}</p>"

        elif ctype == "button":
            return (f"<button class='{props.get('variant', '')}'>"
                    f"{props.get('text')}</button>")

        elif ctype == "image":
            return f"<img src='{props.get('src')}' alt='{props.get('alt')}'/>"

        elif ctype == "navbar":
            links = props.get("links", [])
            nav_links = "".join([f"<a href='{link['href']}'>{link['text']}</a>"\
                                for link in links])
            return f"<nav>{nav_links}</nav>"

        elif ctype in ["flex-row", "flex-col"]:
            direction = "row" if ctype == "flex-row" else "column"
            children = props.get("children", [])
            rendered_children = "".join([self.__render_component(child) \
                                        for child in children])
            return f"<div>{rendered_children}</div>"

        else:
            return "" 

    def get_html(self,json_data):
        html_output = "\n".join(self.__render_component(comp) for comp in \
            json_data if comp.get("type"))
        return html_output
