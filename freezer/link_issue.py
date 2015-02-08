'''
Issue Link Extension for Python-Markdown
====================================

Converts #123 to a link to your tracker issue.

'''
from __future__ import absolute_import
from __future__ import unicode_literals

from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree


class IssueLinkPattern(Pattern):
    def __init__(self, pattern, config):
        super(IssueLinkPattern, self).__init__(pattern)
        self.config = config

    def handleMatch(self, m):
        issue = m.group(2).strip()
        if issue:
            url = self.config['base_url'] + '/' + issue
            a = etree.Element('a')
            a.text = '#' + issue
            a.set('href', url)
        else:
            a = ''
        return a


class IssueLinkExtension(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'base_url': [
                'https://github.com/stephane/libmodbus/issues',
                'String to append to the issue number.'
            ]
        }
        super(IssueLinkExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        ISSUELINK_RE = r'\#(\d+)'
        pattern = IssueLinkPattern(ISSUELINK_RE, self.getConfigs())
        pattern.md = md
        md.inlinePatterns.add('issuelink', pattern, '<not_strong')


def makeExtension(*args, **kwargs):
    return IssueLinkExtension(*args, **kwargs)
