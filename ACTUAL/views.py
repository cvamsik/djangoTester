from django.shortcuts import render
from django.http import HttpResponse
import json
import yfinance as yf
import datetime


def home(request):
    return render(request,'ACTUAL/HTML.html')
# Create your views here.
def result(request):
    symbol=request.GET['symbol']
    stockdata = yf.Ticker(symbol)
    error="Ticker Invalid"

    try:
      name=stockdata.info['longName']
    except KeyError:
      return render(request,'ACTUAL/HTML.html',{'error':error})
    except IndexError:
      return render(request,'ACTUAL/HTML.html',{'error':error})
    except ImportError:
      return render(request,'ACTUAL/HTML.html',{'error':error})

    name=stockdata.info['longName']
    openprice=stockdata.info['open']
    prevavg=stockdata.info['previousClose']
    valueChange=stockdata.info['open']-prevavg
    valueChange=round(valueChange,2)
    printchange=""
    if(valueChange>0):
      outputChange=("+"+str(valueChange))
    else:
      outputChange=("-"+str((valueChange*-1)))
    percentageChange=valueChange/prevavg
    percentageChange=round(percentageChange,2)
    outputPercentage=""
    if(percentageChange>0):
      outputPercentage=outputPercentage + ("+"+str(percentageChange)) + '%'
    else:
      outputPercentage=outputPercentage + ("-"+str((percentageChange*-1)))  + '%' 
    currentDT = datetime.datetime.now()
    output={'Symbol:': symbol ,'Date:':currentDT, 'Name:':name,'openprice:':openprice, 'ValueChange:': outputChange ,'PercentageChange:': outputPercentage }
    return render(request,'ACTUAL/HTML.html',{'outputs':output}) 
