from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

Html = ''
for _ in range(int(input())):
    Html = Html + input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(Html)
parser.close()