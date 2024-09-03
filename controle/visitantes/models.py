from django.db import models

class Visitante(models.Model):
    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT,
    )

    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=150,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        auto_now_add=False,
        auto_now=False,
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name="Número da casa a ser visitada",
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa do Veículo",
        max_length=7,
        blank=True,
        null=True,
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de Chegada na Portaria",
        auto_now_add=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de saída do condomínio",
        auto_now=False,
        blank=True,
        null=True,
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horário de Autorização de Entrada",
        auto_now=False,
        blank=True,
        null=True,
    )

    morador_responsavel = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada",
        max_length=50,
        blank=True,
    )

    STATUS_VISITANTE = [
        ("AGUARDANDO", " Aguardando autorização"),
        ("EM_VISITA", "Em visita"),
        ("FINALIZADO", "Visita finalizada"),
    ]

    status = models.CharField(
        verbose_name = "Status",
        max_length = 10,
        choices = STATUS_VISITANTE,
        default = "AGUARDANDO",
    )

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        
        return "horario de saida nao registrado"

    class Meta:
        verbose_name="Visitante"
        verbose_name_plural="Visitantes"
        db_table="visitante"

    def __str__(self):
        return self.nome_completo    