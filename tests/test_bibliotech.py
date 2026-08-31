from src.bibliotech import (
    pode_emprestar,
    calcular_multa,
    classificar_atraso,
)


def test_rf01_usuario_ativo_sem_pendencia_e_menos_de_3_emprestimos():
    assert pode_emprestar(True, False, 0) is True
    assert pode_emprestar(True, False, 2) is True


def test_rf01_usuario_com_3_emprestimos_nao_pode_emprestar():
    assert pode_emprestar(True, False, 3) is False


def test_rf01_usuario_com_4_emprestimos_nao_pode_emprestar():
    assert pode_emprestar(True, False, 4) is False


def test_rf01_usuario_inativo_nao_pode_emprestar():
    assert pode_emprestar(False, False, 0) is False


def test_rf01_usuario_com_pendencia_nao_pode_emprestar():
    assert pode_emprestar(True, True, 0) is False


def test_rf02_sem_atraso():
    assert calcular_multa(0) == 0.0


def test_rf02_atraso_de_3_dias():
    assert calcular_multa(3) == 6.0


def test_rf02_atraso_de_7_dias():
    assert calcular_multa(7) == 14.0


def test_rf02_atraso_de_8_dias():
    assert calcular_multa(8) == 17.0


def test_rf02_atraso_de_10_dias():
    assert calcular_multa(10) == 23.0


def test_rf03_sem_atraso():
    assert classificar_atraso(0) == "sem atraso"


def test_rf03_atraso_leve():
    assert classificar_atraso(1) == "atraso leve"
    assert classificar_atraso(7) == "atraso leve"


def test_rf03_atraso_moderado():
    assert classificar_atraso(8) == "atraso moderado"
    assert classificar_atraso(30) == "atraso moderado"


def test_rf03_atraso_grave():
    assert classificar_atraso(31) == "atraso grave"
