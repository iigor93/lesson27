import os

from django.core.management.base import BaseCommand
from django.core.management import call_command
from ads.models import Categories, Ads, Location, UserClass


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    fixtures_dir = 'fixtures'
    loaddata_command = 'loaddata'
    filenames = [
        "ad.csv",
        "category.csv",
        "location.csv",
        "user.csv",
    ]

    def handle(self, *args, **options):
        with open(os.path.join(self.fixtures_dir, 'category.csv'), 'r', encoding='UTF-8', newline='\r') as f:
            file_read = f.readlines()
        
        for line in file_read[1:]:
            temp_data = line.split(',')
            temp_ads = Categories()
            temp_ads.name = temp_data[1].strip()
            temp_ads.save()
            
        print('category - OK')
        
        with open(os.path.join(self.fixtures_dir, 'location.csv'), 'r', encoding='UTF-8', newline='\r') as f:
            file_read = f.readlines()
        
        for line in file_read[1:]:
            new_list = []
            i = True
            for item in line:
                if item == '"':
                    i = not i
                if item == ',':
                    if i:
                        new_list.append(';')
                    else:
                        new_list.append(item)
                else:
                    new_list.append(item)
            new_list = ''.join(new_list)
            new_list = new_list.split(';')
            
            temp_ = Location()
            temp_.name = new_list[1].strip()
            temp_.lat = new_list[2].strip()
            temp_.lng = new_list[3].strip()
            temp_.save()
        
        print('location - OK')
        
        with open(os.path.join(self.fixtures_dir, 'user.csv'), 'r', encoding='UTF-8', newline='\r') as f:
            file_read = f.readlines()
        
        for line in file_read[1:]:
            new_list = []
            i = True
            for item in line:
                if item == '"':
                    i = not i
                if item == ',':
                    if i:
                        new_list.append(';')
                    else:
                        new_list.append(item)
                else:
                    new_list.append(item)
            new_list = ''.join(new_list)
            new_list = new_list.split(';')
            
            temp_ = UserClass()
            temp_.first_name = new_list[1].strip()
            temp_.last_name = new_list[2].strip()
            temp_.username = new_list[3].strip()
            temp_.password = new_list[4].strip()
            temp_.role = new_list[5].strip()
            temp_.age = new_list[6].strip()
            temp_.location_id = new_list[7].strip()
            temp_.save()
            
        print('user - OK')
        
        with open(os.path.join(self.fixtures_dir, 'ad.csv'), 'r', encoding='UTF-8', newline='\r') as f:
            file_read = f.readlines()
        
        for line in file_read[1:]:
            new_list = []
            i = True
            for item in line:
                if item == '"':
                    i = not i
                if item == ',':
                    if i:
                        new_list.append(';')
                    else:
                        new_list.append(item)
                else:
                    new_list.append(item)
            new_list = ''.join(new_list)
            new_list = new_list.split(';')
            
            temp_ = Ads()
            temp_.name = new_list[1].strip()
            temp_.author_id = new_list[2].strip()
            temp_.price = new_list[3].strip()
            temp_.description = new_list[4].strip()
            temp_.is_published = True if new_list[5].strip().lower() == 'true' else False
            temp_.image = new_list[6].strip()
            temp_.category_id = new_list[7].strip()
            temp_.save()
        
        print('ad - OK')
            
        
