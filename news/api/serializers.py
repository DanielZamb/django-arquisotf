from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)
        # ** desempacando diccionario en los serializadores, es como un
        # set() de todo el modelo
        # ver documentacion sobre el operador prefijo unario *,**

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)  #retorne el parametro que ya tiene la instancia en caso de que no se encuentre la llave
        instance.title = validated_data.get('title', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.publication_date = validated_data.get('publication_data', instance.publication_date)
        instance.active = validated_data.get('active', instance.active)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance



