import numpy as np
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from keras.models import load_model


# from keras.layers.wrappers import Bidirectional


# Create your views here.
def work(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == 'POST':
        global model
        model = load_model("/home/joker/PycharmProjects/djangoProject3/models/model_3.h5")
        domain = request.POST.get('testingurl')
        domain_data = np.array([([ord(j) for j in domain] + [0 for k in range(53 - len(domain))])
                                if len(domain) <= 53 else [ord(domain[j]) for j in range(53)]])
        pred = model.predict(domain_data)
        if pred[0][0] > pred[0][1]:
            # with open('/home/joker/PycharmProjects/djangoProject3/models/phishing_site_urls.csv',
            #           encoding='utf-8') as f:
            #     reader = csv.reader(f)
            #     header = next(reader)
            # for row in reader:
            #     if row[0] == request.POST.get('testingurl'):
            #         hint = '检测为恶意域名\n'
            #     else:
            hint = '检测为正常域名\n'
        else:
            hint = '检测为恶意域名\n'
    return render(request, 'index.html', {'hint': hint})
