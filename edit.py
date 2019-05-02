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
fieldnames = template_line.keys()
templates=  get_template_line('feed_template.csv')
data= copy.deepcopy(get_template_line('tmp.csv'))
parent_data = copy.deepcopy(template_line)
with open('output/output.csv', 'w', newline='\n') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        parent_data=item
        for temp in templates:
            if temp['Keyword'].lower() in item['title'].lower():
                try:
                    parent_data['google_product_category']=temp['google_product_category']
                    parent_data['color']=temp['color']
                    parent_data['shipping']=temp['shipping']
                    parent_data['item_group_id']=parent_data['id']
                    writer.writerow(parent_data)
                except:
                    continue


    

# writer.writerow(parent_data)
        