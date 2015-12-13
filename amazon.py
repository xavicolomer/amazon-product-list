# -*- coding: utf-8 -*-
import urllib
from pyquery import PyQuery as pq
import pdb
import re
import json
import sys
import argparse
import traceback
import os
import settings


def createFolder(path, overwrite=True):
    if os.path.exists(path):
        if (overwrite):
            import shutil
            shutil.rmtree(path)
            os.makedirs(path)
    else:
        os.makedirs(path)


def downloadImage(folder_path, image_name, url, overwrite=True):
    createFolder(folder_path, overwrite)

    path = folder_path + '/' + image_name
    f = open(path, 'wb')
    f.write(urllib.urlopen(url).read())
    f.close()


def getProductDetail(aid, link, path):
    query = pq(url=link)
    details = {}

    details['images'] = {}
    try:
        regex = re.compile(ur'(data\["colorImages"\] = )(.*)(;)', re.MULTILINE)
        images = re.findall(regex, query.html().encode('utf-8').strip())
        details['images'] = json.loads(images[0][1])

        if (path):
            for image in details['images']:
                for variant in details['images'][image]:
                    downloadImage(path + '/' + image, variant['hiRes'].rsplit('/', 1)[1], variant['hiRes'], False)
        
    except:
        print 'No images found'

    regex = re.compile(r'[\n\r\t]')
    description = query('div').filter('#productDescription.a-section').html()
    if (description):
        description = description.encode('utf-8').strip()
        description = re.sub("(<!--.*?-->)", "", description, flags=re.MULTILINE)
    elif (not description):
        description = ''
    details['description'] = regex.sub('', description).strip()

    myKeywords = ''
    try:
        regex = re.compile(ur'(<meta name="keywords" content=")(.*)("\/>)', re.MULTILINE)
        keywords = re.findall(regex, query.html().encode('utf-8').strip())
        myKeywords = keywords[0][1].split(',')
    except:
        print 'No keywords found'
    details['keywords'] = myKeywords

    myRating = ''
    try:
        rating = query('span').filter('#acrPopover').attr('title').strip().split(' ')[0]
        myRating = rating[0]
    except:
        print 'No rating found'
    details['rating'] = myRating

    return details


def getProductInfo(keyword, page, download):
    products = []

    try:
        link = settings.AMAZON_URL.format(keyword, str(page))
        query = pq(url=link)
        results = query('li').filter('.s-result-item')
        path = None

        for result in results:
            try:
                article = {}
                articleQuery = pq(result)
                article['amazonID'] = articleQuery.attr('data-asin')

                myTitle = ''
                if (articleQuery('h2').filter('.s-access-title').contents()[0]):
                    myTitle = articleQuery('h2').filter('.s-access-title').contents()[0].strip()
                article['title'] = myTitle

                article['thumbnail'] = articleQuery('img').filter('.s-access-image').attr["src"]

                if (download):
                    path = download + '/' + article['amazonID']
                    downloadImage(path, article['thumbnail'].rsplit('/', 1)[1], article['thumbnail'])
                    
                article['url'] = articleQuery('a').filter('.s-access-detail-page').attr["href"]
                article['details'] = getProductDetail(article['amazonID'], article['url'], path)
                price = articleQuery('span').filter('.s-price').contents()[0].split(' ')
                article['price'] = {'currency': price[0], 'value': price[1]}
                products.append(article)

            except Exception, err:
                import traceback
                traceback.print_exc()
                print 'Invalid Product'
                print Exception, err
    except Exception, err:
        print Exception, err

    return products


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', action='store', dest='output', help='Output File', default=settings.DEFAULT_OUTPUT_FOLDER + settings.DEFAULT_OUTPUT_FILENAME)
    parser.add_argument('-k', action='store', dest='keyword', help='Keyword Search')
    parser.add_argument('-p', action='store', dest='pages', help='Num Pages', type=int)
    parser.add_argument('-d', action='store', dest='download', help='Download Images Folder')
    args = parser.parse_args()
    results = []
    currentPage = 1
    download = None

    if (args.download):
        download = args.download
        if (not download.startswith('/')):
            download = settings.DEFAULT_OUTPUT_FOLDER + download

        createFolder(download)

    if (args.keyword):
        if (args.pages):
            for num in range(1, args.pages + 1):
                results = results + getProductInfo(args.keyword, num, download)
        else:
            results = getProductInfo(args.keyword, 1, download)

    if (args.output):
        import codecs
        with codecs.open(args.output, 'w', encoding='utf8') as f:
            f.write(json.dumps(results))
            f.close()

if __name__ == "__main__":
    main(sys.argv)
