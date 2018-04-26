from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from mem_generator.forms import ImageUploadForm
from mem_generator.settings import MEDIA_DIR
from mem_generator.settings import IMAGE_DIR_NAME
from mem_generator.settings import MAX_IMAGE_SIZE
from string import ascii_letters, digits
from random import choice
import os
import hashlib


def index(request):
    return render(request, 'index.html')


class ImageUpload(View):
    form_class = ImageUploadForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['image'].size() > MAX_IMAGE_SIZE:
                return JsonResponse({"status": "ERROR", "msg": "Image is too big"})
            alphaNum = ascii_letters + digits
            dir = os.path.join(MEDIA_DIR, IMAGE_DIR_NAME, choice(alphaNum), choice(alphaNum))
            if not os.path.exists(dir):
                os.makedirs(dir)
            imageData = form.cleaned_data["image"].read()
