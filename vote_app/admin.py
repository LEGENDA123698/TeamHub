from django.contrib import admin
from vote_app.models import *


admin.site.register(Vote)
admin.site.register(VoteAnswer)