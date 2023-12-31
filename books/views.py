from django.shortcuts import render
from pathlib import Path
from importlib.machinery import SourceFileLoader
import json
from django.template.defaulttags import register

pardir = Path(__file__).resolve().parent

goodreads_scrapper = SourceFileLoader("goodreads-scrapper",str(pardir / "goodreads-scrapper" / "goodreads-scrapper.py")).load_module()
# Create your views here.
def loadctx():
  with open(pardir / "context.json") as ctx_file:
    ctx = json.loads(ctx_file.read())
  del ctx_file
  return ctx

ctx = loadctx()

with open(pardir / "info.json") as infofile:
  info = json.loads(infofile.read())
del infofile

book_index={}
index=0
for i in info:
  book_index[i.url] = index
  index+=1
del i, index

# Create your views here.
# def index(request):
#   lctx=loadctx()
#   lctx['books']=booknamelist
#   return render(request, "books-index.html", lctx)

def book(request, book):
  lctx = loadctx()
  lctx['book_data'] = goodreads_scrapper._real_main(info[book_index[book]])
  return render(request, 'book.html', lctx)