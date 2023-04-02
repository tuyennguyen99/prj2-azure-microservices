import logging.config
import os
from flask import Flask, Blueprint, request, jsonify, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import settings
import requests
import json
from flask import make_response
from feedgen.feed import FeedGenerator
from urllib.parse import urljoin
from feedwerk.atom import AtomFeed, FeedEntry
app = Flask(__name__)
Bootstrap(app)



def get_abs_url(url):
    """ Returns absolute url by joining post url with base url """
    return urljoin(request.url_root, url)


@app.route('/feeds/')
def feeds():
    feed = AtomFeed(title='All Advertisements feed',
                    feed_url=request.url, url=request.url_root)

    response = requests.get(settings.API_URL + '/getAdvertisements')
    posts = response.json()

    for key, value in posts.items():
        print("key,value: " + key + ", " + value)

    #     feed.add(post.title,
    #              content_type='html',
    #              author= post.author_name,
    #              url=get_abs_url(post.url),
    #              updated=post.mod_date,
    #              published=post.created_date)

    # return feed.get_response()


@app.route('/rss')
def rss():
    fg = FeedGenerator()
    fg.title('Feed title')
    fg.description('Feed Description')
    fg.link(href='https://neighborly-client-v1.azurewebsites.net/')
    

    response = requests.get(settings.API_URL + '/getAdvertisements')
    ads = response.json()

    for a in ads: 
        fe = fg.add_entry()
        fe.title(a.title)
        fe.description(a.description)

    response = make_response(fg.rss_str())
    response.headers.set('Content-Type', 'application/rss+xml')
    return response

@app.route('/')
def home():
    response = requests.get(settings.API_URL + '/getAdvertisements')
    response2 = requests.get(settings.API_URL + '/getPosts')

    ads = response.json()
    posts = response2.json()
    return render_template("index.html", ads=ads, posts=posts)

@app.route('/post/add', methods=['GET'])
def add_post_view():
    return render_template("new_post.html")

@app.route('/post/new', methods=['POST'])
def add_post_request():
    # Get item from the POST body
    req_data = {
        'title': request.form['title'],
        'city': request.form['city'],
        'description': request.form['description'],
        'imgUrl': request.form['imgUrl'],
    }
    response = requests.post(settings.API_URL + '/createPost', json=req_data)
    return redirect(url_for('home'))

@app.route('/post/view/<id>', methods=['GET'])
def view_post_view(id):
    response = requests.get(settings.API_URL + '/getPost?id=' + id)
    post = response.json()
    return render_template("view_post.html", post=post)

@app.route('/post/edit/<id>', methods=['GET'])
def edit_post_view(id):
    response = requests.get(settings.API_URL + '/getPost?id=' + id)
    post = response.json()
    return render_template("edit_post.html", post=post)

@app.route('/post/update/<id>', methods=['POST'])
def update_post_request(id):
    # Get item from the POST body
    req_data = {
        'title': request.form['title'],
        'city': request.form['city'],
        'description': request.form['description'],
        'imgUrl': request.form['imgUrl'],
    }
    response = requests.put(settings.API_URL + '/updatePost?id=' + id, json=req_data)
    return redirect(url_for('home'))

@app.route('/post/delete/<id>', methods=['GET'])
def delete_post_view(id):
    response = requests.get(settings.API_URL + '/getPost?id=' + id)
    post = response.json()
    return render_template("delete_post.html", post=post)

@app.route('/post/delete/<id>', methods=['POST'])
def delete_post_request(id):
    response = requests.delete(settings.API_URL + '/deletePost?id=' + id)
    if response.status_code == 200:
        return redirect(url_for('home'))

@app.route('/ad/add', methods=['GET'])
def add_ad_view():
    return render_template("new_ad.html")


@app.route('/ad/edit/<id>', methods=['GET'])
def edit_ad_view(id):
    response = requests.get(settings.API_URL + '/getAdvertisement?id=' + id)
    ad = response.json()
    return render_template("edit_ad.html", ad=ad)


@app.route('/ad/delete/<id>', methods=['GET'])
def delete_ad_view(id):
    response = requests.get(settings.API_URL + '/getAdvertisement?id=' + id)
    ad = response.json()
    return render_template("delete_ad.html", ad=ad)

@app.route('/ad/view/<id>', methods=['GET'])
def view_ad_view(id):
    response = requests.get(settings.API_URL + '/getAdvertisement?id=' + id)
    ad = response.json()
    return render_template("view_ad.html", ad=ad)

@app.route('/ad/new', methods=['POST'])
def add_ad_request():
    # Get item from the POST body
    req_data = {
        'title': request.form['title'],
        'city': request.form['city'],
        'description': request.form['description'],
        'email': request.form['email'],
        'imgUrl': request.form['imgUrl'],
        'price': request.form['price']
    }
    response = requests.post(settings.API_URL + '/createAdvertisement', json=req_data)
    return redirect(url_for('home'))

@app.route('/ad/update/<id>', methods=['POST'])
def update_ad_request(id):
    # Get item from the POST body
    req_data = {
        'title': request.form['title'],
        'city': request.form['city'],
        'description': request.form['description'],
        'email': request.form['email'],
        'imgUrl': request.form['imgUrl'],
        'price': request.form['price']
    }
    response = requests.put(settings.API_URL + '/updateAdvertisement?id=' + id, json=req_data)
    return redirect(url_for('home'))

@app.route('/ad/delete/<id>', methods=['POST'])
def delete_ad_request(id):
    response = requests.delete(settings.API_URL + '/deleteAdvertisement?id=' + id)
    if response.status_code == 200:
        return redirect(url_for('home'))

# running app
def main():
    print(' ----->>>> Flask Python Application running in development server')
    app.run(host=settings.SERVER_HOST, port=settings.SERVER_PORT, debug=settings.FLASK_DEBUG)


if __name__ == '__main__':
    main()
