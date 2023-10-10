from django.shortcuts import render
from pathlib import Path
import json

pardir=Path(__file__).resolve().parent

# Create your views here.
def loadctx():
  with open(pardir / "context.json") as ctx_file:
    ctx = json.loads(ctx_file.read())
  del ctx_file
  return ctx

ctx = loadctx()


def index(request):
  return render(request, "index.html", ctx)