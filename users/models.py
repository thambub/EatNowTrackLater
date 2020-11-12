from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from blog.models import Post
from datetime import date

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    user_age = models.IntegerField(default=0)
    user_height_in_inches = models.IntegerField(default=0)
    user_weight_in_lbs = models.IntegerField(default=0)
    user_sex = models.TextField(default=0, max_length=10)
    favorite_food = models.TextField(default=0, max_length=50)
    favorite_hobby = models.TextField(default=0, max_length=50)
    bio = models.TextField(default=0, max_length=50)
    name = models.TextField(default=0, max_length=5)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()
    
    def minutes_aerobic_activity_week(self):
        today = date.today()
        if today.weekday() == 0:
            today = 0
            return self.minutes_aerobic_activity_day(today)
        elif today.weekday() == 1:
            today = 0
            days_before = 1
            monday = int(self.minutes_aerobic_activity_day(days_before))
            tuesday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday
        elif today.weekday() == 2:
            today = 0
            days_before = 1
            two_days_before = 2
            monday = int(self.minutes_aerobic_activity_day(two_days_before))
            tuesday = int(self.minutes_aerobic_activity_day(days_before))
            wednesday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday + wednesday
        elif today.weekday() == 3:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            monday = int(self.minutes_aerobic_activity_day(three_days_before))
            tuesday = int(self.minutes_aerobic_activity_day(two_days_before))
            wednesday = int(self.minutes_aerobic_activity_day(days_before))
            thursday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday + wednesday + thursday
        elif today.weekday() == 4:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            monday = int(self.minutes_aerobic_activity_day(four_days_before))
            tuesday = int(self.minutes_aerobic_activity_day(three_days_before))
            wednesday = int(self.minutes_aerobic_activity_day(two_days_before))
            thursday = int(self.minutes_aerobic_activity_day(days_before))
            friday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday
        elif today.weekday() == 5:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            five_days_before = 5
            monday = int(self.minutes_aerobic_activity_day(five_days_before))
            tuesday = int(self.minutes_aerobic_activity_day(four_days_before))
            wednesday = int(self.minutes_aerobic_activity_day(three_days_before))
            thursday = int(self.minutes_aerobic_activity_day(two_days_before))
            friday = int(self.minutes_aerobic_activity_day(days_before))
            saturday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday + saturday
        elif today.weekday() == 6:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            five_days_before = 5
            six_days_before = 6
            monday = int(self.minutes_aerobic_activity_day(six_days_before))
            tuesday = int(self.minutes_aerobic_activity_day(five_days_before))
            wednesday = int(self.minutes_aerobic_activity_day(four_days_before))
            thursday = int(self.minutes_aerobic_activity_day(three_days_before))
            friday = int(self.minutes_aerobic_activity_day(two_days_before))
            saturday = int(self.minutes_aerobic_activity_day(days_before))
            sunday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday + saturday + sunday
        
    def minutes_weightlifting_activity_week(self):
        today = date.today()
        if today.weekday() == 0:
            today = 0
            return self.minutes_weightlifting_activity_day(today)
        elif today.weekday() == 1:
            today = 0
            days_before = 1
            monday = int(self.minutes_weightlifting_activity_day(days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday
        elif today.weekday() == 2:
            today = 0
            days_before = 1
            two_days_before = 2
            monday = int(self.minutes_weightlifting_activity_day(two_days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(days_before))
            wednesday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday + wednesday
        elif today.weekday() == 3:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            monday = int(self.minutes_weightlifting_activity_day(three_days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(two_days_before))
            wednesday = int(self.minutes_weightlifting_activity_day(days_before))
            thursday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday + wednesday + thursday
        elif today.weekday() == 4:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            monday = int(self.minutes_weightlifting_activity_day(four_days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(three_days_before))
            wednesday = int(self.minutes_weightlifting_activity_day(two_days_before))
            thursday = int(self.minutes_weightlifting_activity_day(days_before))
            friday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday
        elif today.weekday() == 5:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            five_days_before = 5
            monday = int(self.minutes_weightlifting_activity_day(five_days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(four_days_before))
            wednesday = int(self.minutes_weightlifting_activity_day(three_days_before))
            thursday = int(self.minutes_weightlifting_activity_day(two_days_before))
            friday = int(self.minutes_weightlifting_activity_day(days_before))
            saturday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday + saturday
        elif today.weekday() == 6:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            five_days_before = 5
            six_days_before = 6
            monday = int(self.minutes_weightlifting_activity_day(six_days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(five_days_before))
            wednesday = int(self.minutes_weightlifting_activity_day(four_days_before))
            thursday = int(self.minutes_weightlifting_activity_day(three_days_before))
            friday = int(self.minutes_weightlifting_activity_day(two_days_before))
            saturday = int(self.minutes_weightlifting_activity_day(days_before))
            sunday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday + saturday + sunday
        
         
            

    def minutes_aerobic_activity_day(self,days_before):
        today = date.today()
        posts_on_day = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day-days_before, author=self.user)
        total_servings = 0
        for post in posts_on_day:
            total_servings = total_servings + post.minutes_aerobic_exercise
        return total_servings
    
    def minutes_weightlifting_activity_day(self,days_before):
        today = date.today()
        posts_on_day = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day-days_before, author=self.user)
        total_servings = 0
        for post in posts_on_day:
            total_servings = total_servings + post.minutes_weightlifting_exercise
        return total_servings
    
    def minutes_aerobic_activity_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.minutes_aerobic_exercise
        return total_servings
    
    def minutes_weightlifting_activity_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.minutes_weightlifting_exercise
        return total_servings
    
    def meat_servings_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.servings_meat
        return total_servings
    
    def grains_servings_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.servings_grains
        return total_servings

    def dairy_servings_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.servings_dairy
        return total_servings

    def vegetables_servings_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.servings_vegetables
        return total_servings

    def fruit_servings_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.servings_fruit
        return total_servings

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
     
   
        
    
    
