import re
class Parser:

    # Some class constants
    M_REGEX    = 0 # index of regex in matchers tuples
    M_RENDERER = 1 # index of renderer method in matchers tuples

    # Markdown regular expressions
    RE_H1       = r"(?P<text>.*)\n[=]=*\n"
    RE_EMPTY    = r"\n"
    RE_LINE     = r"(?P<text>.*)\n"
    RE_CODE     = r"(?s)(```)(?P<syntax>.*?)\n(?P<text>.*?)(```)"

    def __init__(self,renderer):
        self.matchers = [
            ( Parser.RE_H1, renderer.onHeader1 ),
            ( Parser.RE_CODE, renderer.onCode ),
            ( Parser.RE_EMPTY, renderer.onEmpty ),
            ( Parser.RE_LINE, renderer.onLine )
        ]
        self.renderer = renderer

    def _match(self,regex,buf):
        e = re.match(regex,buf,re.MULTILINE)
        groups = None
        if e:
            buf = buf[e.end():]
            groups = e.groupdict()
        return (e!=None,buf,groups)
   
    def parse(self,buf):
        while (len(buf)>0):
            for r in self.matchers:
                (res,buf,groups) = self._match(r[Parser.M_REGEX],buf)
                if res:
                    output = r[Parser.M_RENDERER](groups)
                    break
        self.renderer.onEnd()