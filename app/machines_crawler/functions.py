from app import db
import math
import json
from sqlalchemy.sql import and_, or_

def get_pagination(page, per_page, query_result):
    registers = len(query_result)
    pages = math.ceil(registers / per_page)
    range_start = (int(page) - 1) * per_page
    range_end = range_start + per_page
    if str(page) == '1':
        has_prev = False
    else:
        has_prev = True

    if str(page) == str(pages):
        has_next = False
    else:
        has_next = True

    return pages, has_prev, has_next, range_start, range_end

def get_form_ajax_data(request, table_name, page, order_by_field, order_by_order, filter_dict):
    if request.form.get('page'):
        page = request.form['page']
    else:
        page = page
    if request.form.get('order_by_field'):
        order_by_field = request.form['order_by_field']
    else:
        order_by_field = order_by_field
    if request.form.get('order_by_order'):
        order_by_order = request.form['order_by_order']
    else:
        order_by_order = order_by_order
    if not request.form.get('filter_values'):  # VALORES INICIAIS
        for filter in filter_dict:
            get_field_name = getattr(table_name.columns, filter['field_name'])
            if filter['filter_type'] == 'select':
                all_options = db.session.query(get_field_name).all()
                option_set = [option[0] for option in all_options]
                select_option = list(set(option_set))
                filter.update({'filter_initial_value': select_option})
                filter.update({'filter_value': '%'})
            if filter['filter_type'] == 'date':
                if filter['filter_name'].endswith('start'):
                    date = db.session.query(db.func.min(get_field_name)).first()  # PRIMEIRA DATA
                elif filter['filter_name'].endswith('end'):
                    date = db.session.query(db.func.max(get_field_name)).first()  # ÚLTIMA DATA
                date_format = date[0].strftime("%Y-%m-%d")
                filter.update({'filter_initial_value': date_format})
                filter.update({'filter_value': date_format})

    else:  # VALORES RESULTANTES DOS FILTROS
        filters = request.form.get('filter_values')
        filters_json = json.loads(filters)
        for filter in filter_dict:
            filter.update({'filter_value': filters_json[filter['filter_name']]})

    return page, order_by_field, order_by_order, filter_dict

def get_filter(filter_dict, table_name):
    filters_list = []
    for filter in filter_dict:
        get_field_name = getattr(table_name.columns, filter['field_name'])
        if filter['filter_type'] == 'select':
            get_filter_value = get_field_name.like(filter['filter_value'])
        if filter['filter_name'].endswith('start'):
            get_filter_value = get_field_name >= (filter['filter_value'])
        if filter['filter_name'].endswith('end'):
            get_filter_value = get_field_name <= (filter['filter_value'])
        filters_list.append(get_filter_value)

    return filters_list

def get_response_params(
        request,
        table_name,
        per_page,
        page,
        order_by_field,
        order_by_order,
        filter_dict
        ):

    # ******** FORM AJAX DATA ******** #
    page, order_by_field, order_by_order, \
    filter_dict = \
        get_form_ajax_data(request, table_name, page, order_by_field, order_by_order, filter_dict)

    # ******** FILTROS ******** #
    filters_list = get_filter(filter_dict, table_name)

    # ******** ORDENAÇÃO ******** #

    get_order_field = getattr(table_name.columns, order_by_field)
    order_field = getattr(get_order_field, order_by_order)()

    # ******** QUERIES ******** #

    query_result = db.session.query(table_name) \
        .filter(and_(*filters_list)) \
        .order_by(order_field) \
        .all()

    # ******** PAGINAÇÃO ******** #

    pages, has_prev, has_next, \
    range_start, range_end = get_pagination(page, per_page, query_result)

    # ******** RESPONSE ******** #

    query_result = query_result[range_start:range_end]
    columns_description = db.session.query(table_name).column_descriptions
    fields_list = [column['name'] for column in columns_description]

    return query_result, fields_list, \
           order_by_field, order_by_order, \
           page, pages, \
           has_prev, has_next, filter_dict