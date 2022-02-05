from capitulo2 import capitulo2_exercicio1
from capitulo2 import capitulo2_exercicio2
from capitulo2 import capitulo2_exercicio3
from capitulo2 import capitulo2_exercicio4
from capitulo2 import capitulo2_exercicio5
from capitulo2 import capitulo2_exercicio6
from capitulo2 import capitulo2_exercicio7
from capitulo2 import capitulo2_exercicio8
from capitulo2 import capitulo2_exercicio9
from capitulo2 import capitulo2_exercicio10
from capitulo2 import capitulo2_exercicio11
from capitulo2 import capitulo2_exercicio12
from capitulo2 import capitulo2_exercicio13
from capitulo2 import capitulo2_exercicio14
from capitulo2 import capitulo2_exercicio15
from capitulo2 import capitulo2_exercicio16
from capitulo2 import capitulo2_exercicio17
from capitulo2 import capitulo2_exercicio18
from capitulo2 import capitulo2_exercicio19
from capitulo2 import capitulo2_exercicio20


import pytest


class TestCapitulo2Exercicio1():
    def test_capitulo2_exercicio1_1(self):
        resultado = capitulo2_exercicio1('oi')
        assert isinstance(resultado, str)
        assert resultado == 'OI'

    def test_capitulo2_exercicio1_2(self):
        resultado = capitulo2_exercicio1('TCHAU')
        assert isinstance(resultado, str)
        assert resultado == 'TCHAU'

    def test_capitulo2_exercicio1_3(self):
        resultado = capitulo2_exercicio1('jOsÉ')
        assert isinstance(resultado, str)
        assert resultado == 'JOSÉ'

    def test_capitulo2_exercicio2_4(self):
        resultado = capitulo2_exercicio1('Editora Novatec')
        assert isinstance(resultado, str)
        assert resultado == 'EDITORA NOVATEC'


class TestCapitulo2Exercicio2():
    def test_capitulo2_exercicio2_1(self):
        resultado = capitulo2_exercicio2('oi')
        assert isinstance(resultado, str)
        assert resultado == 'oi'

    def test_capitulo2_exercicio2_2(self):
        resultado = capitulo2_exercicio2('TCHAU')
        assert isinstance(resultado, str)
        assert resultado == 'tchau'

    def test_capitulo2_exercicio2_3(self):
        resultado = capitulo2_exercicio2('jOsÉ')
        assert isinstance(resultado, str)
        assert resultado == 'josé'

    def test_capitulo2_exercicio2_4(self):
        resultado = capitulo2_exercicio2('Editora Novatec')
        assert isinstance(resultado, str)
        assert resultado == 'editora novatec'


class TestCapitulo2Exercicio3():
    def test_capitulo2_exercicio3_1(self):
        resultado = capitulo2_exercicio3('oi')
        assert isinstance(resultado, str)
        assert resultado == 'Oi'

    def test_capitulo2_exercicio2_2(self):
        resultado = capitulo2_exercicio3('TCHAU')
        assert isinstance(resultado, str)
        assert resultado == 'Tchau'

    def test_capitulo2_exercicio2_3(self):
        resultado = capitulo2_exercicio3('jOsÉ')
        assert isinstance(resultado, str)
        assert resultado == 'José'

    def test_capitulo2_exercicio2_4(self):
        resultado = capitulo2_exercicio3('Editora Novatec')
        assert isinstance(resultado, str)
        assert resultado == 'Editora novatec'


class TestCapitulo2Exercicio4():
    def test_capitulo2_exercicio4_1(self):
        resultado = capitulo2_exercicio4('correndo')
        assert resultado is True

    def test_capitulo2_exercicio4_2(self):
        resultado = capitulo2_exercicio4('andando')
        assert resultado is True

    def test_capitulo2_exercicio4_3(self):
        resultado = capitulo2_exercicio4('sorrindo')
        assert resultado is True

    def test_capitulo2_exercicio4_4(self):
        resultado = capitulo2_exercicio4('Pássado voando pelo ar')
        assert resultado is False


class TestCapitulo2Exercicio5():
    def test_capitulo2_exercicio5_1(self):
        resultado = capitulo2_exercicio5('123mudar')
        assert resultado == 8

    def test_capitulo2_exercicio5_2(self):
        resultado = capitulo2_exercicio5('123')
        assert resultado == 3

    def test_capitulo2_exercicio5_3(self):
        resultado = capitulo2_exercicio5('senha')
        assert resultado == 5

    def test_capitulo2_exercicio5_4(self):
        resultado = capitulo2_exercicio5('S@3!345!@')
        assert resultado == 9


class TestCapitulo2Exercicio6():
    def test_capitulo2_exercicio6_1(self):
        resultado = capitulo2_exercicio6('123mudar')
        assert resultado is False

    def test_capitulo2_exercicio6_2(self):
        resultado = capitulo2_exercicio6('123')
        assert resultado is True

    def test_capitulo2_exercicio6_3(self):
        resultado = capitulo2_exercicio6('senha')
        assert resultado is False

    def test_capitulo2_exercicio6_4(self):
        resultado = capitulo2_exercicio6('S@3!345!@')
        assert resultado is False


class TestCapitulo2Exercicio7():
    def test_capitulo2_exercicio7_1(self):
        resultado = capitulo2_exercicio7('nova', 'Editora Novatec')
        assert resultado is False

    def test_capitulo2_exercicio7_2(self):
        resultado = capitulo2_exercicio7('Editora', 'Editora Novatec')
        assert resultado is True

    def test_capitulo2_exercicio7_3(self):
        resultado = capitulo2_exercicio7('editora', 'Editora Novatec')
        assert resultado is False

    def test_capitulo2_exercicio7_4(self):
        resultado = capitulo2_exercicio7('Novatec', 'Editora Novatec')
        assert resultado is True


class TestCapitulo2Exercicio8():
    def test_capitulo2_exercicio8_1(self):
        resultado = capitulo2_exercicio8('nova', 'Editora Novatec')
        assert resultado is True

    def test_capitulo2_exercicio8_2(self):
        resultado = capitulo2_exercicio8('Editora', 'Editora Novatec')
        assert resultado is True

    def test_capitulo2_exercicio8_3(self):
        resultado = capitulo2_exercicio8('editora', 'Editora Novatec')
        assert resultado is True

    def test_capitulo2_exercicio8_4(self):
        resultado = capitulo2_exercicio8('Novatec', 'Editora Novatec')
        assert resultado is True


class TestCapitulo2Exercicio9():
    def test_capitulo2_exercicio9_1(self):
        resultado = capitulo2_exercicio9(42)
        assert resultado == '0b101010'

    def test_capitulo2_exercicio9_2(self):
        resultado = capitulo2_exercicio9('42')
        assert resultado == '0b101010'

    def test_capitulo2_exercicio9_3(self):
        resultado = capitulo2_exercicio9('42a')
        assert resultado == 'Número inválido'

    def test_capitulo2_exercicio9_4(self):
        resultado = capitulo2_exercicio9('123')
        assert resultado == '0b1111011'


class TestCapitulo2Exercicio10():
    def test_capitulo2_exercicio10_1(self):
        resultado = capitulo2_exercicio10('editora novatec')
        assert resultado == 'Editora Novatec'

    def test_capitulo2_exercicio10_2(self):
        resultado = capitulo2_exercicio10('o dia está lindo')
        assert resultado == 'O Dia Está Lindo'

    def test_capitulo2_exercicio10_3(self):
        resultado = capitulo2_exercicio10('o DiA EstÁ LiNdO')
        assert resultado == 'O Dia Está Lindo'

    def test_capitulo2_exercicio10_4(self):
        resultado = capitulo2_exercicio10('editora NovAtEc')
        assert resultado == 'Editora Novatec'


class TestCapitulo2Exercicio11():
    def test_capitulo2_exercicio11_1(self):
        resultado = capitulo2_exercicio11('Palavra hacker')
        assert resultado == 'P@l@vr@ h@ck$r'

    def test_capitulo2_exercicio11_2(self):
        resultado = capitulo2_exercicio11('o dia está lindo')
        assert resultado == '0 dY@ $stá lYnd0'

    def test_capitulo2_exercicio11_3(self):
        resultado = capitulo2_exercicio11('o DiA EstÁ LiNdO')
        assert resultado == '0 DYA EstÁ LYNdO'

    def test_capitulo2_exercicio11_4(self):
        resultado = capitulo2_exercicio11('editora NovAtEc')
        assert resultado == '$dYt0r@ N0vAtEc'


class TestCapitulo2Exercicio12():
    def test_capitulo2_exercicio12_1(self):
        resultado = capitulo2_exercicio12('Palavra hacker')
        assert resultado == 'p@l@vr@ h@ck$r'

    def test_capitulo2_exercicio12_2(self):
        resultado = capitulo2_exercicio12('o dia está lindo')
        assert resultado == '0 dY@ $stá lYnd0'

    def test_capitulo2_exercicio12_3(self):
        resultado = capitulo2_exercicio12('o DiA EstÁ LiNdO')
        assert resultado == '0 dY@ $stá lYnd0'

    def test_capitulo2_exercicio12_4(self):
        resultado = capitulo2_exercicio12('editora NovAtEc')
        assert resultado == '$dYt0r@ n0v@t$c'


class TestCapitulo2Exercicio13():
    def test_capitulo2_exercicio13_1(self):
        resultado = capitulo2_exercicio13('Palavra hacker')
        assert resultado == 'PALAVRA HACKER'

    def test_capitulo2_exercicio13_2(self):
        resultado = capitulo2_exercicio13('Palavra')
        assert resultado == 'palavra'

    def test_capitulo2_exercicio13_3(self):
        resultado = capitulo2_exercicio13('o DiA EstÁ LiNdO')
        assert resultado == 'O DIA ESTÁ LINDO'

    def test_capitulo2_exercicio13_4(self):
        resultado = capitulo2_exercicio13('editora NovAtEc')
        assert resultado == 'editora novatec'


class TestCapitulo2Exercicio14():
    def test_capitulo2_exercicio14_1(self):
        resultado = capitulo2_exercicio14('Palavra hacker')
        assert resultado == 'rekcah arvalaP'

    def test_capitulo2_exercicio14_2(self):
        resultado = capitulo2_exercicio14('O dia está lindo')
        assert resultado == 'odnil átse aid O'

    def test_capitulo2_exercicio14_3(self):
        resultado = capitulo2_exercicio14('Editora Novatec')
        assert resultado == 'cetavoN arotidE'

    def test_capitulo2_exercicio14_4(self):
        resultado = capitulo2_exercicio14('editora Novatec')
        assert resultado == 'cetavoN arotide'


class TestCapitulo2Exercicio15():
    def test_capitulo2_exercicio15_1(self):
        resultado = capitulo2_exercicio15('Editora Novatec')
        assert resultado is False

    def test_capitulo2_exercicio15_2(self):
        texto = 'socorram me subino onibus em marrocos'
        resultado = capitulo2_exercicio15(texto)
        assert resultado is True

    def test_capitulo2_exercicio15_3(self):
        resultado = capitulo2_exercicio15('ovos')
        assert resultado is False

    def test_capitulo2_exercicio15_4(self):
        resultado = capitulo2_exercicio15('ovo')
        assert resultado is True


class TestCapitulo2Exercicio16():
    def test_capitulo2_exercicio16_1(self):
        resultado = capitulo2_exercicio16('Editora Novatec', 'e')
        assert resultado == 'Editora Novatc'

    def test_capitulo2_exercicio16_2(self):
        resultado = capitulo2_exercicio16('Editora Novatec', 'o')
        assert resultado == 'Editra Nvatec'

    def test_capitulo2_exercicio16_3(self):
        resultado = capitulo2_exercicio16('Editora Novatec', 'a')
        assert resultado == 'Editor Novtec'

    def test_capitulo2_exercicio16_4(self):
        resultado = capitulo2_exercicio16('Editora Novatec', 'ova')
        assert resultado == 'Editora Ntec'


class TestCapitulo2Exercicio17():
    def test_capitulo2_exercicio17_1(self):
        resultado = capitulo2_exercicio17('Editora Novatec')
        assert resultado == 'Editora NovatecEditora Novatec'

    def test_capitulo2_exercicio17_2(self):
        resultado = capitulo2_exercicio17('palavra')
        assert resultado == 'palavrapalavra'

    def test_capitulo2_exercicio17_3(self):
        resultado = capitulo2_exercicio17('O dia está lindo')
        assert resultado == 'O dia está lindoO dia está lindo'

    def test_capitulo2_exercicio17_4(self):
        resultado = capitulo2_exercicio17('ovo')
        assert resultado == 'ovoovo'


class TestCapitulo2Exercicio18():
    def test_capitulo2_exercicio18_1(self):
        resultado = capitulo2_exercicio18('Editora Novatec')
        assert resultado == 'Editora'

    def test_capitulo2_exercicio18_2(self):
        resultado = capitulo2_exercicio18('A casa é amarela')
        assert resultado == 'A'

    def test_capitulo2_exercicio18_3(self):
        resultado = capitulo2_exercicio18('O dia está lindo')
        assert resultado == 'O'

    def test_capitulo2_exercicio18_4(self):
        resultado = capitulo2_exercicio18('Editora')
        assert resultado == 'Editora'


class TestCapitulo2Exercicio19():
    def test_capitulo2_exercicio19_1(self):
        resultado = capitulo2_exercicio19('Editora Novatec')
        assert resultado == 'Novatec'

    def test_capitulo2_exercicio19_2(self):
        resultado = capitulo2_exercicio19('A casa é amarela')
        assert resultado == 'amarela'

    def test_capitulo2_exercicio19_3(self):
        resultado = capitulo2_exercicio19('O dia está lindo')
        assert resultado == 'lindo'

    def test_capitulo2_exercicio19_4(self):
        resultado = capitulo2_exercicio19('Editora')
        assert resultado == 'Editora'


class TestCapitulo2Exercicio20():
    def test_capitulo2_exercicio20_1(self):
        resultado = capitulo2_exercicio20('123mud@r')
        assert resultado is True

    def test_capitulo2_exercicio20_2(self):
        resultado = capitulo2_exercicio20('senha#Forte')
        assert resultado is True

    def test_capitulo2_exercicio20_3(self):
        resultado = capitulo2_exercicio20('123mudar')
        assert resultado is False

    def test_capitulo2_exercicio20_4(self):
        resultado = capitulo2_exercicio20('123')
        assert resultado is False
