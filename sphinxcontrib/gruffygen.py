# -*- coding: utf-8 -*-
"""
    sphinxcontrib.gruffygen
    ~~~~~~~~~~~~~~~~~~~~~~~

    This extension render to simple Graph. use Gruffy module.

    :author: Hideo Hattori <hhatto.jp@gmail.com>
    :license: BSD
"""
import os
import posixpath
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util import ensuredir
from sphinx.util.compat import Directive
try:
    from hashlib import sha1 as sha
except ImportError:
    from sha import sha
import gruffy


class gruffygen(nodes.General, nodes.Element):
    pass


class Gruffy(Directive):
    """
    Directive to
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'title': directives.unchanged,
        'type': directives.unchanged,
        'width': directives.nonnegative_int
    }

    def run(self):
        gruffydata = '\n'.join(self.content)
        node = gruffygen()
        node['code'] = gruffydata
        node['options'] = self.options
        if 'title' not in self.options:
            node['options']['title'] = ''
        if 'width' not in self.options:
            node['options']['width'] = 600
        if 'type' not in self.options:
            node['options']['type'] = 'Dot'
        return [node]


def render_gruffy(self, code, options, formattype, prefix='gruffy'):
    hashkey = code.encode('utf-8') + str(options)
    fname = "%s-%s.%s" % (prefix, sha(hashkey).hexdigest(), formattype)
    relfn = posixpath.join('_images', fname)
    outfn = os.path.join(self.builder.outdir, '_images', fname)
    ensuredir(os.path.dirname(outfn))
    if not os.path.exists(os.path.dirname(outfn)):
        raise
    exec "g = gruffy.%s(%d)" % (options['type'], options['width'])
    g.title = str(options['title'])
    for line in code.splitlines():
        exec "g.%s" % line.strip()
    g.write(outfn)
    return relfn


def render_gruffy_html(self, node, code, options, prefix='gruffy'):
    formattype = 'png'
    htmlfn = render_gruffy(self, code, options, formattype, prefix)
    self.body.append(self.starttag(node, 'p', CLASS='gruffy'))
    self.body.append('<img src="%s" alt="%s">\n' % (htmlfn, options['title']))
    self.body.append('</p>\n')
    raise nodes.SkipNode


def html_visit_gruffy(self, node):
    render_gruffy_html(self, node, node['code'], node['options'])


def setup(app):
    app.add_node(gruffygen,
                 html=(html_visit_gruffy, None))
    app.add_directive('gruffy', Gruffy)
