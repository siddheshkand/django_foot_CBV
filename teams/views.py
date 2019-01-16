from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from . import models


class PlayerListView(ListView):
    model = models.Player


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


class TeamCreateView(CreateView):
    # Default template name is team_form.html ie: model_name_form.html
    # Can be overridden by template_name = "teams/team_form.html"
    model = models.Team
    fields = ["name", "practice_location", "coach"]  # requires field attr to which need to be included


class TeamUpdateView(UpdateView):
    fields = ["name", "practice_location", "coach"]
    model = models.Team


class TeamDeleteView(DeleteView):
    model = models.Team
    success_url = reverse_lazy("teams:list")
