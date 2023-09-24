from modeltranslation.translator import translator, TranslationOptions
from polls.models import PhoneModel

class PhoneTranslationOptions(TranslationOptions):
    fields = ('name','creator_name')
    required_languages = ('en', 'uz')


translator.register(PhoneModel,PhoneTranslationOptions)