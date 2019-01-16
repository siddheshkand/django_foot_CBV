from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . import models


def team_list(request):
    teams = models.Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})


def team_detail(request, pk):
    team = get_object_or_404(models.Team, pk=pk)
    return render(request, 'teams/team_detail.html', {'team': team})


class TeamListView(ListView):
    # Default template name is team_list.html ie: model_name_list.html
    model = models.Team
    context_object_name = "teams"


class TeamDetailView(DetailView):
    # Default template name is team_detail.html ie: model_name_detail.html
    # Also pk is the default arg passed to detail view
    model = models.Team
