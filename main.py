from clarifai.rest import ClarifaiApp
import json

app = ClarifaiApp()
tags = app.tag_urls(['http://responsiblemarketing.com/blog/wp-content/uploads/2008/12/collegiate-churches-of-new-york-phone-booth-ad.jpg'])

print json.dumps(tags)

ad_words = ['billboard', 'sign', 'business', 'logo']
