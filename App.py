import GetData, DoMath, API
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def front_page():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        if request.form['button'] == 'submit':
            summoner1 = request.form['sum1']
            summoner2 = request.form['sum2']
            summoner3 = request.form['sum3']
            summoner4 = request.form['sum4']
            summoner5 = request.form['sum5']
            summoners = [summoner1, summoner2, summoner3, summoner4, summoner5]
            values = [name.lower().replace(" ", "") for name in summoners]
            values.append(request.form['region'])
            values.append(request.form['champions'])
            list_as_string = ','.join(values)
            return redirect(url_for('.results', values=list_as_string))

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
        list_as_string = request.args['values']
        values = list_as_string.split(',')
        summoners = values[:5]
        region = values[5]
        champ_count = int(values[6])
        if region not in ['NA', 'BR', 'EUNE', 'EUW', 'JP', 'KR', 'LAN', 'LAS', 'OCE', 'TR', 'RU']:
            return redirect(url_for('.error', values='Region not valid'))

        if champ_count < 15 or champ_count > 30:
            return redirect(url_for('.error', values='Champ count not valid'))

        # Get a dictionary that maps champion id to champion name
        champ_id_to_name = API.champion_lookup(region)
        # Get the champion name for later use, because 'champion 35' doesn't mean much to people
        champ_id_to_name = {key: value['name'] for key, value in champ_id_to_name.items()}

        try:
            summoner_data = gather_info(summoners, champ_count, champ_id_to_name, region)
        except KeyError as inst:
            err_message = str(inst)[1:-1]
            return redirect(url_for('.error', values=err_message))
        dream_team = build_team(summoner_data)
        answer0 = [dream_team[0].player, dream_team[0].role, dream_team[0].name, dream_team[0].id]
        answer1 = [dream_team[1].player, dream_team[1].role, dream_team[1].name, dream_team[1].id]
        answer2 = [dream_team[2].player, dream_team[2].role, dream_team[2].name, dream_team[2].id]
        answer3 = [dream_team[3].player, dream_team[3].role, dream_team[3].name, dream_team[3].id]
        answer4 = [dream_team[4].player, dream_team[4].role, dream_team[4].name, dream_team[4].id]
        team = [answer0, answer1, answer2, answer3, answer4]

        return render_template('results.html', results=team)

    if request.method == 'POST':
        if request.form['button'] == 'home':
            return redirect(url_for('.front_page'))


def gather_info(summoners, champ_count, champ_id_to_name, region):
    summoner_data = {}
    for player in summoners:
        summoner_id, summoner_name, account_id = GetData.get_summoner_data(player, region)
        champ_points_pair = GetData.get_summoners_mastery(summoner_id, summoner_name, champ_count, region)
        champ_counters = GetData.lanes_and_roles(account_id, summoner_name, champ_points_pair, champ_id_to_name, region)
        GetData.percentages(champ_counters)
        summoner_data[summoner_name] = GetData.data_compile(summoner_name, champ_counters,
                                                            champ_id_to_name, champ_points_pair)

    return summoner_data


def build_team(summoner_data):
    population = DoMath.populate_generation(summoner_data, 2500)
    population = DoMath.mutate(population, summoner_data)
    health = 0
    new_health = 1
    while health / new_health < .99:
        health = DoMath.grade_generation(population)
        population = DoMath.evolve(population)
        new_health = DoMath.grade_generation(population)

    dream_team = population[0]

    return dream_team
