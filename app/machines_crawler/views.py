from . import machines_crawler

from flask import jsonify, render_template, request
from flask_login import login_required
from app.models import *
from app import db
import math
import json
from datetime import date
from sqlalchemy.sql import and_, or_
from sqlalchemy import create_engine
from sqlalchemy import inspect
from .functions import *


@machines_crawler.route('/machines_crawler/hist', methods=['GET', 'POST'])
@login_required
def hist():

    return render_template('machines_crawler/hist.html')


@machines_crawler.route('/machines_crawler/hist-post', methods=['POST'])
@login_required
def post_hist():

    # ******** INICIALIZAÇÃO ******** #
    table_name = t_price_crawler_hist
    per_page = 5 # NÚMERO DE REGISTROS POR PÁGINA
    page = 1 # PÁGINA INICIAL
    order_by_field = 'data_extracao' # COLUNA QUE FARÁ A ORDENAÇÃO INICIAL DA TABELA
    order_by_order = 'desc' # 'asc' - CRESCENTE ou 'desc' - DECRESCENTE
    filter_dict = [
        {'field_name': 'produto',
         'filter_type': 'select',
         'filter_name': 'select_produto',
        },
        {'field_name': 'loja',
         'filter_type': 'select',
         'filter_name': 'select_loja',
        },
        {'field_name': 'data_extracao',
         'filter_type': 'date',
         'filter_name': 'date_data_extracao_start',
         },
        {'field_name': 'data_extracao',
         'filter_type': 'date',
         'filter_name': 'date_data_extracao_end',
         }
    ]


    query_result, \
    fields_list, \
    order_by_field, \
    order_by_order, \
    page, \
    pages, \
    has_prev, \
    has_next, \
    filter_dict  =  get_response_params(
        request,
        table_name,
        per_page,
        page,
        order_by_field,
        order_by_order,
        filter_dict
    )


    if request.method == "POST":
        return jsonify({'query_result':query_result,
                        'fields_list':fields_list,
                        'order_by_field':order_by_field,
                        'order_by_order':order_by_order,
                        'page': page,
                        'pages': pages,
                        'has_prev': has_prev,
                        'has_next': has_next,
                        'filter_dict': filter_dict
                        })

    return jsonify({'error': 'MissingData'})


@machines_crawler.route('/machines_crawler/min', methods=['GET', 'POST'])
@login_required
def min():

    return render_template('machines_crawler/min.html')


@machines_crawler.route('/machines_crawler/min-post', methods=['POST'])
@login_required
def post_min():

    # ******** INICIALIZAÇÃO ******** #
    table_name = t_price_crawler_min
    per_page = 5 # NÚMERO DE REGISTROS POR PÁGINA
    page = 1 # PÁGINA INICIAL
    order_by_field = 'data_extracao' # COLUNA QUE FARÁ A ORDENAÇÃO INICIAL DA TABELA
    order_by_order = 'desc' # 'asc' - CRESCENTE ou 'desc' - DECRESCENTE
    filter_dict = [
        {'field_name': 'produto',
         'filter_type': 'select',
         'filter_name': 'select_produto',
        },
        {'field_name': 'loja',
         'filter_type': 'select',
         'filter_name': 'select_loja',
        },
        {'field_name': 'data_extracao',
         'filter_type': 'date',
         'filter_name': 'date_data_extracao_start',
         },
        {'field_name': 'data_extracao',
         'filter_type': 'date',
         'filter_name': 'date_data_extracao_end',
         }
    ]


    query_result, \
    fields_list, \
    order_by_field, \
    order_by_order, \
    page, \
    pages, \
    has_prev, \
    has_next, \
    filter_dict  =  get_response_params(
        request,
        table_name,
        per_page,
        page,
        order_by_field,
        order_by_order,
        filter_dict
    )


    if request.method == "POST":
        return jsonify({'query_result':query_result,
                        'fields_list':fields_list,
                        'order_by_field':order_by_field,
                        'order_by_order':order_by_order,
                        'page': page,
                        'pages': pages,
                        'has_prev': has_prev,
                        'has_next': has_next,
                        'filter_dict': filter_dict
                        })

    return jsonify({'error': 'MissingData'})


@machines_crawler.route('/machines_crawler/evolution', methods=['GET', 'POST'])
@login_required
def evolution():

    return render_template('machines_crawler/evolution.html')


@machines_crawler.route('/machines_crawler/evolution-post', methods=['POST'])
@login_required
def post_evolution():

    # ******** INICIALIZAÇÃO ******** #
    table_name = t_price_crawler_evolution
    per_page = 7 # NÚMERO DE REGISTROS POR PÁGINA
    page = 1 # PÁGINA INICIAL
    order_by_field = 'data_extracao' # COLUNA QUE FARÁ A ORDENAÇÃO INICIAL DA TABELA
    order_by_order = 'desc' # 'asc' - CRESCENTE ou 'desc' - DECRESCENTE
    filter_dict = [
        {'field_name': 'data_extracao',
         'filter_type': 'date',
         'filter_name': 'date_data_extracao_start',
         },
        {'field_name': 'data_extracao',
         'filter_type': 'date',
         'filter_name': 'date_data_extracao_end',
         }
    ]


    query_result, \
    fields_list, \
    order_by_field, \
    order_by_order, \
    page, \
    pages, \
    has_prev, \
    has_next, \
    filter_dict  =  get_response_params(
        request,
        table_name,
        per_page,
        page,
        order_by_field,
        order_by_order,
        filter_dict
    )


    if request.method == "POST":
        return jsonify({'query_result':query_result,
                        'fields_list':fields_list,
                        'order_by_field':order_by_field,
                        'order_by_order':order_by_order,
                        'page': page,
                        'pages': pages,
                        'has_prev': has_prev,
                        'has_next': has_next,
                        'filter_dict': filter_dict
                        })

    return jsonify({'error': 'MissingData'})


@machines_crawler.route('/machines_crawler/simple_chart')
@login_required
def line_chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]


    table_name = t_price_crawler_evolution
    dados = db.session.query(table_name).all()

    columns_description = db.session.query(table_name).column_descriptions
    fields_list = [column['name'] for column in columns_description]

    datas = [obj.data_extracao.strftime("%Y") + '-' +
             obj.data_extracao.strftime("%m") + '-' +
             obj.data_extracao.strftime("%d")
             for obj in dados]
    mini_me = [int(obj.mini_me) for obj in dados if int(obj.mini_me) > 0]
    essenza = [int(obj.essenza) for obj in dados if int(obj.essenza) > 0]
    inissia = [int(obj.inissia) for obj in dados if int(obj.inissia) > 0]
    mimo_cafeteira = [int(obj.mimo_cafeteira) for obj in dados if int(obj.mimo_cafeteira) > 0]
    pop_plus = [int(obj.pop_plus) for obj in dados if int(obj.pop_plus) > 0]

    context = {'legend': legend,
               'labels': labels,
               'values': values,
               'datas': datas,
               'mini_me': mini_me,
               'essenza': essenza,
               'inissia': inissia,
               'mimo_cafeteira': mimo_cafeteira,
               'pop_plus': pop_plus
               }

    return render_template('chartjs/custom_chart.html', context=context)
