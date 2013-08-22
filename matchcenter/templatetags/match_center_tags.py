from django import template
from matchcenter.helpers import get_fixture

register = template.Library()

LEAGUE_ID = 1
SEASON_ID = 9064

@register.inclusion_tag('_vs_fixture.html')
def sl_fixture(match_id):
    weeks, currentWeek = get_fixture(LEAGUE_ID, SEASON_ID, int(match_id))
    return {"weeks": weeks, "currentWeek": currentWeek}

@register.inclusion_tag('_vs_before_playerlistitem.html')
def sl_before_playerlistitem(player):
    return {
        "class": ('starting' if player.get('eleven')==1 else 'sub'),
        "player": player
    }

@register.inclusion_tag('_vs_center_eventitem.html', takes_context=True)
def sl_center_eventitem(context, event, homeSquad, awaySquad):

    img_lookup = lambda x: {
        0: "images/goal.png",
        1: "images/own-goal.png",
        2: "images/penalty.png",
        3: "images/missed-pen.png",
        4: "images/yellow.png",
        5: "images/second-yellow.png",
        6: "images/red.png",
    }.get(x)

    ctx = {
        "event": event,
        "homeSquad": homeSquad,
        "awaySquad": awaySquad,
        "eventImagePath": img_lookup(int(event["type"])),
        "homeTeamId": context.get("homeTeamId"),
        "awayTeamId": context.get("awayTeamId")
    }

    return ctx