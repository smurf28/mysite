# IPython log file

get_ipython().magic('logstart bug.py')
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
client = Client()
response = client.get('/')
response.status_code
from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code
response.content
response.context['latest_question_list']
exit()
