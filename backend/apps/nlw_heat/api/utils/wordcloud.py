from django.conf import settings
from django.db.models.query import QuerySet

import base64, io, urllib
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from matplotlib import use
from PIL import Image
import numpy as np

use('Agg')

def create_word_cloud(messages: QuerySet) -> str:
    mask = np.array(Image.open(str(settings.BASE_DIR / 'apps/nlw_heat/api/utils/rocket.png')))
    comment_words = ''
    stopwords = set(STOPWORDS)
    comment_words  = ' '.join(messages.values_list('text', flat=True))

    wc = WordCloud(
        background_color='black',
        colormap='Set2',
        max_words=100,
        mask=mask,
        stopwords=stopwords,
        contour_width=3,
        contour_color='#222'
    ).generate(comment_words)

    plt.figure(figsize=(15, 15), facecolor=None)
    plt.imshow(wc)
    plt.axis('off')
    plt.tight_layout(pad=0)
    fig = plt.gcf()
    buf = io.BytesIO()
    # buf = io.StringIO() # svg string
    fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0, transparent=True)
    buf.seek(0)
    # print(buf.getvalue()) # svg string

    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return  'data:image/png;base64,' + uri
