# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

import csv

from .models import Doc

# Create your views here.

class DocUpdate(UpdateView):
    model = Doc
    fields = [
        'aboutProductLaunch',
        'aboutProductApproval',
        'mentionsProduct',
        'subjectProduct',
        'ifProductInBodyWhere',
        'subjectCompany',
        'otherCompany',
        'otherProduct',
        ]
        
    template_name = "rate_doc/doc_edit.html"
    
    def form_valid(self, form):
        form.instance.ratedBy = self.request.user
        form.instance.rated = True
        form.save()
        return HttpResponseRedirect(reverse('get-next'))


class DocList(ListView):
    model = Doc
    template_name = "rate_doc/doc_list.html"      


def get_next(request):

    assigned_doc = Doc.objects.filter(rated=False).filter(assignedTo=request.user.pk)
    if assigned_doc:
        doc = assigned_doc.first()
    else:
        doc = Doc.objects.filter(rated=False,assignedTo=None).first()
        doc.assignedTo = request.user
        doc.save()
    
    return HttpResponseRedirect(reverse('rate-doc', kwargs={'pk':doc.pk}))

    
def Export(request):
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="document_ratings.csv"'

    writer = csv.writer(response, quoting=csv.QUOTE_ALL)
    
    fields = [
        'pk',
        'rated',  
        'ratedBy__username',
        'aboutProductLaunch',
        'aboutProductApproval',
        'mentionsProduct',
        'ifProductInBodyWhere',
        'subjectProduct',
        'subjectCompany',
        'otherCompany',
        'otherProduct',
        'article_title',
        'subject',
        'company',
        'publication_title',
        'publication_date',
        'publication_subject',
        'source_type',
        'document_type',
        'html',
    ]    

    writer.writerow(fields)    
    
    docs = Doc.objects.all().values_list(*fields)
    for doc in docs:
        writer.writerow(doc)
        
    return response