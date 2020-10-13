from django.test import TestCase
from .models import Category,Location,Image

class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save()

        self.category = Category(name='Nature')
        self.category.save()

        self.image_test = Image(id=1, image='image.jpg', description='this is image', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class CategoryTestClass(TestCase):
  def setUp(self):
    self.nature = Category(name = 'Nature')    
    
  def test_instance(self):
    self.assertTrue(isinstance(self.nature,Category)) 
    
  def test_save_category(self):
    self.nature.save_category()
    category = Category.objects.all()
    self.assertTrue(len(category) >0)

class  LocationTestClass(TestCase):
  
  def setUp(self):
    self.nairobi = Location(name = 'Nairobi')
    
  def test_instance(self):
    self.assertTrue(isinstance(self.nairobi,Location))  
    
  def test_save_method(self):
    self.nairobi.save_location()
    location = Location.objects.all()
    self.assertTrue(len(location) > 0)