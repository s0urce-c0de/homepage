from django.shortcuts import render
from pathlib import Path
from importlib.machinery import SourceFileLoader
import json

pardir = Path(__file__).resolve().parent

imdb_scrapper = SourceFileLoader("imdb-scrapper",str(pardir / "imdb-scrapper" / "imdb-scrapper.py")).load_module()
# Create your views here.
def loadctx():
  with open(pardir / "context.json") as ctx_file:
    ctx = json.loads(ctx_file.read())
  del ctx_file
  return ctx

ctx = loadctx()

with open(pardir / "url2movie.json") as url2moviedictfile:
  url2moviedict = json.loads(url2moviedictfile.read())
del url2moviedictfile
with open(pardir / "moviename.json") as movienamefile:
  movienamelist = json.loads(movienamefile.read())
del movienamefile

# Create your views here.
def index(request):
  lctx=loadctx()
  lctx['movies']=movienamelist
  return render(request, "movies-index.html", lctx)

def movie(request, movie):

  lctx = loadctx()
  lctx['movie_data'] = imdb_scrapper._real_main(url2moviedict[movie])
  return render(request, 'movie.html', lctx)