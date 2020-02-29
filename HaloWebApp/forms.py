from wtforms.validators import DataRequired
from HaloWebApp import main_functions
import requests
from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
import json


class HaloWebParameters(FlaskForm):
    player = StringField('player', validators=[DataRequired()],

                        )
    SelectField('state',choices=[('TotalTimePlayed', 'TotalTimePlayed'),
                                                      ('TotalMatchesCompleted','TotalMatchesCompleted'),
                                                      ('TotalMatchesWon','TotalMatchesWon'),
                                                      ('TotalMatchesLost','TotalMatchesLost'),
                                                          ('TotalUnitsBuilt','TotalUnitsBuilt'),
                                                      ('TotalUnitsLost','TotalUnitsLost'),
                                                      ('TotalUnitsDestroyed','TotalUnitsDestroyed'),
                                                      ('HighestWaveCompleted','HighestWaveCompleted')

    ] )


def haloParam(player):

    url = "https://www.haloapi.com/stats/hw2/players/"+player+"/stats"
    contents = requests.get(url,
                            headers={"Ocp-Apim-Subscription-Key": '468f05ddc65248068b1dd813618d33a3'}).json()

    main_functions.save_to_file(contents,"HaloWebApp/JSON_Files/api.json")

    halo_player = main_functions.read_from_file("HaloWebApp/JSON_Files/api.json")

    TTP= halo_player["CustomSummary"]['SkirmishStats']['SinglePlayerStats']["TotalTimePlayed"]
    TMC= halo_player["CustomSummary"]['SkirmishStats']['SinglePlayerStats']["TotalMatchesCompleted"]
    TMW = halo_player["CustomSummary"]['SkirmishStats']['SinglePlayerStats']["TotalMatchesWon"]
    TML = halo_player["CustomSummary"]['SkirmishStats']['SinglePlayerStats']["TotalMatchesLost"]
    TUB = halo_player["CustomSummary"]['SkirmishStats']['SinglePlayerStats']["TotalUnitsBuilt"]
    TUL = halo_player["CustomSummary"]['SkirmishStats']['SinglePlayerStats']["TotalUnitsLost"]
    TUD = halo_player["CustomSummary"]['SkirmishStats']['SinglePlayerStats']["TotalUnitsDestroyed"]
    HWC = halo_player["CustomSummary"]['SkirmishStats']['SinglePlayerStats']["HighestWaveCompleted"]


    labels = ['TotalTimePlayed',
               'TotalMatchesCompleted',
                'TotalMatchesWon',
               'TotalMatchesLost',
               'TotalUnitsBuilt',
               'TotalUnitsLost',
               'TotalUnitsDestroyed',
               'TotalUnitsDestroyed',
               'HighestWaveCompleted']
    values = [TTP,TMC,TMW,TML,TUB,TUL,TUL,TUD,HWC]

    return labels,values

