from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Team, State, Color
# Create your views here.

def index(request):
    query1(1, 10, 30, 0, 0, 40, 0, 0, 6, 0, 0, 5, 0, 0.0, 10.0, 0, 0.0, 10)
    query2('Gold')
    query3('FloridaState')
    query4('FL', 'Maroon')
    query5(8)
    return HttpResponse("Hello, world. You're at the query index.")




def query1(use_mpg, min_mpg, max_mpg, use_ppg, min_ppg, max_ppg, use_rpg, min_rpg, max_rpg, use_apg, min_apg, max_apg, use_spg, min_spg, max_spg, use_bpg, min_bpg, max_bpg):
    use_array = [use_mpg, use_ppg, use_rpg, use_apg, use_spg, use_bpg]
    min_array = [min_mpg, min_ppg, min_rpg, min_apg, min_spg, min_bpg]
    max_array = [max_mpg, max_ppg, max_rpg, max_apg, max_spg, max_bpg]
    attributes = ['mpg', 'ppg', 'rpg', 'apg', 'spg', 'bpg']
    result = Player.objects.all()

    for i in range(len(use_array)):
        if use_array[i] == 1:
            attribute_filter = {}
            attribute_gte = attributes[i]+'__gte'
            attribute_lte = attributes[i]+'__lte'
            attribute_filter[attribute_gte] = min_array[i]
            attribute_filter[attribute_lte] = max_array[i]
            result = result.filter(**attribute_filter).values_list()

    print('PLAYER_ID TEAM_ID UNIFORM_NUM FIRST_NAME LAST_NAME MPG PPG RPG APG SPG BPG')
    for record in result:
        #for field in Player._meta.get_fields():
        #   print(str(getattr(record, field.name))+' ', end='')
        for field in record:
            print(str(field)+' ', end='')
        print('')


def query2(team_color):
    color = Color.objects.get(name=team_color)
    result = Team.objects.filter(color_id=color.color_id).values_list('name')
    print('Name')
    for record in result:
        for value in record:
            print(value)


def query3(team_name):
    team = Team.objects.get(name=team_name)
    result = Player.objects.filter(team_id=team.team_id).values_list('first_name', 'last_name').order_by('-ppg')
    print('FIRST_NAME LAST_NAME')
    for record in result:
        for value in record:
            print(value+' ', end='')
        print('')


def query4(team_state, team_color):
    state = State.objects.get(name=team_state)
    color = Color.objects.get(name=team_color)
    team = Team.objects.get(state_id=state.state_id, color_id=color.color_id)
    result = Player.objects.filter(team_id=team.team_id).values_list('first_name', 'last_name', 'uniform_num')
    print('FIRST_NAME LAST_NAME UNIFORM_NUM')
    for record in result:
        for value in record:
            print(str(value)+' ', end='')
        print('')


def query5(num_wins):
    teams = Team.objects.filter(wins__gte=num_wins).values_list('team_id')
    result = Player.objects.filter(team_id__in=teams).values_list('first_name', 'last_name', 'team__name', 'team__wins')
    print('FIRST_NAME LAST_NAME TEAM_NAME WINS')
    for record in result:
        for value in record:
            print(str(value)+' ', end='')
        print('')
