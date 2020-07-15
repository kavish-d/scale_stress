# The MIT License (MIT)
#
# Copyright (c) 2014 Florian Neagu - michaelneagu@gmail.com - https://github.com/k3oni/
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import platform
import os
import multiprocessing
from datetime import timedelta

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
import time

lat=0.1

def home(request):
	global lat
	try:
		#set default to 0.1
		time.sleep(lat)
		# int(os.environ['latency']))
	except:
		pass
	return render_to_response('index.html', context_instance=RequestContext(request))

def latup(request):
	global lat
	try:
		lat=int(request.GET.get('value', lat))
	except:
		return HttpResponse(401)
	return HttpResponse(200)

def set_lat(l):
	global lat
	try:
		lat=int(l)
	except:
		pass
	return lat

def get_lat():
	global lat
	return lat