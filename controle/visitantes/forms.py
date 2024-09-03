from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model  = Visitante
        fields = (
            "nome_completo",
            "cpf",
            "data_nascimento",
            "numero_casa",
            "placa_veiculo",
        )

        error_messages = {
            "nome_completo": {
                "required": "O nome completo é obrigatorio"
            },
            "cpf":{
                "required": "O CPF é um campo obrigatorio"
            },
            "data_nascimento":{
                "required": "A data é obrigatoria",
                "invalid": "A data precisa ter o formato DD/MM/YYYY"
            },
            "numero_casa":{
                "required": "O numero da casa é um campo obrigatorio"
            }
        }

class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required = True)

    class Meta:
        model = Visitante
        fields = [
            "morador_responsavel"
        ]
        
        error_messages = {
            "morador_responsavel":{
                "required": "informe o morador responsavel"
            }
        }
