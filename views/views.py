from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify, make_response,send_file
from flask_login import login_required,current_user
from WebApp.db import dbconnection
from WebApp.db_functions import check_if_player_exist_game,get_rightleft_hand_table_data,check_rightleft_index_one,\
    create_hand_index_data,create_stats_row,get_bat_results_data,update_results_column,get_results_x_count,get_results_total_counts,\
    get_player_name,get_game_name,get_filtered_bat_results_data,get_filtered_rightleft_hand_table_data,get_filtered_bat_results_data_balltype,\
    get_roster_data,update_v_column,get_last_ball_strike_count,get_game_name,get_pitch_result,delete_row_from_stats_table


views = Blueprint('views', __name__)


@views.route("/", methods=['GET','POST'])
@login_required
def home():



    dbconnect = dbconnection()

    query = '''
        select game_id,game_name,game_date,location_setting from game
        '''


    dbconnect.execute(query)
    gamedata = dbconnect.fetchall()
    dbconnect.close()



    return render_template("home.html", gamedata=gamedata,name=current_user.name)


@views.route("/score", methods=['GET','POST'])
def score():


    return render_template("score.html")



@views.route("/select/<gameid>",methods=["POST","GET"])
@login_required
def studentscheduleVIEW(gameid):



    roster_data_by_game = get_roster_data()

    game_name = get_game_name(gameid)


    return render_template("select.html", game_name=game_name,roster_data_by_game=roster_data_by_game,gameid=gameid,name=current_user.name)





@views.route("/playing/<game>/<player>/<rowid>", methods=['GET', 'POST'])
@login_required
def playing1(game,player,rowid):




    bat_results_data = get_bat_results_data(rowid)

    last_ball_strike_count = get_last_ball_strike_count(rowid)

    last_ball_strike_count = last_ball_strike_count.split("/")


    main_dict = {}


    for xx in bat_results_data:
        data_n_cords = {xx[1]: {"BallIndex": xx[1], "BallType": xx[2],
                                "Xcord": xx[3], "Ycord": xx[4]
                                }}
        main_dict.update(data_n_cords)



    hand_index_data = get_rightleft_hand_table_data(player,game)

    introwid = int(rowid)

    # total count
    total_counts = get_results_total_counts(player,game)

    # player name
    player_name = get_player_name(player)

    # game name
    game_name = get_game_name(game)


    return render_template("playing.html",name=current_user.name,game_name=game_name,player_name=player_name,total_counts=total_counts,main_dict=main_dict,introwid=introwid,bat_results_data=bat_results_data,
                           hand_index_data=hand_index_data,game=game,player=player,rowid=rowid,last_ball_strike_count=last_ball_strike_count)



@views.route("/dev", methods=['GET', 'POST'])
@login_required
def dev():


    listofids = request.args.get("ToggleIds")
    game = request.args.get("gameid")
    player = request.args.get("playerid")
    balltype = request.args.get("type")



    hand_index_data = get_filtered_rightleft_hand_table_data(player, game, listofids)

    if balltype == 'filterall':

        bat_results_data = get_filtered_bat_results_data(listofids)

        main_dict = {}

        for xx in bat_results_data:
            data_n_cords = {xx[9]: {"BallIndex": xx[9], "BallType": xx[2],
                                    "Xcord": xx[3], "Ycord": xx[4]
                                    }}
            main_dict.update(data_n_cords)

        # total count
        total_counts = get_results_total_counts(player, game)

        # player name
        player_name = get_player_name(player)

        # game name
        game_name = get_game_name(game)

        return render_template("filter.html", name=current_user.name,game_name=game_name, player_name=player_name, total_counts=total_counts,
                               main_dict=main_dict, bat_results_data=bat_results_data,
                               hand_index_data=hand_index_data, game=game, player=player)


    elif balltype == 'filterfastball':
        balltype = 'Fastball'
    elif balltype == 'filterchangeup':
        balltype = 'Change Up'
    elif balltype == 'filtercurve':
        balltype = 'Curve Ball'



    bat_results_data = get_filtered_bat_results_data_balltype(listofids,balltype)

    main_dict = {}

    for xx in bat_results_data:
        data_n_cords = {xx[9]: {"BallIndex": xx[9], "BallType": xx[2],
                                "Xcord": xx[3], "Ycord": xx[4]
                                }}
        main_dict.update(data_n_cords)


    # total count
    total_counts = get_results_total_counts(player,game)

    # player name
    player_name = get_player_name(player)

    # game name
    game_name = get_game_name(game)


    return render_template("filter.html",game_name=game_name,player_name=player_name,total_counts=total_counts,main_dict=main_dict,bat_results_data=bat_results_data,
                           hand_index_data=hand_index_data,game=game,player=player)





@views.route("/createindexrowleftright", methods=['POST'])
@login_required
def createindexrowleftright():

    # finish up here next is call the create_hand_index_data db function
    gameid = request.form['gameid']
    playerid = request.form['playerid']
    HvsPIndex = request.form['HvsPIndex']
    RightLeftValue = request.form['RightLeftValue']
    #def create_hand_index_data(playerid, gameid,HvsPIndex,RightLeftValue):
    idx = create_hand_index_data(playerid,gameid,HvsPIndex,RightLeftValue)

    return str(idx)


@views.route("/creategame", methods=['POST'])
@login_required
def creategame():
    x = "x"

    GameName = request.form['GameName']
    GameDate = request.form['GameDate']
    GameLocation = request.form['GameLocation']

    dbconnect = dbconnection()

    query = (f''' 

INSERT INTO game
([game_name], [season_id],[game_date],[location_setting])
VALUES ('{GameName}', '1','{GameDate}','{GameLocation}');

    ''').format(GameName=GameName,GameDate=GameDate, GameLocation=GameLocation)

    print(query)

    dbconnect.execute(query)

    dbconnect.close()

    return 'True'


@views.route("/createplayerandstats", methods=['POST'])
@login_required
def createplayerandstats():
    x = "x"

    rosterid = request.form['rosterid']
    gameid = request.form['gameid']
    print(f"Game Id: {gameid}")
    print(f"Player Id: {rosterid}")

    # check
    checking = check_if_player_exist_game(rosterid,gameid)

    if checking:

        dbconnect = dbconnection()


        query = (
            f'''
        
        INSERT INTO player_hit_vs_ptich
        ([player_id],[game_id])
        VALUES ('{rosterid}','{gameid}');
    
            ''').format(rosterid=rosterid,gameid=gameid)

        dbconnect.execute(query)

        dbconnect.close()

        return "True"

    else:

        return "False"




@views.route("/createstatsrow", methods=['POST'])
@login_required
def createstatsrow():
    x = "x"

    rowid = request.form['rowid']
    tableballcount = request.form['tableballcount']
    balltype = request.form['balltype']
    inout = request.form['inout']
    PitchResults = request.form['PitchResults']
    xcord = request.form['xcord']
    ycord = request.form['ycord']
    ballinoutcount = request.form['ballinoutcount']
    strikeinoutcount = request.form['strikeinoutcount']


    ballstrike = str(ballinoutcount)+"/"+str(strikeinoutcount)


    create_stats_row(rowid,tableballcount,balltype,inout,PitchResults,xcord,ycord,ballstrike)



    return "yo"


#updateresultstable
@views.route("/updateresultstable", methods=['POST'])
@login_required
def updateresultstable():
    x = "x"

    rowid = request.form['rowid']
    results = request.form['results']
    game = request.form['game']
    player = request.form['player']
    countText = request.form['countText']


    update_results_column(rowid, results)
    # get_results_x_count(player,game,result)
    results_x_count = get_results_x_count(player, game, countText)
    results_x_count = str(results_x_count)


    return results_x_count



@views.route("/postVinput", methods=['POST'])
@login_required
def postVinput():


    rowid = request.form['rowid']
    ballindex = request.form['tableballcount']
    vinput = request.form['vinput']

    print(rowid,ballindex,vinput)

    update_v_column(rowid,ballindex,vinput)
    x = get_pitch_result(rowid,ballindex)
    print(x)

    return_dict = {}

    for xx in x:
        data_n_cords = {"pitch_results": x[0], "BallType": x[1]}


        return_dict.update(data_n_cords)

    print(return_dict)

    return return_dict



@views.route("/undobutton", methods=['POST'])
@login_required
def undobutton():

    rowid = request.form['rowid']
    #user_id = current_user.user_id
    delete = delete_row_from_stats_table(rowid)

    if delete == "None":
        return "None"

    return "yo"