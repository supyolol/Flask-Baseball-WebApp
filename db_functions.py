import pyodbc
from WebApp.db import dbconnection

def check_if_player_exist_game(playerid,gameid):


    dbconnect = dbconnection()

    query = '''
    select id from player_hit_vs_ptich
where player_id = '{playerid}'
and game_id = '{gameid}'
    
    '''.format(playerid=playerid,gameid=gameid)

    dbconnect.execute(query)

    sqldata = dbconnect.fetchone()
    dbconnect.close()

    if sqldata:
        return False
    else:
        return True


def get_rightleft_hand_table_data(playerid, gameid):

    dbconnect = dbconnection()

    query = '''
    select id,player_id,game_id,hitter_vs_pitcher_index,left_right_handed,results
    from player_hit_vs_ptich
    where player_id = '{playerid}'
    and game_id = '{gameid}'

    '''.format(playerid=playerid, gameid=gameid)

    dbconnect.execute(query)

    sqldata = dbconnect.fetchall()

    dbconnect.close()

    return sqldata


def get_filtered_rightleft_hand_table_data(playerid, gameid, listrowids):

    dbconnect = dbconnection()

    query = '''
    select id,player_id,game_id,hitter_vs_pitcher_index,left_right_handed,results
    from player_hit_vs_ptich
    where player_id = '{playerid}'
    and game_id = '{gameid}'
    and id in ({listrowids})

    '''.format(playerid=playerid, gameid=gameid,listrowids=listrowids)


    dbconnect.execute(query)

    sqldata = dbconnect.fetchall()

    dbconnect.close()

    return sqldata






def check_rightleft_index_one(playerid, gameid):

    dbconnect = dbconnection()

    query = '''
    select id,player_id,game_id,hitter_vs_pitcher_index,left_right_handed
    from player_hit_vs_ptich
    where player_id = '{playerid}'
    and game_id = '{gameid}'
    and hitter_vs_pitcher_index = '1'

    '''.format(playerid=playerid, gameid=gameid)

    dbconnect.execute(query)

    sqldata = dbconnect.fetchone()
    dbconnect.close()

    if sqldata:
        return False
    else:
        return True



def get_rightleft_hand_table_id(playerid,gameid,HvsPIndex,RightLeftValue):

    dbconnect = dbconnection()

    query = '''
    select id
    from player_hit_vs_ptich
    where player_id = '{playerid}'
    and game_id = '{gameid}'
    and hitter_vs_pitcher_index = '{HvsPIndex}'
    and left_right_handed = '{RightLeftValue}'

    '''.format(playerid=playerid, gameid=gameid, HvsPIndex=HvsPIndex,RightLeftValue=RightLeftValue)

    dbconnect.execute(query)

    sqldata = dbconnect.fetchone()

    sqldata = sqldata[0]

    dbconnect.close()


    return sqldata



def create_hand_index_data(playerid,gameid,HvsPIndex,RightLeftValue):


    dbconnect = dbconnection()

    query = (
        f'''

    INSERT INTO player_hit_vs_ptich
    ([player_id],[game_id],[hitter_vs_pitcher_index],[left_right_handed])
    VALUES ('{playerid}','{gameid}','{HvsPIndex}','{RightLeftValue}');

        ''').format(playerid=playerid, gameid=gameid,
                    HvsPIndex=HvsPIndex,RightLeftValue=RightLeftValue)


    dbconnect.execute(query)


    idx = get_rightleft_hand_table_id(playerid,gameid,HvsPIndex,RightLeftValue)


    dbconnect.close()


    return idx


def create_stats_row(rowid,ballcount,balltype,inout,pitchresults,xcord,ycord,ballstrike):


    dbconnect = dbconnection()

    query = (
        f'''

        
            INSERT INTO player_hit_vs_ptich_stats
            ([id],
            [ball_index],
            [ball_type],
            [ball_x_cords],
            [ball_y_cords],
            [in_out],
            [pitch_results],
            [ball_strike])
            VALUES ({rowid},
            '{ballcount}',
            '{balltype}',
            '{xcord}',
            '{ycord}',
            '{inout}',
            '{pitchresults}',
            '{ballstrike}');
        
        ''').format(rowid=rowid, ballcount=ballcount,
                    balltype=balltype,inout=inout,pitchresults=pitchresults,
                    xcord=xcord,ycord=ycord,ballstrike=ballstrike)


    dbconnect.execute(query)
    dbconnect.close()


    return "Hello"


def get_bat_results_data(rowid):

    dbconnect = dbconnection()

    query = '''
  select
        [id]
      ,[ball_index]
      ,[ball_type]
      ,[ball_x_cords]
      ,[ball_y_cords]
      ,[in_out]
      ,[velocity]
      ,[ball_strike]
      ,[pitch_results]
  from player_hit_vs_ptich_stats
  where id = '{rowid}'
  ORDER BY [created_time_stamp]

    '''.format(rowid=rowid)

    dbconnect.execute(query)

    sqldata = dbconnect.fetchall()



    dbconnect.close()


    return sqldata


def get_filtered_bat_results_data(rowid):

    dbconnect = dbconnection()

    query = '''
  select
        [id]
      ,[ball_index]
      ,[ball_type]
      ,[ball_x_cords]
      ,[ball_y_cords]
      ,[in_out]
      ,[velocity]
      ,[ball_strike]
      ,[pitch_results]
      ,ROW_NUMBER() OVER (order by ball_type desc) AS table_index
  from player_hit_vs_ptich_stats
  where id in ({rowid})

    '''.format(rowid=rowid)



    dbconnect.execute(query)

    sqldata = dbconnect.fetchall()



    dbconnect.close()


    return sqldata


def get_filtered_bat_results_data_balltype(rowid,balltype):

    dbconnect = dbconnection()

    query = '''
  select
        [id]
      ,[ball_index]
      ,[ball_type]
      ,[ball_x_cords]
      ,[ball_y_cords]
      ,[in_out]
      ,[velocity]
      ,[ball_strike]
      ,[pitch_results]
      ,ROW_NUMBER() OVER (order by ball_type desc) AS table_index
  from player_hit_vs_ptich_stats
  where id in ({rowid})
  and ball_type = '{balltype}'

    '''.format(rowid=rowid,balltype=balltype)


    dbconnect.execute(query)

    sqldata = dbconnect.fetchall()



    dbconnect.close()


    return sqldata


def update_results_column(rowid,result):


    dbconnect = dbconnection()

    query = (
        f'''

update player_hit_vs_ptich
SET results = '{result}'
where id = '{rowid}'
        ''').format(rowid=rowid, result=result)



    dbconnect.execute(query)



    dbconnect.close()

    return "True"

def get_results_x_count(player,game,result):


    dbconnect = dbconnection()

    query = (
        f'''
select count (results) as results_x_count
from player_hit_vs_ptich
where player_id = '{player}'
and game_id = '{game}'
and results like '%{result}%'

        ''').format(player=player,game=game,result=result)



    dbconnect.execute(query)
    results_x_count = dbconnect.fetchone()
    results_x_count = results_x_count[0]

    dbconnect.close()

  
    return results_x_count

def get_results_total_counts(player,game):


    dbconnect = dbconnection()

    query = (
        f'''
select (

select count (results) as results_hit_count
from player_hit_vs_ptich
where player_id = '{player}'
and game_id = '{game}'
and results like '%Hit%'
) as results_Hit_count,
 (

select count (results) as results_walk_count
from player_hit_vs_ptich
where player_id = '{player}'
and game_id = '{game}'
and results like '%KL%'
) as results_walk_count,
 (

select count (results) as results_KL_count
from player_hit_vs_ptich
where player_id = '{player}'
and game_id = '{game}'
and results like '%Walk%'
) as results_KL_count,
 (

select count (results) as results_out_count
from player_hit_vs_ptich
where player_id = '{player}'
and game_id = '{game}'
and results like '%HBP%'
) as results_out_count,
 (

select count (results) as results_HBP_count
from player_hit_vs_ptich
where player_id = '{player}'
and game_id = '{game}'
and results like '%Out%'
) as results_HBP_count,
 (

select count (results) as results_total_count
from player_hit_vs_ptich
where player_id = '{player}'
and game_id = '{game}'
) as results_total_count

        ''').format(player=player,game=game)



    dbconnect.execute(query)
    results_total_count = dbconnect.fetchone()
    results_total_count = results_total_count

    dbconnect.close()


    return results_total_count



def get_player_name(player):


    dbconnect = dbconnection()

    query = (
        f'''

select first_name,last_name from roster
where player_id = '{player}'

        ''').format(player=player)


    dbconnect.execute(query)
    player_name = dbconnect.fetchone()

    dbconnect.close()


    return player_name


def get_game_name(game):


    dbconnect = dbconnection()

    query = (
        f'''
        
        select game_name from game
        where game_id = '{game}'

        ''').format(game=game)


    dbconnect.execute(query)
    game_name = dbconnect.fetchone()

    dbconnect.close()


    return game_name


def get_roster_data():

    dbconnect = dbconnection()

    query = (
        f'''
        
    select player_id,first_name,last_name
    from roster

        ''')

    dbconnect.execute(query)
    rosterdata = dbconnect.fetchall()

    dbconnect.close()

 
    return rosterdata


def get_game_name(gameid):
    dbconnect = dbconnection()

    query = (
        f'''

   select game_name from game
  where game_id = '{gameid}'

        ''')

    dbconnect.execute(query)
    gamename = dbconnect.fetchall()

    dbconnect.close()


    return gamename


def update_v_column(rowid,ballindex,vinput):


    dbconnect = dbconnection()

    query = (
        f'''

update player_hit_vs_ptich_stats
set velocity = '{vinput}'
where id = '{rowid}' and ball_index = '{ballindex}'

        ''').format(rowid=rowid, ballindex=ballindex,vinput=vinput)

    print(query)


    dbconnect.execute(query)




    dbconnect.close()


    return "True"


def get_last_ball_strike_count(rowid):

    dbconnect = dbconnection()

    query = (
        f'''

  select top 1 ball_strike from player_hit_vs_ptich_stats
  where id = '{rowid}'
  ORDER BY ball_index DESC

        ''').format(rowid=rowid)


    dbconnect.execute(query)

    ballstrikecount = dbconnect.fetchone()

    if(ballstrikecount):
        ballstrikecount = ballstrikecount[0]
    else:
        ballstrikecount = "None/None"


    dbconnect.close()


    return ballstrikecount



def get_user_id(email):

    dbconnect = dbconnection()

    query = (
        f'''

            SELECT user_id
            FROM users
            WHERE email = '{email}';

        ''').format(email=email)

    print(query)
    dbconnect.execute(query)

    user_id = dbconnect.fetchone()

    user_id = user_id[0]

    user_id_unicode = str(user_id).encode("utf-8").decode("utf-8")

    dbconnect.close()

    return user_id_unicode



def get_user_id_by_id(id):

    dbconnect = dbconnection()

    query = (
        f'''

            SELECT user_id
            FROM users
            WHERE user_id = '{id}';

        ''').format(id=id)

    print(query)
    dbconnect.execute(query)

    user_id = dbconnect.fetchone()

    user_id = user_id[0]

    user_id_unicode = str(user_id).encode("utf-8").decode("utf-8")

    dbconnect.close()

    return user_id_unicode

def get_user_name_by_email(email):

    dbconnect = dbconnection()

    query = (
        f'''

            SELECT first_name
            FROM users
            WHERE email = '{email}';

        ''').format(email=email)

    print(query)
    dbconnect.execute(query)

    user_name = dbconnect.fetchone()

    user_name = user_name[0]

    dbconnect.close()

    return user_name


def get_user_name_by_id(id):

    dbconnect = dbconnection()

    query = (
        f'''

            SELECT first_name
            FROM users
            WHERE user_id = '{id}';

        ''').format(id=id)

    print(query)
    dbconnect.execute(query)

    user_name = dbconnect.fetchone()

    user_name = user_name[0]

    dbconnect.close()

    return user_name


def get_pitch_result(id,ballindex):

    dbconnect = dbconnection()

    query = (
        f'''

  select pitch_results,ball_type from player_hit_vs_ptich_stats
  where id = '{id}' and ball_index = '{ballindex}'



        ''').format(id=id)

    print(query)
    dbconnect.execute(query)

    pitch_results = dbconnect.fetchone()



    dbconnect.close()

    return pitch_results





def check_row_from_stats_table(rowid):
    dbconnect = dbconnection()

    query = (
        f'''

select top 1 id from player_hit_vs_ptich_stats
where id = '{rowid}'

        ''').format(rowid=rowid)

    x = dbconnect.execute(query)
    x = x.fetchone()
    dbconnect.close()

    if x:
        return "success"
    else:
        return "None"





def delete_row_from_stats_table(rowid):


    datacheck = check_row_from_stats_table(rowid)
    print(datacheck)

    if datacheck != 'None':


        dbconnect = dbconnection()

        query = (
            f'''
    
        delete from player_hit_vs_ptich_stats
        where id IN 
        ( select top 1 id from player_hit_vs_ptich_stats
        where id = '{rowid}' ORDER BY created_time_stamp DESC)
        and ball_index IN (
        select top 1 ball_index from player_hit_vs_ptich_stats
        where id = '{rowid}' ORDER BY created_time_stamp DESC)
    
            ''').format(rowid=rowid)

        dbconnect.execute(query)


        dbconnect.close()

        return "success"

    else:

        return "None"


def create_login_attempt_log(email, client_ip, status):

    dbconnect = dbconnection()

    query = (
        f'''


            INSERT INTO login_log
            (
            [email],
            [client_ip],
            [status] )
            VALUES (
            '{email}',
            '{client_ip}',
            '{status}');

        ''').format(email=email, client_ip=client_ip,
                    status=status)

    dbconnect.execute(query)
    dbconnect.close()

    return "Hello"


def create_vistor_log(client_ip):

    dbconnect = dbconnection()

    query = (
        f'''
            INSERT INTO [vistor_log]
            (
            [client_ip]
            )
            VALUES (
            '{client_ip}'
            );

        ''').format(client_ip=client_ip)


    dbconnect.execute(query)
    dbconnect.close()

    return "Hello"
