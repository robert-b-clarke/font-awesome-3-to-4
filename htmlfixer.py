from HTMLParser import HTMLParser

class HTMLFixerBase(HTMLParser):
    """A sub class of the Python HTMLParser that copies everything as is
    Intended to form the base of anything that makes slight ammendments to HTML
    """
    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        #HTMLParser not a new style class so using super to reach base class doesn't work
        self._completed_html = str()

    def handle_starttag(self, tag, attrs):
        self._completed_html += self.get_starttag_text()

    def handle_endtag(self, tag):
        self._completed_html += "</%s>" % (tag)

    def handle_data(self, data):
        self._completed_html += data

    def handle_comment(self, data):
        self._completed_html += "<!--%s-->" % (data)

    def handle_entityref(self, name):
        self._completed_html += "&%s;" % (name)

    def handle_decl(self, decl):
        self._completed_html += "<!%s>" % (decl)

    def process_html(self, html_in):
        """Accept an html string and return the output of the parser. If the class isn't overridden this should be the same as the input, regardless of the quality of the html
        >>> parser = HTMLFixerBase()
        >>> parser.process_html('<blink>Stuff &amp; nonsense <font></blink>')
        '<blink>Stuff &amp; nonsense <font></blink>'
        """
        self.feed(html_in)
        return self._completed_html

if __name__ == "__main__":
    import doctest
    doctest.testmod()
