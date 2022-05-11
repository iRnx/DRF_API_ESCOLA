from rest_framework import serializers

from.models import Curso, Avaliacao


#  Nesta perte definimos os campos que sera mostrado na api.
# os dados que vamos pegar, serão os que nós fizemos no models.

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}  # para n mostrar o campo de email.
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
        )
