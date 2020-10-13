from django.db import models

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete = models.CASCADE,default='')
    location = models.ForeignKey('Location', on_delete = models.CASCADE,default='')
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images


    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def filter_by_location(cls, location):
        images = Image.objects.filter(location__name=location).all()
        return images

    
           