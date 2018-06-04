from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from io import BytesIO
from qiniu import Auth, put_data

# Create your models here.
from mysite import settings

bucket_name = 'photowall'
access_key = 'cbjqXDJKDDy9wy2sRRq2NulALQKhE7l6EZv9XV3S'
secret_key = '6fZVQq_U4hxx-q6fQ69TfHUsBXlXACSoH9S2NToW'
q = Auth(access_key, secret_key)


class Photo(models.Model):
    '''
    照片的数据模型
    '''

    # owner = models.ForeignKey(User)
    # album = models.ForeignKey(Album)
    title = models.CharField(max_length=32, blank=True)
    caption = models.TextField(blank=True)
    # tags = models.ManyToManyField(Tag)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    shot_date = models.DateTimeField(null=True)
    camera = models.CharField(max_length=128, blank=True)
    square_loc = models.CharField(max_length=128, default="")  # 方格图
    thumb_loc = models.CharField(max_length=128, default="")
    middle_loc = models.CharField(max_length=128, default="")
    original_loc = models.CharField(max_length=128, default="")
    middle_width = models.IntegerField(default=0)
    middle_height = models.IntegerField(default=0)
    original_width = models.IntegerField(default=0)
    original_height = models.IntegerField(default=0)
    score = models.FloatField(default=0)  # 根据用户的喜欢数和时间计算照片的得分
    image_url = models.CharField(max_length=128, default="")

    def __unicode__(self):
        return str(self.id)

    def save_photo_file(self, photofile):
        image = Image.open(photofile)
        output = BytesIO()
        image.save(output, "png", quality=90)
        img_data = output.getvalue()
        output.close()
        # self.owner.save()
        self.save()
        setting_url = '%s/%s_%s_o.jpg' % (settings.QINIU_IMG_URL, settings.QINIU_FILE_PREFIX, str(self.id))
        self.image_url = setting_url
        filekey = '%s_%s_o.jpg' % (settings.QINIU_FILE_PREFIX, str(self.id))
        self.save()
        uptoken = q.upload_token(bucket_name, filekey, 3600)
        ret, err = put_data(uptoken, filekey, img_data)
        print(err, ret)

    # def save_photo_brief(self, user, photofile, album_id):
    #     self.owner = user
    #     self.album = Album.objects.get(id=album_id)
    #     # 相册和用户的照片计数在upload view函数中统一保存
    #     # self.owner.photo_count += 1
    #     # self.album.photo_count += 1
    #     # self.owner.save()
    #     # self.album.save()
    #     self.save()  # 保存到数据库，生成id
    #
    #     self.save_photo_file(photofile)  # 生成照片文件的各种尺寸并保存到指定目录中
    #     self.save()  # 保存到数据库
    #
    # def get_photo_url(self):
    #     file_name = '%s_%s_o.jpg' % (settings.QINIU_FILE_PREFIX, str(self.id))
    #     url = '%s/%s' % (settings.QINIU_IMG_URL, file_name)
    #     print(url)


class Album(models.Model):
    '''
    相册的数据模型
    '''

    owner = models.ForeignKey(User)
    topic = models.CharField(max_length=32)
    caption = models.TextField(blank=True)
    # 不要用默认值，默认值只在第一次时被赋值，以后都是用相同的默认值，也就是相同的时间
    # date_created = models.DateTimeField(default=datetime.datetime.now())
    date_created = models.DateTimeField(auto_now_add=True)
    # -1表示没有封面，当相册中有照片时，系统会自动选择一张作为显示的封面
    cover_photo_id = models.IntegerField(default=-1)
    last_post = models.DateTimeField(null=True)
    view_count = models.IntegerField(default=0)
    photo_count = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        ordering = ['-date_created']  # 按创建时间倒序，最近的排在前面
        app_label = 'glow'

    # 当用户没有指定封面时，如果该相册中有照片，就选择一张作为封面
    def setNewDefaultCover(self):
        cover_loc = 'default_album_cover.gif'  # 缺省的相册封面
        if self.photo_count > 0:
            try:
                photo = (Photo.objects.filter(owner=self.owner, album=self))[0]
            except:
                self.cover_photo_id = -1
            else:
                self.cover_photo_id = photo.id
                self.save()  # 保存
                try:
                    photo = Photo.objects.get(owner=self.owner, album=self, id=self.cover_photo_id)
                    cover_loc = photo.square_loc
                except:
                    pass

        return cover_loc

        # 获取相册封面的照片文件地址

    def getCoverLoc(self):
        # cover_loc = '/static/img/default_album_cover.gif'#缺省的相册封面
        if self.cover_photo_id == -1:
            cover_loc = self.setNewDefaultCover()
        else:
            try:
                photo = Photo.objects.get(owner=self.owner, album=self, id=self.cover_photo_id)
                cover_loc = photo.square_loc
            except:
                cover_loc = self.setNewDefaultCover()

        return cover_loc
