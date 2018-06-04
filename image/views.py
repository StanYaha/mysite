from django.shortcuts import render, render_to_response
from qiniu import Auth, put_file
import os
from image.models import Photo


def uploadimg(request):

    if request.method == 'POST':
        photo_id_list = []
        for i in request.FILES.getlist('pickup'):
            print(i)
            photo = Photo()
            print(photo_id_list)
            # photo.save_photo_brief(request.FILES[i])
            photo.save_photo_file(i)
            photo_id_list.append(photo.id)

    return render(request, 'upload.html')


def hots(request):
    # photos = Photo.objects.all().order_by('-score')[0:21]  # 按得分倒序，最大的排在前面
    # for p in photos:
    #     p.tag_list = p.tags.all()[0:4]  # 只取前4个标签
    #
    # p_len = len(photos)
    # p_len_remainder = p_len % 3  # 余数
    #
    # if p_len_remainder != 0:
    #     p_len -= p_len_remainder
    #
    # # 把[1,2,3,4,5]转换成[[1,2,3],[4,5]]
    # p_items = []
    # for i in range(0, p_len, 3):
    #     p_items.extend([[photos[i], photos[i + 1], photos[i + 2]]])
    #
    # if p_len_remainder == 1:
    #     p_items.extend([[photos[p_len]]])
    # elif p_len_remainder == 2:
    #     p_items.extend([[photos[p_len], photos[p_len + 1]]])

    return render_to_response('explore3.html', {'request': request,
                                                       'p_items': '', 'isHots': True})


def photowall(request):
    photolist = Photo.objects.all()
    return render(request, 'photowall.html', {
        'photolist': photolist
    })
