from django.shortcuts import render

# Create your views here.
# TODO: Temporary database - REMOVE THIS AFTER ADDING FINCH MODEL
finches = [
  {'name': 'Toothless', 'breed': 'house finch', 'description': 'angry bird', 'age': 3},
  {'name': 'Piper', 'breed': 'purple finch', 'description': 'sweetest angel', 'age': 2},
]
# Create your views here.

def home(request):
    return render(request, 'home.html')

# add a new ve=uew function "about"
# it should render about.html
def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
        })