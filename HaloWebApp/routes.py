from HaloWebApp import app, forms
from flask import request, render_template


@app.route('/', methods=['GET', 'POST'])
def search():
    searchForm = forms.HaloWebParameters(request.form)
    if request.method == "POST":
        player = request.form['player']
        labels,values=forms.haloParam(player)

        return render_template('results.html', labels=labels,result=values)
    return render_template('search.html', form=searchForm)
