from datetime import datetime


class Post(object):
     def __init__(self, text, timestamp=None):
         self.text = text
         self.timestamp = timestamp
         self.user = None

     def set_user(self, user):
         self.user = user


class TextPost(Post):  # Inherit properly
     def __str__(self):
         return '@{firstname} {lastname}: "{text}"\n\t{weekday}, {month} {day}, {year}'.format(
              firstname=self.user.first_name, lastname=self.user.last_name, text=self.text, weekday=self.timestamp.strftime("%A"), month = self.timestamp.strftime("%b"),
              day = self.timestamp.day, year = self.timestamp.year)


class PicturePost(Post):  # Inherit properly
     def __init__(self, text, image_url, timestamp=None):
         super(PicturePost, self).__init__(text, timestamp)
         self.image_url = image_url

     def __str__(self):
         return '@{firstname} {lastname}: "{text}"\n\t{url}\n\t{weekday}, {month} {day}, {year}'.format(
              firstname=self.user.first_name, lastname=self.user.last_name, text=self.text, url = self.image_url, weekday=self.timestamp.strftime("%A"), 
              month = self.timestamp.strftime("%b"),
              day = self.timestamp.day, year = self.timestamp.year)


class CheckInPost(Post):  # Inherit properly
     def __init__(self, text, latitude, longitude, timestamp=None):
         super(CheckInPost, self).__init__(text, timestamp)
         self.latitude = latitude
         self.longitude = longitude

     def __str__(self):
         return '@{firstname} Checked In: "{text}"\n\t{lat}, {lon}\n\t{weekday}, {month} {day}, {year}'.format(
              firstname=self.user.first_name, text=self.text, lat = self.latitude, lon = self.longitude, 
              weekday=self.timestamp.strftime("%A"), month = self.timestamp.strftime("%b"),
              day = self.timestamp.day, year = self.timestamp.year)
