import get_data, do_math
from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def front_page():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        if request.form['button'] == 'submit':
            summoner1 = request.form['sum1'].lower().replace(" ", "")
            summoner2 = request.form['sum2'].lower().replace(" ", "")
            summoner3 = request.form['sum3'].lower().replace(" ", "")
            summoner4 = request.form['sum4'].lower().replace(" ", "")
            summoner5 = request.form['sum5'].lower().replace(" ", "")
            region = request.form['region']
            champ_count = request.form['champions']
            picked_list = []
            banned_list = []
            return redirect(url_for('.results', sum1=summoner1, sum2=summoner2, sum3=summoner3, sum4=summoner4,
                                    sum5=summoner5, region=region, champnum=champ_count, picked=picked_list,
                                    banned=banned_list))

        if request.form['button'] == 'about':
            return redirect(url_for('.about'))


@app.route("/about", methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        return render_template('about.html')

    if request.method == 'POST':
        if request.form['button'] == 'home':
            return redirect(url_for('.front_page'))


@app.route("/error", methods=['GET', 'POST'])
def error():
    if request.method == 'GET':
        error_message = request.args['values']
        return render_template('error.html', error=error_message)

    if request.method == 'POST':
        if request.form['button'] == 'home':
            return redirect(url_for('.front_page'))


@app.route("/results", methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        summoner1 = request.args['sum1']
        summoner2 = request.args['sum2']
        summoner3 = request.args['sum3']
        summoner4 = request.args['sum4']
        summoner5 = request.args['sum5']
        region = request.args['region']
        champ_count = int(request.args['champnum'])

        # Get a dictionary that maps champion id to champion name
        dir_path = os.path.dirname(os.path.realpath(__file__))
        champ_file = '{0}/{1}'.format(dir_path, 'champion_dict.json')
        with open(champ_file) as f:
            champ_id_to_name = json.load(f)
        # Get the champion name for later use, because 'champion 35' doesn't mean much to people
        champ_id_to_name = {key: value['name'] for key, value in champ_id_to_name.items()}

        try:
            picked_list = set(request.args['picked'].split(','))
        except KeyError:
            picked_list = set()
        try:
            banned_list = set(request.args['banned'].split(','))
        except KeyError:
            banned_list = set()
        try:
            assert len(picked_list) <= 5
            assert len(banned_list) <= 15
        except AssertionError:
            return redirect(url_for('.error', values='You tampered with the picked or banned list.'
                                                     ' Please don\'t do that!'))

        summoners = [summoner1, summoner2, summoner3, summoner4, summoner5]

        if region not in ['NA', 'BR', 'EUNE', 'EUW', 'JP', 'KR', 'LAN', 'LAS', 'OCE', 'TR', 'RU']:
            return redirect(url_for('.error', values='Region not valid'))

        if champ_count < 15 or champ_count > 30:
            return redirect(url_for('.error', values='Champ count not valid'))

        try:
            summoner_data = gather_info(summoners, champ_count, champ_id_to_name, region)
        except KeyError as inst:
            err_message = str(inst)[1:-1]
            return redirect(url_for('.error', values=err_message))
        dream_team = build_team(summoner_data, picked_list, banned_list)
        answer0 = [dream_team[0].player, dream_team[0].role, dream_team[0], dream_team[0].id]
        answer1 = [dream_team[1].player, dream_team[1].role, dream_team[1], dream_team[1].id]
        answer2 = [dream_team[2].player, dream_team[2].role, dream_team[2], dream_team[2].id]
        answer3 = [dream_team[3].player, dream_team[3].role, dream_team[3], dream_team[3].id]
        answer4 = [dream_team[4].player, dream_team[4].role, dream_team[4], dream_team[4].id]
        team = [answer0, answer1, answer2, answer3, answer4]

        return render_template('results.html', results=team)

    if request.method == 'POST':
        if request.form['button'] == 'home':
            return redirect(url_for('.front_page'))
        if request.form['button'] == 'recalculate':
            summoner1 = request.args['sum1']
            summoner2 = request.args['sum2']
            summoner3 = request.args['sum3']
            summoner4 = request.args['sum4']
            summoner5 = request.args['sum5']
            region = request.args['region']
            champ_count = int(request.args['champnum'])

            try:
                past_picked = set(request.args['picked'].split(','))
            except KeyError:
                past_picked = set()
            try:
                past_banned = set(request.args['banned'].split(','))
            except KeyError:
                past_banned = set()

            try:
                champ1 = request.form['pb1']
            except KeyError:
                champ1 = None
            try:
                champ2 = request.form['pb2']
            except KeyError:
                champ2 = None
            try:
                champ3 = request.form['pb3']
            except KeyError:
                champ3 = None
            try:
                champ4 = request.form['pb4']
            except KeyError:
                champ4 = None
            try:
                champ5 = request.form['pb5']
            except KeyError:
                champ5 = None
            pb_list = [champ1, champ2, champ3, champ4, champ5]
            pb_list = {value for value in pb_list if value is not None}
            picked_list = ",".join([name[:-1] for name in pb_list if name[-1] == 'P'] + list(past_picked))
            banned_list = ",".join([name[:-1] for name in pb_list if name[-1] == 'B'] + list(past_banned))
            return redirect(url_for('.results', sum1=summoner1, sum2=summoner2, sum3=summoner3, sum4=summoner4,
                                    sum5=summoner5, region=region, champnum=champ_count, picked=picked_list,
                                    banned=banned_list))


def gather_info(summoners, champ_count, champ_id_to_name, region):
    summoner_data = {}
    for player in summoners:
        summoner_id, summoner_name, account_id = get_data.get_summoner_data(player, region)
        champ_points_pair = get_data.get_summoners_mastery(summoner_id, summoner_name, champ_count, region)
        champ_counters = get_data.lanes_and_roles(account_id, summoner_name, champ_points_pair, champ_id_to_name, region)
        get_data.percentages(champ_counters)
        summoner_data[summoner_name] = get_data.data_compile(summoner_name, champ_counters,
                                                             champ_id_to_name, champ_points_pair)

    return summoner_data


def build_team(summoner_data, picked_list, banned_list):
    population = do_math.populate_generation(summoner_data, 5000, picked_list, banned_list)
    health = 0
    new_health = 1
    while health / new_health < .995:
        health = do_math.grade_generation(population)
        population = do_math.evolve(population, picked_list, banned_list)
        population = do_math.mutate(population, summoner_data, picked_list, banned_list)
        new_health = do_math.grade_generation(population)

    dream_team = population[0]

    return dream_team
