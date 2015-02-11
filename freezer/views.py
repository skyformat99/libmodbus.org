# -*- coding: utf-8 -*-

import math
import os

from flask import render_template, send_from_directory, abort

from .app import app
from .models import Article

# Allows trailing slashes (avoid 404)
app.url_map.strict_slashes = False

def by_date(articles):
    return sorted(articles, reverse=True, key=lambda p: p['published'])


@app.route('/', endpoint='home')
@app.route('/news/')
def news():
    return render_template(
        'news.html', selected='news',
        articles=by_date(Article.get_posts()))


@app.route('/documentation/')
def documentation():
    return render_template('documentation.html', selected='documentation')


@app.route('/download/')
def download():
    return render_template('download.html', selected='download')


@app.route('/reportbug/')
def reportbug():
    return render_template('reportbug.html', selected='reportbug')


@app.route('/tags/')
def tags():
    counts = {}
    for article in Article.get_posts():
        for tag in article.meta.get('tags', []):
            counts[tag] = counts.get(tag, 0) + 1

    return render_template(
        'tag_list.html', selected='news',
        tags=[
            # count => weight: 1 => 100, 10 => 150, 100 => 200
            (tag, int(100 + 50 * math.log10(count)))
            # sorted alphabetically by tag name
            for tag, count in sorted(counts.items())
        ])


@app.route('/tags/<name>/')
def tag(name):
    articles = by_date(
        a for a in Article.get_posts() if name in a.meta.get('tags', [])
    )
    if not articles:
        abort(404)

    return render_template('tag.html', selected='news', tag=name, articles=articles)


@app.route('/<int:year>/')
def archives(year):
    articles = by_date(Article.get_posts(year=str(year)))
    return render_template(
        'archives.html', selected='news', articles=articles, year=year)


@app.route('/<int:year>/<name>/')
def article(year, name):
    return render_template(
        'article.html', selected='news', article=Article.load(str(year), name))


@app.route('/<int:year>/<name>/<path:path>')
def static_in_posts(year, name, path):
    return send_from_directory(os.path.join(Article.root, str(year), name), path)


@app.route('/feed.atom')
def feed():
    articles = sorted(
        Article.get_posts(),
        key=lambda o: o['published'],
        reverse=True)[:10]
    feed_updated = articles[0].meta['published']
    xml = render_template('atom.xml', feed_updated=feed_updated, articles=articles)
    return app.response_class(xml, mimetype='application/atom+xml')


@app.errorhandler(404)
def not_found(_e):
    return render_template('404.html')
