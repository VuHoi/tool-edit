import copy
import csv




def get_template_line(fileName):
     # Read data that needs processing from CSV files
    template = []
    with open(fileName, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            template.append(row)

    return template


template_line = get_template_line('feed_template.csv')[0]
temp1 = copy.deepcopy(template_line)
del temp1['Keyword']
fieldnames = temp1.keys()
templates=  get_template_line('feed_template.csv')
data= copy.deepcopy(get_template_line('tmp.csv'))
parent_data = copy.deepcopy(template_line)

with open('output/output.csv', 'w', newline='\n') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        # parent_data=item
        for temp in templates:
            keys = temp['Keyword'].split('/')
            if (keys[0].lower() in item['title'].lower() or (len(keys) > 0 and keys[len(keys)-1].lower() in item['title'].lower())):
                try:
                    parent_data['google_product_category']=temp['google_product_category']
                    parent_data['color']=temp['color']
                    parent_data['shipping']=temp['shipping']
                    parent_data['item_group_id']=item['id']
                    parent_data['image_link']=item['image_link']
                    parent_data['title']=item['title']
                    parent_data['link']=item['link']
                    parent_data['additional_image_link']=item['additional_image_link']
                    parent_data['availability']=item['availability']
                    parent_data['description']=item['description']
                    parent_data['price']=item['price']
                    parent_data['condition']=item['condition']
                    parent_data['adult']=item['adult']
                    parent_data['is_bundle']=item['is_bundle']
                    parent_data['age_group']=item['age_group']
                    parent_data['tax']=item['tax']
                    parent_data['gender']=item['gender']
                    parent_data['size']=item['size']
                    parent_data['product_type']=item['product_type']
                    parent_data['id']=item['id']
                    print(parent_data)
                    a= copy.deepcopy(parent_data)
                    del a['Keyword']
                    writer.writerow(a)
                    break
                except:
                    continue


    

# writer.writerow(parent_data)
        