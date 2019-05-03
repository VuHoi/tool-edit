import copy
import csv
import collections



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
temp1['additional_image_link1']=''
d= collections.OrderedDict(
    [('id', ''), ('custom_label_0', ''), ('custom_label_1', ''), ('custom_label_2', ''), ('custom_label_3', ''), ('custom_label_4', ''), ('title', ''), ('link', ''), ('image_link', ''), ('additional_image_link', ''),('additional_image_link1', ''),('additional_image_link2', ''),('additional_image_link3', ''),('additional_image_link4', ''),('additional_image_link5', ''),('additional_image_link6', ''),('additional_image_link7', ''),('additional_image_link8', ''),('additional_image_link9', ''),('additional_image_link10', ''), ('availability', ''), ('description', ''), ('google_product_category', 'Vehicles & Parts > Vehicle Parts & Accessories > Vehicle Maintenance, Care & Decor > Vehicle Decor > Vehicle Decor Accessory Sets'), ('price', ''), ('brand', ''), ('gtin', ''), ('condition', ''), ('adult', ''), ('is_bundle', ''), ('age_group', ''), ('tax', ''), ('color', ''), ('gender', ''), ('size', ''), ('shipping', 'Universal Fit'), ('product_type', ''), ('identifier_exists', ''), ('promotion_id', ''), ('item_group_id', '{{id}}')]
)
fieldnames = d.keys()

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
                    # parent_data['additional_image_link']=item['additional_image_link']
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
                    a= copy.deepcopy(parent_data)
                    del a['Keyword']
                    writer.writerow(a)
                    break
                except:
                    continue


    

# writer.writerow(parent_data)
        