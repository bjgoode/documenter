import os, sys, csv
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "documenter.settings")

import django
django.setup()

from rate_doc.models import Doc

dir_path = os.path.dirname(os.path.realpath(__file__))
doc_list = os.path.abspath(os.path.join(dir_path,'aux/naics325412.csv'))

with open(doc_list) as oFile:
    reader = csv.reader(oFile)
    next(reader)
    for row in reader:
        article_title = row[0]
        subject = row[1]
        company = row[2]
        publication_title = row[3]
        
        date_string = row[4]
        print(date_string)
        if date_string == 'NA':
            publication_date = None
        else:
            year, month, day = date_string.split('-')
            publication_date = date(year=int(year),month=int(month),day=int(day))
        
        publication_subject = row[5]
        source_type = row[6]
        document_type = row[7]
        html = row[8]

        doc = Doc(
            article_title = article_title,
            subject = subject,
            company = company,
            publication_title = publication_title,
            publication_date = publication_date,
            publication_subject = publication_subject,
            source_type = source_type,
            document_type = document_type,
            html = html,
            )
        doc.save()
