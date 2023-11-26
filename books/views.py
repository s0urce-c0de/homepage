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

with open(pardir / "url2book.json") as url2bookdictfile:
  url2bookdict = json.loads(url2bookdictfile.read())
del url2bookdictfile
# with open(pardir / "bookname.json") as booknamefile:
#   booknamelist = json.loads(booknamefile.read())
# del booknamefile

# Create your views here.
# def index(request):
#   lctx=loadctx()
#   lctx['books']=booknamelist
#   return render(request, "books-index.html", lctx)

def book(request, book):
  lctx = loadctx()
  lctx['book_data'] = goodreads_scrapper._real_main(url2bookdict[book])
  return render(request, 'book.html', lctx)