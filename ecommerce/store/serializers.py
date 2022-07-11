from rest_framework import serializers

class GeneralSerializer(serializers.ModelSerializer):
    APPS_NAME = ['store', 'api'] # Apps in which might be needed model

    def __init__(self, *args, **kwargs):
        '''
            Retrieve key's name of dictionary, i.e. model's name and
            override kwargs["data"] to model's values, i.e. without model's name
        '''

        # Second condition is for browser, without this it won't work
        if kwargs["context"]["request"].method == 'POST' and 'data' in kwargs:
            model_name = list(kwargs["data"])[0]
            model_class = self.get_model_class_by_name(model_name)
            self.Meta.model = model_class
            model_values = list(kwargs["data"].values())[0]
            kwargs["data"] = model_values

        super().__init__(*args,  **kwargs)

    @classmethod
    def get_model_class_by_name(obj, model_name):
        '''
            Searches in models.py of apps(APPS_NAME) for corresponding
            model_name and returns that model class
        '''

        model_class = None
        
        for model in obj.APPS_NAME:
            app = __import__(model)
            model_class = getattr(app.models, model_name, None)

            if model_class is not None:
                break

        return model_class

    class Meta:
        model = None
        fields = '__all__'
