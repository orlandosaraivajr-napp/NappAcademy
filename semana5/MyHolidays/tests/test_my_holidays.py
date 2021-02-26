from MyHolidays.myholidays.holidays import MyCalendar
from datetime import date
import pytest


class TestMyCalendar:
    def test_class_declared(self):
        """
        Testar se a classe está declarada
        """
        objeto = MyCalendar()
        assert isinstance(objeto, MyCalendar)

    def test_inner_list_declared(self):
        """
        Testar se o objeto possui uma lista interna chamada datas
        """
        objeto = MyCalendar()
        assert isinstance(objeto.datas, list)

    datas = [
        (date(2021, 12, 5), date(2021, 4, 21), 2),
        ('25/12/2021', date(2021, 4, 21), 2),
        ('25/12/2021', '07/09/2021', 2),
        (date(2021, 4, 21), '25/12/2021', 2),
        (date(2021, 4, 21), 15, 1),
        (20, date(2021, 4, 21), 1),
        ([1, 2, 3], date(2021, 4, 21), 1),
        ((1, 2, 3), date(2021, 4, 21), 1),
    ]

    @pytest.mark.parametrize("dt1, dt2, tamanho_lista", datas)
    def test_class_instanced_with(self, dt1, dt2, tamanho_lista):
        """
        Testar se o construtor recebe tanto objetos dates quanto
        strings no formato dd/MM/aaaa
        """
        objeto = MyCalendar(dt1, dt2)
        assert len(objeto.datas) == tamanho_lista
        assert isinstance(objeto.datas[0], date)

    def test_receive_bad_formatted_strings(self):
        """
        Testar se o objeto, ao ser instanciado recebe uma lista de strings
        no formato dd/MM/aaaa. Caso a string esteja mal formatada,
        o objeto deve ignorar a data.
        """
        dt1 = '15/2'
        dt2 = '25/12'
        dt3 = '15/2/2021'
        objeto = MyCalendar(dt1, dt2, dt3)
        assert len(objeto.datas) == 1
        assert isinstance(objeto.datas[0], date)

    def test_receive_bad_formatted_strings_2(self):
        """
        Testar se o objeto, ao ser instanciado recebe uma lista de strings
        no formato dd/MM/aaaa. Caso a string esteja mal formatada,
        o objeto deve ignorar a data.
        """
        dt1 = '15/15/2021'
        dt2 = '25/25/2021'
        dt3 = '15/12/2021'
        objeto = MyCalendar(dt1, dt2, dt3)
        assert len(objeto.datas) == 1
        assert isinstance(objeto.datas[0], date)

    def test_method_add_holiday_1(self):
        """
        Testar se método add_holiday consegue adicionar um novo feriado.
        """
        dt1 = '15/01/2021'
        dt2 = '15/02/2021'
        dt3 = '15/03/2021'
        objeto = MyCalendar(dt1, dt2)
        objeto.add_holiday(dt3)
        assert len(objeto.datas) == 3
        assert isinstance(objeto.datas[0], date)
        assert isinstance(objeto.datas[1], date)
        assert isinstance(objeto.datas[2], date)

    def test_method_add_holiday_2(self):
        """
        Testar se método add_holiday consegue adicionar mais de
        um novo feriado.
        """
        dt1 = '15/01/2021'
        dt2 = '15/02/2021'
        dt3 = '15/03/2021'
        dt4 = '15/04/2021'
        objeto = MyCalendar(dt1, dt2)
        objeto.add_holiday(dt3, dt4)
        assert len(objeto.datas) == 4
        assert isinstance(objeto.datas[0], date)
        assert isinstance(objeto.datas[1], date)
        assert isinstance(objeto.datas[2], date)
        assert isinstance(objeto.datas[3], date)

    def test_method_add_holiday_3(self):
        """
        Testar se método add_holiday consegue adicionar mais de
        um novo feriado.
        """
        dt1 = '15/01/2021'
        dt2 = date(2021, 2, 15)
        dt3 = '15/03/2021'
        dt4 = date(2021, 4, 15)
        objeto = MyCalendar(dt1, dt2)
        objeto.add_holiday(dt3, dt4)
        objeto.add_holiday(dt1, dt2)
        assert len(objeto.datas) == 4
        assert isinstance(objeto.datas[0], date)
        assert isinstance(objeto.datas[1], date)
        assert isinstance(objeto.datas[2], date)
        assert isinstance(objeto.datas[3], date)

    def test_method_add_holiday_4(self):
        """
        Testar se método add_holiday consegue adicionar mais
        de um novo feriado, sem repetir os feriados adicionados
        anteriormente.
        """
        dt1 = '15/01/2021'
        dt2 = date(2021, 2, 15)
        dt3 = '15/03/2021'
        dt4 = date(2021, 4, 15)
        objeto = MyCalendar(dt1, dt2, dt3)
        objeto.add_holiday(dt1, dt2)
        objeto.add_holiday(dt1, dt2)
        objeto.add_holiday(dt1, dt3)
        objeto.add_holiday(dt4)
        assert len(objeto.datas) == 4

    def test_method_add_holiday_5(self):
        """
        Testar se método add_holiday é resiliente com datas mal formadas.
        """
        dt1 = '150/14/2021'
        dt2 = '15/25/2021'
        dt3 = '15/03/2021'
        objeto = MyCalendar()
        objeto.add_holiday(dt1)
        objeto.add_holiday(dt2)
        objeto.add_holiday(dt3)
        assert len(objeto.datas) == 1

    def test_method_check_holiday_1(self):
        """
        Testar se método check_holiday verifica se a data
        passada como parâmetro é feriado.
        """
        dt1 = '15/01/2021'
        dt2 = date(2021, 2, 15)
        dt3 = '15/03/2021'
        dt4 = date(2021, 4, 15)
        dt5 = '15/05/2021'
        objeto = MyCalendar(dt1, dt2, dt3)
        assert objeto.check_holiday(dt1) is True
        assert objeto.check_holiday(dt2) is True
        assert objeto.check_holiday(dt1) is True
        assert objeto.check_holiday(dt4) is False
        assert objeto.check_holiday(dt5) is False

    def test_method_check_holiday_2(self):
        """
        Testar se método check_holiday verifica se a data passada
        como parâmetro é feriado. Caso seja passada data mal formada,
        ou com erro, o retorno padrão será FALSE
        """
        dt1 = '15/01/2021'
        dt2 = date(2021, 2, 15)
        dt3 = '15/03/2021'
        dt4 = '15/05'
        dt5 = '24/24/2021'
        objeto = MyCalendar(dt1, dt2)
        assert objeto.check_holiday(dt1) is True
        assert objeto.check_holiday(dt2) is True
        assert objeto.check_holiday(dt3) is False
        assert objeto.check_holiday(dt4) is False
        assert objeto.check_holiday(dt5) is False

    def test_method_check_holiday_3(self):
        """
        Testar se método check_holiday verifica se a data passada
        como parâmetro é feriado. Caso seja passada data mal formada,
        ou com erro, o retorno padrão será FALSE
        """
        dt1 = '15/15/2021'
        dt2 = '120/3/2021'
        dt3 = '15/03/2021'
        dt4 = '15/05'
        dt5 = '24/24/2021'
        objeto = MyCalendar(dt1, dt2)
        assert objeto.check_holiday(dt1) is False
        assert objeto.check_holiday(dt2) is False
        assert objeto.check_holiday(dt3) is False
        assert objeto.check_holiday(dt4) is False
        assert objeto.check_holiday(dt5) is False
