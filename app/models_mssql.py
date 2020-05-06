# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, Integer, MetaData, Numeric, String, Table, Unicode

metadata = MetaData()


t_Price_Crawler_Essenza_Hist = Table(
    'Price_Crawler_Essenza_Hist', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Essenza_dayly = Table(
    'Price_Crawler_Essenza_dayly', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Evolution = Table(
    'Price_Crawler_Evolution', metadata,
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('mini me', Float(53)),
    Column('essenza', Float(53)),
    Column('inissia', Float(53)),
    Column('mimo cafeteira', Float(53)),
    Column('pop plus', Float(53))
)


t_Price_Crawler_Hist = Table(
    'Price_Crawler_Hist', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Inissia_Hist = Table(
    'Price_Crawler_Inissia_Hist', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Inissia_dayly = Table(
    'Price_Crawler_Inissia_dayly', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Mimo_Hist = Table(
    'Price_Crawler_Mimo_Hist', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Mimo_dayly = Table(
    'Price_Crawler_Mimo_dayly', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Min_Price = Table(
    'Price_Crawler_Min_Price', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Mini_Me_Hist = Table(
    'Price_Crawler_Mini_Me_Hist', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Mini_Me_dayly = Table(
    'Price_Crawler_Mini_Me_dayly', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Pop_Plus_Hist = Table(
    'Price_Crawler_Pop_Plus_Hist', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_Price_Crawler_Pop_Plus_dayly = Table(
    'Price_Crawler_Pop_Plus_dayly', metadata,
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Data de Extração', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Loja', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Preço', Float(53))
)


t_actions_contact = Table(
    'actions_contact', metadata,
    Column('email', Unicode),
    Column('Tipo de Contato', Unicode),
    Column('Número', Unicode),
    Column('Unidade', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Data', DateTime),
    Column('action_sequence', BigInteger),
    Column('action_sequence_desc', BigInteger),
    Column('action_tipo_sequence', BigInteger),
    Column('action_tipo_sequence_desc', BigInteger)
)


t_advil_trends_rising = Table(
    'advil_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_advil_trends_top = Table(
    'advil_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_analysis_capsula_consumidor = Table(
    'analysis_capsula_consumidor', metadata,
    Column('email', Unicode),
    Column('capsula', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('OptinOut', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('qtd', Float(53)),
    Column('perfil_compra_capsula', String(14, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
)


t_analysis_caseiro_uplift = Table(
    'analysis_caseiro_uplift', metadata,
    Column('email', Unicode),
    Column('Qtd_anterior', Float(53)),
    Column('Qtd_atual', Float(53)),
    Column('Diferença', Float(53))
)


t_analysis_correlation_box = Table(
    'analysis_correlation_box', metadata,
    Column('Ordem', BigInteger),
    Column('capsula', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Caffè Matinal', Float(53)),
    Column('Café Au Lait', Float(53)),
    Column('Cappuccino', Float(53)),
    Column('Caramel Latte Macchiato', Float(53)),
    Column('Chai Tea Latte', Float(53)),
    Column('Chococino', Float(53)),
    Column('Chococino Caramel', Float(53)),
    Column('Cortado', Float(53)),
    Column('Espresso', Float(53)),
    Column('Espresso Barista', Float(53)),
    Column('Espresso Decaffeinato', Float(53)),
    Column('Espresso Intenso', Float(53)),
    Column('Latte Macchiato', Float(53)),
    Column('Lungo', Float(53)),
    Column('Marrakesh Style Tea', Float(53)),
    Column('Mocha', Float(53)),
    Column('Mochaccino Canela', Float(53)),
    Column('Nescau', Float(53)),
    Column('Nestea® Limão', Float(53)),
    Column('Nestea® Pêssego', Float(53)),
    Column('Ristretto', Float(53)),
    Column('Ristretto Ardenza', Float(53)),
    Column('STARBUCKS CARAMEL MACCHIATO - 12 CÁPSULAS', Float(53)),
    Column('Starbucks Americano House Blend - 12 Cápsulas', Float(53)),
    Column('Starbucks Blonde Espresso Roast - 12 Cápsulas', Float(53)),
    Column('Starbucks Cappuccino - 12 Cápsulas', Float(53)),
    Column('Starbucks Espresso Roast - 12 Cápsulas', Float(53)),
    Column('Starbucks Latte Macchiato - 12 Cápsulas', Float(53)),
    Column('Vanilla Latte Macchiato', Float(53))
)


t_analysis_novos_sabores_caseiro = Table(
    'analysis_novos_sabores_caseiro', metadata,
    Column('email', Unicode),
    Column('Última_Compra', String(7, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Penúltima_Compra', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Faixas', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('variacao', String(27, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cápsulas', Float(53)),
    Column('delta_Cápsulas', Float(53)),
    Column('Total_Variação', Float(53)),
    Column('Caps/Ordem', Float(53))
)


t_analysis_novos_sabores_caseiro_temp = Table(
    'analysis_novos_sabores_caseiro_temp', metadata,
    Column('email', Unicode),
    Column('Última_Compra', String(7, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Penúltima_Compra', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Faixas', String(10, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_analysis_novos_sabores_caseiro_temp_2 = Table(
    'analysis_novos_sabores_caseiro_temp_2', metadata,
    Column('email', Unicode),
    Column('Última_Compra', String(7, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Penúltima_Compra', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Faixas', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('variacao', String(27, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cápsulas', Float(53)),
    Column('delta_Cápsulas', Float(53))
)


t_analysis_novos_sabores_desnatado = Table(
    'analysis_novos_sabores_desnatado', metadata,
    Column('email', Unicode),
    Column('Última_Compra', String(9, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Penúltima_Compra', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Faixas', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('variacao', String(27, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cápsulas', Float(53)),
    Column('delta_Cápsulas', Float(53)),
    Column('Total_Variação', Float(53)),
    Column('Caps/Ordem', Float(53))
)


t_analysis_novos_sabores_desnatado_temp_2 = Table(
    'analysis_novos_sabores_desnatado_temp_2', metadata,
    Column('email', Unicode),
    Column('Última_Compra', String(9, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Penúltima_Compra', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Faixas', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('variacao', String(27, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cápsulas', Float(53)),
    Column('delta_Cápsulas', Float(53))
)


t_analysis_perfil_consumidor = Table(
    'analysis_perfil_consumidor', metadata,
    Column('email', Unicode),
    Column('perfil', String(11, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_analysis_preco_medio_consumidor = Table(
    'analysis_preco_medio_consumidor', metadata,
    Column('email', Unicode),
    Column('preco_medio_capsula', Float(53)),
    Column('classificacao', String(11, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
)


t_analysis_rfv_total = Table(
    'analysis_rfv_total', metadata,
    Column('email', Unicode),
    Column('OptinOut', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Consumo de Cápsulas', Float(53)),
    Column('Recency', Integer),
    Column('Faixa_Recency', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Frequency', Integer),
    Column('Faixa_Frequency', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Value', Float(53)),
    Column('Faixa_Value', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Score', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Segment', String(11, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_analysis_rfv_total_labels = Table(
    'analysis_rfv_total_labels', metadata,
    Column('Faixa', BigInteger),
    Column('Recencia_De_Dias', BigInteger),
    Column('Recência_Até_Dias', BigInteger),
    Column('Frequência_De_Compras', BigInteger),
    Column('Frequência_Até_Compras', BigInteger),
    Column('Valor_De_Cáps', BigInteger),
    Column('Valor_Até_Cáps', BigInteger)
)


t_analysis_sales = Table(
    'analysis_sales', metadata,
    Column('email', Unicode),
    Column('customerid', Unicode),
    Column('ordernumber', Unicode),
    Column('Assinatura', String(26, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('item_id', BigInteger),
    Column('orderdate', Float(53)),
    Column('Last_Update_Date', Unicode),
    Column('Days_Since_Last_Update', Numeric(24, 12)),
    Column('Ano', Unicode),
    Column('Mês_Número', Unicode),
    Column('Dia', Integer),
    Column('Hora', Integer),
    Column('Data', String(38, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Data_Date', Unicode),
    Column('Semana', Integer),
    Column('Dia Semana Número', Integer),
    Column('Dia Semana', String(7, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Quarter', Integer, nullable=False),
    Column('order_status', Unicode),
    Column('productid', BigInteger),
    Column('sku', Unicode),
    Column('quantidade', BigInteger),
    Column('preco_original', Float(53)),
    Column('preco_subtotal_diluido', Float(53)),
    Column('preco_desconto_diluido', Float(53)),
    Column('preco_frete_diluido', Float(53)),
    Column('preco_final', Float(53)),
    Column('preco_total_pago', Float(53)),
    Column('Cidade', Unicode),
    Column('Estado', Unicode),
    Column('cep', Float(53)),
    Column('applied_rule_ids', Unicode),
    Column('applied_rule_names', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('categoria', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('capsula', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tipo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Frete Grátis', Integer, nullable=False),
    Column('Desconto', Integer, nullable=False),
    Column('Bônus_Blisspoints', Integer, nullable=False),
    Column('Evento', Integer, nullable=False),
    Column('Relacionamento', Integer, nullable=False),
    Column('Promo Assinatura', Integer, nullable=False),
    Column('Ignorar', Integer, nullable=False),
    Column('Quantidade Dose', Float(53)),
    Column('Quantidade Cápsula', Float(53)),
    Column('Quantidade Caixa', Float(53)),
    Column('child_productid', Float(53)),
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('OptinOut', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Gênero', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Source', Unicode),
    Column('Canal', Unicode),
    Column('Campanha', Unicode),
    Column('POSSUI_DSJ', Integer, nullable=False),
    Column('POSSUI_CAIXA_NORMAL', Integer, nullable=False),
    Column('POSSUI_ACESSÓRIO', Integer, nullable=False),
    Column('POSSUI_MÁQUINA', Integer, nullable=False),
    Column('POSSUI_COMBO', Integer, nullable=False),
    Column('POSSUI_VOUCHER', Integer, nullable=False),
    Column('USOU_BLISSPOINTS', String(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('order_sequence', BigInteger),
    Column('order_sequence_desc', BigInteger),
    Column('Cápsulas', Float(53)),
    Column('previous_orderdate', Unicode),
    Column('previous_ordernumber', Unicode),
    Column('previous_Cápsulas', Float(53)),
    Column('delta_days', Numeric(24, 12)),
    Column('delta_Cápsulas', Float(53)),
    Column('Média_delta_days', Numeric(38, 12)),
    Column('Média_Cápsulas', Float(53)),
    Column('Total_days', Numeric(38, 12)),
    Column('Total_Cápsulas', Float(53)),
    Column('Consumo_de_Cápsulas/Dia_temp', Float(53)),
    Column('Cápsulas Consumidas', Float(53)),
    Column('Remaining_caps', Float(53)),
    Column('Remaining_days', Float(53)),
    Column('previous_Consumo_de_Cápsulas/Dia', Float(53)),
    Column('delta_Consumo_de_Cápsulas/Dia', Float(53)),
    Column('Fim_das_Cápsulas', Date),
    Column('Dias_Remanescentes', Numeric(24, 12)),
    Column('Estoque Atual', Float(53)),
    Column('Consumo_de_Cápsulas/Dia', Float(53))
)


t_analysis_sales_previous_week_1 = Table(
    'analysis_sales_previous_week_1', metadata,
    Column('email', Unicode),
    Column('customerid', Unicode),
    Column('ordernumber', Unicode),
    Column('Assinatura', String(26, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('item_id', BigInteger),
    Column('orderdate', Float(53)),
    Column('Last_Update_Date', Unicode),
    Column('Days_Since_Last_Update', Numeric(24, 12)),
    Column('Ano', Unicode),
    Column('Mês_Número', Unicode),
    Column('Dia', Integer),
    Column('Hora', Integer),
    Column('Data', String(38, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Data_Date', Unicode),
    Column('Semana', Integer),
    Column('Dia Semana Número', Integer),
    Column('Dia Semana', String(7, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Quarter', Integer, nullable=False),
    Column('order_status', Unicode),
    Column('productid', BigInteger),
    Column('sku', Unicode),
    Column('quantidade', BigInteger),
    Column('preco_original', Float(53)),
    Column('preco_subtotal_diluido', Float(53)),
    Column('preco_desconto_diluido', Float(53)),
    Column('preco_frete_diluido', Float(53)),
    Column('preco_final', Float(53)),
    Column('preco_total_pago', Float(53)),
    Column('Cidade', Unicode),
    Column('Estado', Unicode),
    Column('cep', Float(53)),
    Column('applied_rule_ids', Unicode),
    Column('applied_rule_names', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('categoria', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('capsula', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tipo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Frete Grátis', Integer, nullable=False),
    Column('Desconto', Integer, nullable=False),
    Column('Bônus_Blisspoints', Integer, nullable=False),
    Column('Evento', Integer, nullable=False),
    Column('Relacionamento', Integer, nullable=False),
    Column('Promo Assinatura', Integer, nullable=False),
    Column('Ignorar', Integer, nullable=False),
    Column('Quantidade Dose', Float(53)),
    Column('Quantidade Cápsula', Float(53)),
    Column('Quantidade Caixa', Float(53)),
    Column('child_productid', Float(53)),
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('OptinOut', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Gênero', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Source', Unicode),
    Column('Canal', Unicode),
    Column('Campanha', Unicode),
    Column('POSSUI_DSJ', Integer, nullable=False),
    Column('POSSUI_CAIXA_NORMAL', Integer, nullable=False),
    Column('POSSUI_ACESSÓRIO', Integer, nullable=False),
    Column('POSSUI_MÁQUINA', Integer, nullable=False),
    Column('POSSUI_COMBO', Integer, nullable=False),
    Column('POSSUI_VOUCHER', Integer, nullable=False),
    Column('USOU_BLISSPOINTS', String(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('order_sequence', BigInteger),
    Column('order_sequence_desc', BigInteger),
    Column('Cápsulas', Float(53)),
    Column('previous_orderdate', Unicode),
    Column('previous_ordernumber', Unicode),
    Column('previous_Cápsulas', Float(53)),
    Column('delta_days', Numeric(24, 12)),
    Column('delta_Cápsulas', Float(53)),
    Column('Média_delta_days', Numeric(38, 12)),
    Column('Média_Cápsulas', Float(53)),
    Column('Total_days', Numeric(38, 12)),
    Column('Total_Cápsulas', Float(53)),
    Column('Consumo_de_Cápsulas/Dia_temp', Float(53)),
    Column('Cápsulas Consumidas', Float(53)),
    Column('Remaining_caps', Float(53)),
    Column('Remaining_days', Float(53)),
    Column('previous_Consumo_de_Cápsulas/Dia', Float(53)),
    Column('delta_Consumo_de_Cápsulas/Dia', Float(53)),
    Column('Fim_das_Cápsulas', Date),
    Column('Dias_Remanescentes', Numeric(24, 12)),
    Column('Estoque Atual', Float(53)),
    Column('Consumo_de_Cápsulas/Dia', Float(53))
)


t_analysis_sales_previous_week_2 = Table(
    'analysis_sales_previous_week_2', metadata,
    Column('email', Unicode),
    Column('customerid', Unicode),
    Column('ordernumber', Unicode),
    Column('Assinatura', String(26, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('item_id', BigInteger),
    Column('orderdate', Float(53)),
    Column('Last_Update_Date', Unicode),
    Column('Days_Since_Last_Update', Numeric(24, 12)),
    Column('Ano', Unicode),
    Column('Mês_Número', Unicode),
    Column('Dia', Integer),
    Column('Hora', Integer),
    Column('Data', String(38, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Data_Date', Unicode),
    Column('Semana', Integer),
    Column('Dia Semana Número', Integer),
    Column('Dia Semana', String(7, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Quarter', Integer, nullable=False),
    Column('order_status', Unicode),
    Column('productid', BigInteger),
    Column('sku', Unicode),
    Column('quantidade', BigInteger),
    Column('preco_original', Float(53)),
    Column('preco_subtotal_diluido', Float(53)),
    Column('preco_desconto_diluido', Float(53)),
    Column('preco_frete_diluido', Float(53)),
    Column('preco_final', Float(53)),
    Column('preco_total_pago', Float(53)),
    Column('Cidade', Unicode),
    Column('Estado', Unicode),
    Column('cep', Float(53)),
    Column('applied_rule_ids', Unicode),
    Column('applied_rule_names', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('categoria', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('capsula', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tipo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Frete Grátis', Integer, nullable=False),
    Column('Desconto', Integer, nullable=False),
    Column('Bônus_Blisspoints', Integer, nullable=False),
    Column('Evento', Integer, nullable=False),
    Column('Relacionamento', Integer, nullable=False),
    Column('Promo Assinatura', Integer, nullable=False),
    Column('Ignorar', Integer, nullable=False),
    Column('Quantidade Dose', Float(53)),
    Column('Quantidade Cápsula', Float(53)),
    Column('Quantidade Caixa', Float(53)),
    Column('child_productid', Float(53)),
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('OptinOut', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Gênero', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Source', Unicode),
    Column('Canal', Unicode),
    Column('Campanha', Unicode),
    Column('POSSUI_DSJ', Integer, nullable=False),
    Column('POSSUI_CAIXA_NORMAL', Integer, nullable=False),
    Column('POSSUI_ACESSÓRIO', Integer, nullable=False),
    Column('POSSUI_MÁQUINA', Integer, nullable=False),
    Column('POSSUI_COMBO', Integer, nullable=False),
    Column('POSSUI_VOUCHER', Integer, nullable=False),
    Column('USOU_BLISSPOINTS', String(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('order_sequence', BigInteger),
    Column('order_sequence_desc', BigInteger),
    Column('Cápsulas', Float(53)),
    Column('previous_orderdate', Unicode),
    Column('previous_ordernumber', Unicode),
    Column('previous_Cápsulas', Float(53)),
    Column('delta_days', Numeric(24, 12)),
    Column('delta_Cápsulas', Float(53)),
    Column('Média_delta_days', Numeric(38, 12)),
    Column('Média_Cápsulas', Float(53)),
    Column('Total_days', Numeric(38, 12)),
    Column('Total_Cápsulas', Float(53)),
    Column('Consumo_de_Cápsulas/Dia_temp', Float(53)),
    Column('Cápsulas Consumidas', Float(53)),
    Column('Remaining_caps', Float(53)),
    Column('Remaining_days', Float(53)),
    Column('previous_Consumo_de_Cápsulas/Dia', Float(53)),
    Column('delta_Consumo_de_Cápsulas/Dia', Float(53)),
    Column('Fim_das_Cápsulas', Date),
    Column('Dias_Remanescentes', Numeric(24, 12)),
    Column('Estoque Atual', Float(53)),
    Column('Consumo_de_Cápsulas/Dia', Float(53))
)


t_association_capsulas = Table(
    'association_capsulas', metadata,
    Column('from', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Espresso', Numeric(26, 12)),
    Column('Espresso Intenso', Numeric(26, 12)),
    Column('Espresso Barista', Numeric(26, 12)),
    Column('Ristretto', Numeric(26, 12)),
    Column('Ristretto Ardenza', Numeric(26, 12)),
    Column('Espresso Decaffeinato', Numeric(26, 12)),
    Column('Caffè Matinal', Numeric(26, 12)),
    Column('Café Caseiro', Numeric(26, 12)),
    Column('Café Caseiro Intenso', Numeric(26, 12)),
    Column('Lungo', Numeric(26, 12)),
    Column('Café Au Lait', Numeric(26, 12)),
    Column('Café Au Lait com Leite Desnatado', Numeric(26, 12)),
    Column('Cortado', Numeric(26, 12)),
    Column('Cappuccino', Numeric(26, 12)),
    Column('Latte Macchiato', Numeric(26, 12)),
    Column('Caramel Latte Macchiato', Numeric(26, 12)),
    Column('Vanilla Latte Macchiato', Numeric(26, 12)),
    Column('Mochaccino Canela', Numeric(26, 12)),
    Column('Mocha', Numeric(26, 12)),
    Column('Nescau', Numeric(26, 12)),
    Column('Chococino', Numeric(26, 12)),
    Column('Chococino Caramel', Numeric(26, 12)),
    Column('Marrakesh Style Tea', Numeric(26, 12)),
    Column('Chai Tea Latte', Numeric(26, 12)),
    Column('Nestea® Limão', Numeric(26, 12)),
    Column('Nestea® Pêssego', Numeric(26, 12)),
    Column('Starbucks Americano House Blend - 12 Cápsulas', Numeric(26, 12)),
    Column('Starbucks Blonde Espresso Roast - 12 Cápsulas', Numeric(26, 12)),
    Column('Starbucks Espresso Roast - 12 Cápsulas', Numeric(26, 12)),
    Column('Starbucks Cappuccino - 12 Cápsulas', Numeric(26, 12)),
    Column('Starbucks Latte Macchiato - 12 Cápsulas', Numeric(26, 12)),
    Column('STARBUCKS CARAMEL MACCHIATO - 12 CÁPSULAS', Numeric(26, 12))
)


t_azia_trends_rising = Table(
    'azia_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_azia_trends_top = Table(
    'azia_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_café_trends_rising = Table(
    'café_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger)
)


t_café_trends_top = Table(
    'café_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger)
)


t_capsulas_trends_rising = Table(
    'capsulas_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger)
)


t_capsulas_trends_top = Table(
    'capsulas_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger)
)


t_cerveja_trends_rising = Table(
    'cerveja_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_cerveja_trends_top = Table(
    'cerveja_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_dashboard_executivo_days = Table(
    'dashboard_executivo_days', metadata,
    Column('last_day', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('first_day', String(2, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('current_day', Unicode)
)


t_dashboard_executivo_metas = Table(
    'dashboard_executivo_metas', metadata,
    Column('Compras_Realizadas', Integer),
    Column('Valor_Real', Float(53)),
    Column('Compras_Esperadas', Integer),
    Column('Valor_Esperado', Float(53))
)


t_dashboard_executivo_previsao_cliente = Table(
    'dashboard_executivo_previsao_cliente', metadata,
    Column('email', Unicode),
    Column('Próxima_Compra', Date),
    Column('Ticket_Médio', Float(53))
)


t_dashboard_executivo_rule_names_by_orders = Table(
    'dashboard_executivo_rule_names_by_orders', metadata,
    Column('Data_Date', Unicode),
    Column('ordernumber', Unicode),
    Column('DATA_ID', Unicode)
)


t_dashboard_executivo_ticket_medio = Table(
    'dashboard_executivo_ticket_medio', metadata,
    Column('Dimensão', String(29, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Ano_Anterior', Float(53)),
    Column('Ano_Atual', Float(53))
)


t_dashboard_executivo_top_10_rules = Table(
    'dashboard_executivo_top_10_rules', metadata,
    Column('Regra', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('contagem', Integer)
)


t_dashboard_executivo_valores_esperados = Table(
    'dashboard_executivo_valores_esperados', metadata,
    Column('Compras_Esperadas', Integer),
    Column('Valor_Esperado', Float(53))
)


t_dashboard_historico_executivo_consumidores_com_blisspoint = Table(
    'dashboard_historico_executivo_consumidores_com_blisspoint', metadata,
    Column('Consumidores_com_Blisspoint', Integer)
)


t_dashboard_historico_executivo_consumidores_com_máquina = Table(
    'dashboard_historico_executivo_consumidores_com_máquina', metadata,
    Column('Consumidores_com_Máquina', Integer)
)


t_dashboard_historico_executivo_consumidores_máquina_2019_e_antes = Table(
    'dashboard_historico_executivo_consumidores_máquina_2019_e_antes', metadata,
    Column('Consumidores_Máquina_2019_e_antes', Integer)
)


t_dashboard_historico_executivo_consumidores_year_over_year = Table(
    'dashboard_historico_executivo_consumidores_year_over_year', metadata,
    Column('Dimensão', String(30, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Consumidores_2018', Integer),
    Column('Consumidores_2019', Integer),
    Column('Var_abs', Integer),
    Column('Var_%', Numeric(24, 12))
)


t_digital_transformation = Table(
    'digital_transformation', metadata,
    Column('Ano', BigInteger),
    Column('UF', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Empresa', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Produto', BigInteger),
    Column('Cod Barras', BigInteger),
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Divisão', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Seção', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Grupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Subgrupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Marca', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Quantidade', Float(53)),
    Column('Valor', Float(53))
)


t_digital_transformation_bebidas_liquidas = Table(
    'digital_transformation_bebidas_liquidas', metadata,
    Column('Ano', BigInteger),
    Column('UF', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês_Número', Integer),
    Column('Empresa', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Produto', BigInteger),
    Column('Cod Barras', BigInteger),
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Divisão', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Seção', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Grupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Subgrupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Marca', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Quantidade', Float(53)),
    Column('Valor', Float(53))
)


t_digital_transformation_bebidas_liquidas_comparacao = Table(
    'digital_transformation_bebidas_liquidas_comparacao', metadata,
    Column('Ano', BigInteger),
    Column('Mês_Número', Integer),
    Column('Qtd_Liquido', Float(53)),
    Column('Qtd_Roots_to_Go', Float(53))
)


t_digital_transformation_health_science = Table(
    'digital_transformation_health_science', metadata,
    Column('Ano', BigInteger),
    Column('UF', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês_Número', Integer),
    Column('Empresa', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Produto', BigInteger),
    Column('Cod Barras', BigInteger),
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Divisão', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Seção', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Grupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Subgrupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Marca', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Quantidade', Float(53)),
    Column('Valor', Float(53))
)


t_digital_transformation_health_science_comparacao = Table(
    'digital_transformation_health_science_comparacao', metadata,
    Column('Ano', BigInteger),
    Column('Mês_Número', Integer),
    Column('Qtd_NHS', Float(53)),
    Column('Qtd_Mu', Float(53))
)


t_digital_transformation_lojas_sp = Table(
    'digital_transformation_lojas_sp', metadata,
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Cenario', String(9, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vendas', Float(53))
)


t_digital_transformation_salgados = Table(
    'digital_transformation_salgados', metadata,
    Column('Ano', BigInteger),
    Column('UF', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês_Número', Integer),
    Column('Empresa', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Produto', BigInteger),
    Column('Cod Barras', BigInteger),
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Divisão', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Seção', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Grupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Subgrupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Marca', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Quantidade', Float(53)),
    Column('Valor', Float(53))
)


t_digital_transformation_salgados_comparacao = Table(
    'digital_transformation_salgados_comparacao', metadata,
    Column('Ano', BigInteger),
    Column('Mês_Número', Integer),
    Column('Qtd_Nesfit', Float(53)),
    Column('Qtd_Roots_to_Go', Float(53))
)


t_digital_transformation_start_ups = Table(
    'digital_transformation_start_ups', metadata,
    Column('Ano', BigInteger),
    Column('UF', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês_Número', Integer),
    Column('Empresa', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Produto', BigInteger),
    Column('Cod Barras', BigInteger),
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Divisão', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Seção', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Grupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Subgrupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Marca', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Quantidade', Float(53)),
    Column('Valor', Float(53))
)


t_digital_transformation_start_ups_temp = Table(
    'digital_transformation_start_ups_temp', metadata,
    Column('Ano', BigInteger),
    Column('UF', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Empresa', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Produto', BigInteger),
    Column('Cod Barras', BigInteger),
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Divisão', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Seção', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Grupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Subgrupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Marca', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Quantidade', Float(53)),
    Column('Valor', Float(53))
)


t_digital_transformation_start_ups_top_3_qtd = Table(
    'digital_transformation_start_ups_top_3_qtd', metadata,
    Column('Ano', BigInteger),
    Column('Mês_Número', Integer),
    Column('Divisão', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Quantidade', Float(53)),
    Column('Rank_qtd', BigInteger)
)


t_doces_trends_rising = Table(
    'doces_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_doces_trends_top = Table(
    'doces_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_eno_trends_rising = Table(
    'eno_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_eno_trends_top = Table(
    'eno_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_au_lait_desnatado = Table(
    'fluxo_compras_novos_sabores_au_lait_desnatado', metadata,
    Column('email', Unicode),
    Column('Última_Compra', String(9, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Penúltima_Compra', String(15, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_caseiro = Table(
    'fluxo_compras_novos_sabores_caseiro', metadata,
    Column('Faixas', String(9, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('email', Unicode)
)


t_fluxo_compras_novos_sabores_caseiro_temp = Table(
    'fluxo_compras_novos_sabores_caseiro_temp', metadata,
    Column('email', Unicode),
    Column('Última_Compra', String(7, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Penúltima_Compra', String(15, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_0 = Table(
    'fluxo_compras_novos_sabores_letter_0', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_1 = Table(
    'fluxo_compras_novos_sabores_letter_1', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_2 = Table(
    'fluxo_compras_novos_sabores_letter_2', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_3 = Table(
    'fluxo_compras_novos_sabores_letter_3', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_4 = Table(
    'fluxo_compras_novos_sabores_letter_4', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_5 = Table(
    'fluxo_compras_novos_sabores_letter_5', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_6 = Table(
    'fluxo_compras_novos_sabores_letter_6', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_7 = Table(
    'fluxo_compras_novos_sabores_letter_7', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_8 = Table(
    'fluxo_compras_novos_sabores_letter_8', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_9 = Table(
    'fluxo_compras_novos_sabores_letter_9', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter__ = Table(
    'fluxo_compras_novos_sabores_letter__', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_a = Table(
    'fluxo_compras_novos_sabores_letter_a', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_b = Table(
    'fluxo_compras_novos_sabores_letter_b', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_c = Table(
    'fluxo_compras_novos_sabores_letter_c', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_d = Table(
    'fluxo_compras_novos_sabores_letter_d', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_e = Table(
    'fluxo_compras_novos_sabores_letter_e', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_f = Table(
    'fluxo_compras_novos_sabores_letter_f', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_g = Table(
    'fluxo_compras_novos_sabores_letter_g', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_h = Table(
    'fluxo_compras_novos_sabores_letter_h', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_i = Table(
    'fluxo_compras_novos_sabores_letter_i', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_j = Table(
    'fluxo_compras_novos_sabores_letter_j', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_k = Table(
    'fluxo_compras_novos_sabores_letter_k', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_l = Table(
    'fluxo_compras_novos_sabores_letter_l', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_n = Table(
    'fluxo_compras_novos_sabores_letter_n', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_o = Table(
    'fluxo_compras_novos_sabores_letter_o', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_p = Table(
    'fluxo_compras_novos_sabores_letter_p', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_q = Table(
    'fluxo_compras_novos_sabores_letter_q', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_r = Table(
    'fluxo_compras_novos_sabores_letter_r', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_s = Table(
    'fluxo_compras_novos_sabores_letter_s', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_t = Table(
    'fluxo_compras_novos_sabores_letter_t', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_u = Table(
    'fluxo_compras_novos_sabores_letter_u', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_v = Table(
    'fluxo_compras_novos_sabores_letter_v', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_w = Table(
    'fluxo_compras_novos_sabores_letter_w', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_x = Table(
    'fluxo_compras_novos_sabores_letter_x', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_y = Table(
    'fluxo_compras_novos_sabores_letter_y', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_letter_z = Table(
    'fluxo_compras_novos_sabores_letter_z', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_novos_sabores_temp = Table(
    'fluxo_compras_novos_sabores_temp', metadata,
    Column('email', Unicode),
    Column('Última_compra', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Penúltima_compra', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_compras_starbucks_temp = Table(
    'fluxo_compras_starbucks_temp', metadata,
    Column('email', Unicode),
    Column('order_sequence', BigInteger),
    Column('categoria', String(9, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Cápsulas', Float(53))
)


t_fluxo_compras_starbucks_temp_2 = Table(
    'fluxo_compras_starbucks_temp_2', metadata,
    Column('email', Unicode),
    Column('order_sequence', BigInteger),
    Column('categoria', String(9, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Cápsulas', Float(53)),
    Column('Cápsulas_anteriores', Float(53)),
    Column('Diferença', Float(53))
)


t_fluxo_variacao_novos_sabores_caseiro = Table(
    'fluxo_variacao_novos_sabores_caseiro', metadata,
    Column('email', Unicode),
    Column('Última_Compra', String(7, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Penúltima_Compra', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Faixas', String(9, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_fluxo_variacao_novos_sabores_desnatado = Table(
    'fluxo_variacao_novos_sabores_desnatado', metadata,
    Column('email', Unicode),
    Column('Última_Compra', String(9, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Penúltima_Compra', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Faixas', String(9, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_frango_trends_rising = Table(
    'frango_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_frango_trends_top = Table(
    'frango_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_ga_campaigns_bulk = Table(
    'ga_campaigns_bulk', metadata,
    Column('Campanha', Unicode),
    Column('ordernumber', Unicode)
)


t_ga_channels_bulk = Table(
    'ga_channels_bulk', metadata,
    Column('Canal', Unicode),
    Column('ordernumber', Unicode)
)


t_ga_orders_info = Table(
    'ga_orders_info', metadata,
    Column('ordernumber', Unicode),
    Column('Source', Unicode),
    Column('Canal', Unicode),
    Column('Campanha', Unicode)
)


t_ga_source_bulk = Table(
    'ga_source_bulk', metadata,
    Column('Source', Unicode),
    Column('ordernumber', Unicode)
)


t_hist_rfv_total_segments = Table(
    'hist_rfv_total_segments', metadata,
    Column('Semana', String(25, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Segment', String(11, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Clientes_Semana_Atual', Integer),
    Column('Clientes_Semana_Anterior', Integer)
)


t_hist_rfv_total_segments_temp = Table(
    'hist_rfv_total_segments_temp', metadata,
    Column('Semana', String(25, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Segment', String(11, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Clientes_Semana_Atual', Integer)
)


t_histograma_quantidade_novos_sabores_caseiro = Table(
    'histograma_quantidade_novos_sabores_caseiro', metadata,
    Column('Faixas', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('email', Unicode)
)


t_loteria_trends_rising = Table(
    'loteria_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_loteria_trends_top = Table(
    'loteria_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_manual_ces_bulk = Table(
    'manual_ces_bulk', metadata,
    Column('Data_Date', DateTime),
    Column('Código do Chamado', Unicode),
    Column('Nome da Pessoa', Unicode),
    Column('email', Unicode),
    Column('Cidade', Unicode),
    Column('UF', Unicode),
    Column('Manifestação', Unicode),
    Column('Linha de Produto', Unicode),
    Column('Assunto', Unicode),
    Column('Variedade', Unicode),
    Column('Nível 1', Unicode),
    Column('Nível 2', Unicode),
    Column('Nível 3', Unicode),
    Column('Nível 4', Unicode),
    Column('Palavra Chave Manifestação', Unicode),
    Column('Forma de Contato', Unicode),
    Column('Marketing', Unicode),
    Column('Qualificação do Contato', Unicode)
)


t_manual_eloqua_bulk_temp = Table(
    'manual_eloqua_bulk_temp', metadata,
    Column('ContactID', Unicode),
    Column('Email Address', Unicode),
    Column('MarketId', Unicode),
    Column('Newsletter', Unicode),
    Column('Salutation', Unicode),
    Column('First Name', Unicode),
    Column('Last Name', Unicode),
    Column('Address 1', Unicode),
    Column('Address 2', Unicode),
    Column('Zip or Postal Code', Unicode),
    Column('City', Unicode),
    Column('Country', Unicode),
    Column('Language', Unicode),
    Column('Gender', Unicode),
    Column('Mobile Phone', Unicode),
    Column('Birthday', Unicode),
    Column('ConsumerId', Unicode),
    Column('LastOrderDate', Unicode),
    Column('Registration Date', Unicode),
    Column('DWH Updated Date', Unicode),
    Column('Date Created', Unicode),
    Column('Date Modified', Unicode),
    Column('LastLogin', Unicode),
    Column('OwnsMachine', Unicode),
    Column('LastBasketAmount', Unicode),
    Column('MachineModelRegisteredWithCode', Unicode),
    Column('MachineLastOnlinePurchaseDate', Unicode),
    Column('MachineRegisteredDateWithCode', Unicode),
    Column('Permission Source', Unicode),
    Column('Permission Medium', Unicode),
    Column('Permission Date', Unicode),
    Column('Promo Code 1', Unicode),
    Column('Promo Code 2', Unicode),
    Column('Promo Code 3', Unicode),
    Column('Promo Code 4', Unicode),
    Column('Promo Code 5', Unicode),
    Column('Promo Code 6', Unicode),
    Column('Promo Code 7', Unicode),
    Column('Participant Welcome Program', Unicode),
    Column('Eloqua Contact ID', Unicode),
    Column('LoyaltyPoints', Unicode),
    Column('LoyaltyPointsToExpire', Unicode),
    Column('LastOfferRedeemed', Unicode),
    Column('TotalTurnover_All_Local', Unicode),
    Column('NumberOfOrders_All', Unicode),
    Column('FirstMachineRegistered', Unicode),
    Column('MachineModelRegisteredNoCode', Unicode),
    Column('MachineRegisteredPurchaseDateNoCode', Unicode),
    Column('MachineRegisteredDateNoCode', Unicode),
    Column('MachineRegisteredCode', Unicode),
    Column('MachineRegisteredPurchaseDateWithCode', Unicode),
    Column('MachineModelPurchasedOnline', Unicode),
    Column('MachineFirstOnlinePurchaseDate', Unicode),
    Column('OwnsMachinePurchasedOnline', Unicode),
    Column('NumberOfOrderedMachines_All', Unicode)
)


t_manual_enderecos_bulk = Table(
    'manual_enderecos_bulk', metadata,
    Column('Endereço', Unicode),
    Column('Bairro', Unicode),
    Column('Cidade', Unicode),
    Column('Estado', Unicode),
    Column('cep', Unicode),
    Column('Latitude', Unicode),
    Column('Longitude', Unicode)
)


t_manual_flavours_order = Table(
    'manual_flavours_order', metadata,
    Column('capsula', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('order', BigInteger)
)


t_manual_productids = Table(
    'manual_productids', metadata,
    Column('categoria', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('capsula', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('productid', BigInteger),
    Column('tipo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('multiplicador_dose', Float(53)),
    Column('multiplicador_capsula', Float(53)),
    Column('multiplicador_caixa', Float(53)),
    Column('child_productid', Float(53)),
    Column('sku_GA', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('produto_GA', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_manual_promoids = Table(
    'manual_promoids', metadata,
    Column('Name', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tipo_promo', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_manual_rule_ids = Table(
    'manual_rule_ids', metadata,
    Column('applied_rule_ids', BigInteger),
    Column('tipo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Nome', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_manual_rule_ids_concat = Table(
    'manual_rule_ids_concat', metadata,
    Column('tipo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('rules', Unicode),
    Column('query', Unicode)
)


t_manual_segments_rfv = Table(
    'manual_segments_rfv', metadata,
    Column('Segment', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Segmentos', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Estratégia', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_manual_weather_bulk = Table(
    'manual_weather_bulk', metadata,
    Column('Estacao', Unicode),
    Column('Data', Unicode),
    Column('Data_Date', Unicode),
    Column('Hora', Unicode),
    Column('Precipitacao', Unicode),
    Column('TempBulboSeco', Unicode),
    Column('TempBulboUmido', Unicode),
    Column('TempMaxima', Unicode),
    Column('TempMinima', Unicode),
    Column('UmidadeRelativa', Unicode),
    Column('PressaoAtmEstacao', Unicode),
    Column('PressaoAtmMar', Unicode),
    Column('DirecaoVento', Unicode),
    Column('VelocidadeVento', Unicode),
    Column('Insolacao', Unicode),
    Column('Nebulosidade', Unicode),
    Column('Evaporacao Piche', Unicode),
    Column('Temp Comp Media', Unicode),
    Column('Umidade Relativa Media', Unicode),
    Column('Velocidade do Vento Media', Unicode)
)


t_manual_weather_stations_bulk_temp = Table(
    'manual_weather_stations_bulk_temp', metadata,
    Column('Nome', Unicode),
    Column('Código', Unicode),
    Column('Latitude', Unicode),
    Column('Longitude', Unicode),
    Column('Altitude', Unicode),
    Column('Status da Operação', Unicode),
    Column('Ínicio da Operação', Unicode)
)


t_mg_blisspoints_report_bulk = Table(
    'mg_blisspoints_report_bulk', metadata,
    Column('CustomerID', Unicode),
    Column('Balance', Unicode),
    Column('Points', BigInteger),
    Column('Reason', Unicode),
    Column('CreatedAt', Unicode),
    Column('ExpiredAt', Unicode),
    Column('Comment', Unicode),
    Column('ordernumber', Unicode),
    Column('coupon', Unicode),
    Column('Update Date', Unicode)
)


t_mg_current_email = Table(
    'mg_current_email', metadata,
    Column('customer_id', Unicode),
    Column('customer_email', Unicode)
)


t_mg_email_optinout_bulk = Table(
    'mg_email_optinout_bulk', metadata,
    Column('CustomerID', Unicode),
    Column('FirstName', Unicode),
    Column('LastName', Unicode),
    Column('CustomerEmail', Unicode),
    Column('Status', Unicode),
    Column('UpdateDate', Unicode),
    Column('optinout', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('update_sequence', BigInteger),
    Column('status_sequence', BigInteger)
)


t_mg_first_name_predicted_gender = Table(
    'mg_first_name_predicted_gender', metadata,
    Column('firstname', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('gender', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_mg_first_name_predicted_gender_pygenderbr = Table(
    'mg_first_name_predicted_gender_pygenderbr', metadata,
    Column('name', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('gender', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_mg_new_product_ids = Table(
    'mg_new_product_ids', metadata,
    Column('product_id', Unicode),
    Column('sku', Unicode)
)


t_mg_orders_dbm_bulk = Table(
    'mg_orders_dbm_bulk', metadata,
    Column('customer_id', Unicode),
    Column('customer_email', Unicode),
    Column('customer_fiscalcode', Unicode),
    Column('increment_id', Unicode),
    Column('created_at', Unicode),
    Column('status', Unicode),
    Column('item_id', Unicode),
    Column('product_id', Unicode),
    Column('sku', Unicode),
    Column('qty_ordered', Unicode),
    Column('Orginal_Price', Unicode),
    Column('subtotal', Unicode),
    Column('base_discount_amount', Unicode),
    Column('base_grand_total', Unicode),
    Column('base_total_paid', Unicode),
    Column('method', Unicode),
    Column('base_shipping_amount', Unicode),
    Column('Deliveryaddress', Unicode),
    Column('city', Unicode),
    Column('region', Unicode),
    Column('postcode', Unicode),
    Column('applied_rule_ids', Unicode),
    Column('updated_at', Unicode),
    Column('status_sequence', BigInteger),
    Column('customer_sequence', BigInteger)
)


t_mg_promotionid_report_bulk = Table(
    'mg_promotionid_report_bulk', metadata,
    Column('RuleID', BigInteger),
    Column('CustomerGroups', Unicode),
    Column('Name', Unicode),
    Column('Status', Unicode),
    Column('FromDate', Unicode),
    Column('ToDate', Unicode)
)


t_mg_rule_names = Table(
    'mg_rule_names', metadata,
    Column('applied_rule_ids', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('applied_rule_names', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_mg_subscriptions_weekly_report_bulk = Table(
    'mg_subscriptions_weekly_report_bulk', metadata,
    Column('Status', Unicode),
    Column('Subscriber_sexo', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('email', Unicode),
    Column('dob', Unicode),
    Column('Mobile', Unicode)
)


t_ml_train_previsao_ordens = Table(
    'ml_train_previsao_ordens', metadata,
    Column('Ano', Unicode),
    Column('Quarter', Integer, nullable=False),
    Column('Mês_Número', Unicode),
    Column('Data_Date', Unicode),
    Column('Semana', Integer),
    Column('Dia Semana Número', Integer),
    Column('Dia', Integer),
    Column('DSJ_EXCLUSIVO', Integer, nullable=False),
    Column('MISTO', Integer, nullable=False),
    Column('SEM_DSJ', Integer, nullable=False),
    Column('Ordens', Integer)
)


t_orders_complete = Table(
    'orders_complete', metadata,
    Column('email', Unicode),
    Column('customerid', Unicode),
    Column('ordernumber', Unicode),
    Column('Assinatura', String(26, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('item_id', BigInteger),
    Column('orderdate', Float(53)),
    Column('Last_Update_Date', Unicode),
    Column('Days_Since_Last_Update', Numeric(24, 12)),
    Column('Ano', Unicode),
    Column('Mês_Número', Unicode),
    Column('Dia', Integer),
    Column('Hora', Integer),
    Column('Data', String(38, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Data_Date', Unicode),
    Column('Semana', Integer),
    Column('Dia Semana Número', Integer),
    Column('Dia Semana', String(7, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Quarter', Integer, nullable=False),
    Column('order_status', Unicode),
    Column('productid', BigInteger),
    Column('sku', Unicode),
    Column('quantidade', BigInteger),
    Column('preco_original', Float(53)),
    Column('preco_subtotal_diluido', Float(53)),
    Column('preco_desconto_diluido', Float(53)),
    Column('preco_frete_diluido', Float(53)),
    Column('preco_final', Float(53)),
    Column('preco_total_pago', Float(53)),
    Column('Cidade', Unicode),
    Column('Estado', Unicode),
    Column('cep', Float(53)),
    Column('applied_rule_ids', Unicode),
    Column('applied_rule_names', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('categoria', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('capsula', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tipo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Frete Grátis', Integer, nullable=False),
    Column('Desconto', Integer, nullable=False),
    Column('Bônus_Blisspoints', Integer, nullable=False),
    Column('Evento', Integer, nullable=False),
    Column('Relacionamento', Integer, nullable=False),
    Column('Promo Assinatura', Integer, nullable=False),
    Column('Ignorar', Integer, nullable=False),
    Column('Quantidade Dose', Float(53)),
    Column('Quantidade Cápsula', Float(53)),
    Column('Quantidade Caixa', Float(53)),
    Column('child_productid', Float(53)),
    Column('Produto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('OptinOut', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Gênero', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Source', Unicode),
    Column('Canal', Unicode),
    Column('Campanha', Unicode),
    Column('POSSUI_DSJ', Integer, nullable=False),
    Column('POSSUI_CAIXA_NORMAL', Integer, nullable=False),
    Column('POSSUI_ACESSÓRIO', Integer, nullable=False),
    Column('POSSUI_MÁQUINA', Integer, nullable=False),
    Column('POSSUI_COMBO', Integer, nullable=False),
    Column('POSSUI_VOUCHER', Integer, nullable=False),
    Column('USOU_BLISSPOINTS', String(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('order_sequence', BigInteger),
    Column('order_sequence_desc', BigInteger)
)


t_ração_trends_rising = Table(
    'ração_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_ração_trends_top = Table(
    'ração_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_receitas_de_doces_trends_rising = Table(
    'receitas_de_doces_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_receitas_de_doces_trends_top = Table(
    'receitas_de_doces_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_receitas_trends_rising = Table(
    'receitas_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger)
)


t_receitas_trends_top = Table(
    'receitas_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_refluxo_trends_rising = Table(
    'refluxo_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_refluxo_trends_top = Table(
    'refluxo_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_rfv_current_week_segments = Table(
    'rfv_current_week_segments', metadata,
    Column('email', Unicode),
    Column('Segment', String(11, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_rfv_previous_week_1_segments = Table(
    'rfv_previous_week_1_segments', metadata,
    Column('email', Unicode),
    Column('Segment', String(11, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_rfv_previous_week_2_segments = Table(
    'rfv_previous_week_2_segments', metadata,
    Column('email', Unicode),
    Column('Segment', String(11, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_rfv_total_previous_week_1 = Table(
    'rfv_total_previous_week_1', metadata,
    Column('email', Unicode),
    Column('OptinOut', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Consumo de Cápsulas', Float(53)),
    Column('Recency', Integer),
    Column('Faixa_Recency', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Frequency', Integer),
    Column('Faixa_Frequency', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Value', Float(53)),
    Column('Faixa_Value', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Score', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Segment', String(11, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_rfv_total_previous_week_1_labels = Table(
    'rfv_total_previous_week_1_labels', metadata,
    Column('Faixa', BigInteger),
    Column('Recencia_De_Dias', BigInteger),
    Column('Recência_Até_Dias', BigInteger),
    Column('Frequência_De_Compras', BigInteger),
    Column('Frequência_Até_Compras', BigInteger),
    Column('Valor_De_Cáps', BigInteger),
    Column('Valor_Até_Cáps', BigInteger)
)


t_rfv_total_previous_week_2 = Table(
    'rfv_total_previous_week_2', metadata,
    Column('email', Unicode),
    Column('OptinOut', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Consumo de Cápsulas', Float(53)),
    Column('Recency', Integer),
    Column('Faixa_Recency', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Frequency', Integer),
    Column('Faixa_Frequency', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Value', Float(53)),
    Column('Faixa_Value', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Score', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Segment', String(11, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_rfv_total_previous_week_2_labels = Table(
    'rfv_total_previous_week_2_labels', metadata,
    Column('Faixa', BigInteger),
    Column('Recencia_De_Dias', BigInteger),
    Column('Recência_Até_Dias', BigInteger),
    Column('Frequência_De_Compras', BigInteger),
    Column('Frequência_Até_Compras', BigInteger),
    Column('Valor_De_Cáps', BigInteger),
    Column('Valor_Até_Cáps', BigInteger)
)


t_segment_week_evolution = Table(
    'segment_week_evolution', metadata,
    Column('email', Unicode),
    Column('Segmento_0', String(11, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Segmento_1', String(11, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Segmento_2', String(11, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_skol_trends_rising = Table(
    'skol_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_skol_trends_top = Table(
    'skol_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_sopas_trends_rising = Table(
    'sopas_trends_rising', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', BigInteger),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_sopas_trends_top = Table(
    'sopas_trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(12, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Ordem', BigInteger),
    Column('Palavra-Chave', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_start_ups = Table(
    'start_ups', metadata,
    Column('Ano', BigInteger),
    Column('UF', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês_Número', Integer),
    Column('Empresa', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Produto', BigInteger),
    Column('Cod Barras', BigInteger),
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Divisão', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Seção', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Grupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Subgrupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Marca', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Quantidade', Float(53)),
    Column('Valor', Float(53))
)


t_start_ups_temp = Table(
    'start_ups_temp', metadata,
    Column('Ano', BigInteger),
    Column('UF', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Mês', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Empresa', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Produto', BigInteger),
    Column('Cod Barras', BigInteger),
    Column('Descrição', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Divisão', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Seção', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Grupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Subgrupo', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Marca', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Quantidade', Float(53)),
    Column('Valor', Float(53))
)


t_total_email_capsulas = Table(
    'total_email_capsulas', metadata,
    Column('capsula', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('compradores', Integer)
)


t_trends_top = Table(
    'trends_top', metadata,
    Column('assunto', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('tendência', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Estado', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Região', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('Período', String(collation='SQL_Latin1_General_CP1_CI_AS'))
)


t_variacao_quantidade_novos_sabores_caseiro = Table(
    'variacao_quantidade_novos_sabores_caseiro', metadata,
    Column('email', Unicode),
    Column('Variação_Quantidade', Float(53))
)
